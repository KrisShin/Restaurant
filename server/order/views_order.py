from flask import Blueprint, json, jsonify, request
from config.global_params import db
from config.status_code import *
from config.settings import ORDER_STATUS
from utils.wraps import auth, get_userId
from user.models import User, Address
from dish.models import Dish
from .models import Order, Comment

order = Blueprint('Order', __name__, url_prefix='/order')


@order.route('/<string:order_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth
def operate_order(order_id):
    if request.method == 'GET':
        order = Order.query.filter_by(id=order_id).first()
        return jsonify({'success': True, 'data': {'order': dict(order)}})
    if request.method == 'PUT':
        return jsonify({'success': True})
    if request.method == 'POST':
        data = request.get_json()
        cart = data.get('cart')
        note = data.get('note')
        addr_id = data.get('addrId')
        if not cart:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        cart = json.loads(cart)

        dish_amount = {k: v for k, v in cart.items() if v}
        if not dish_amount:
            return jsonify({'success': False, 'code': ORDER_EMPTY_CART})
        user = User.query.filter_by(id=get_userId(request)).first()
        addr = Address.query.filter_by(id=addr_id).first()
        if not addr:
            addr = Address.query.filter(
                Address.user == user, Address.is_default == True).first()
        dishes = Dish.query.filter(Dish.id.in_(dish_amount.keys())).all()
        money = 0
        for dish in dishes:
            money += dish_amount[str(dish.id)] * \
                dish.price*dish.discount.discount
        money = round(money, 2)

        order = Order(
            note=note,
            money=money,
            dish_amount=dish_amount,
            address=addr,
            user=user,
            dishes=dishes,
        )
        db.session.add(order)
        db.session.commit()
        return jsonify({'success': True, 'data': {'id': order.id}})
    if request.method == 'DELETE':
        order = Order.query.filter_by(id=order_id).first()
        order.delete()
        db.session.commit()
        return jsonify({'success': True})


@order.route('/list', methods=['POST'])
@auth
def post_order_list():
    user = User.query.filter_by(id=get_userId(request)).first()
    point = request.get_json().get('point', 0)
    print(point)
    orders = [dict(order) for order in user.orders[point:point+5]]
    return jsonify({'success': True, 'data': {'orders': orders}})


@order.route('/status', methods=['GET'])
@auth
def get_order_status():
    user = User.query.filter_by(id=get_userId(request)).first()
    order_status = {
        'waitPay': 0,
        'paid': 0,
        'gotOrder': 0,
        'waitComment': 0,
        'doneOrder': 0,
        'cancelOrder': 0
    }
    for order in user.orders:
        order_status[ORDER_STATUS[order.status]] += 1
    return jsonify({'success': True, 'data': {'orderStatus': order_status, 'orderCount': len(user.orders)}})


@order.route('/pay', methods=['POST'])
@auth
def post_order_pay():
    id = request.get_json().get('id')
    user = User.query.filter_by(id=get_userId(request)).first()
    order = Order.query.filter_by(id=id).first()
    user.account.balance -= order.money
    order.status = 2
    db.session.commit()
    return jsonify({'success': True})


@order.route('/cancel', methods=['POST'])
@auth
def post_order_cancel():
    id = request.get_json().get('id')
    user = User.query.filter_by(id=get_userId(request)).first()
    order = Order.query.filter_by(id=id).first()
    msg = ''
    if order.status == 1:
        order.status = 0
    elif order.status == 2:
        user.account.balance += order.money
        order.status = 0
    elif 6 > order.status > 2:
        msg = '等待商家审批退款'
        order.status = 6
    elif order.status in [0, 6]:
        msg = '该状态下无法退款, 如有疑问请前往申诉'
    db.session.commit()
    return jsonify({'success': True, 'data': {'message': msg}})
