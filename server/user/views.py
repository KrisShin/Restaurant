from flask import Blueprint, jsonify, request, session
from flask_login import current_user, login_required, login_user, logout_user
from .models import User, Address
from utils.util import make_password, check_password, get_captcha, sender
from config.global_params import db, login_manager
import re
from utils.rest_redis import r

user = Blueprint('User', __name__, url_prefix='/user')


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@user.route('/register', methods=['POST'])
def user_register():
    '''register a new user.
    resp:
    {
        "success": true,
        "info": "OK",
        "data":{
            "phone":"13433334444"
        }
    }
    '''
    data = request.get_json()
    nickname = data.get('nickname')
    phone = data.get('phone')

    # check phone number
    reg_phone = r'^1[3-9]\d{9}$'
    if not re.match(reg_phone, phone):
        return jsonify({'success': False, 'info': '手机号格式错误'})

    gender = data.get('gender')
    password = make_password(data.get('password'))
    age = data.get('age')
    user = User(nickname=nickname, phone=phone, age=age,
                password=password, gender=gender, avatar='/static/avatar/default.jpg')
    db.session.add(user)
    db.session.commit()

    return jsonify({'success': True,
                    'info': '',
                    'data': {'phone': phone}})


@user.route('/login', methods=['POST'])
def user_login():
    '''Login user by phone and password.
    resp:
    {
        "success": true,
        "info": "OK",
        "data": {
            "user_id": user_id,
            "nickname": nickname,
            "is_vip": true/false,
            "is_active": true/false,
            "is_new": true/false,
            "gender": true/false,
            "balance": 0.00,
            // 下面的内容完善中, 暂时会写死或者返回空值
            "tags":["微辣", "甜点", "奶茶", "小龙虾"],
            "push_dishes":[
                {
                    "name":"鱼香肉丝",
                    "img":"dish_img_url", 
                    "tag":["微辣","酸甜"],
                    "price":23.78, 
                    "amount":18 // 累计销量
                },
            ]
        }
    }
    '''

    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    user = User.query.filter_by(phone=phone).first()
    if not user:
        return jsonify({'success': False, 'info': '用户未注册'})

    if not check_password(password, user.password):
        return jsonify({'success': False, 'info': '密码错误'})

    login_user(user)
    return jsonify({})


@user.route('/logout', methods=['POST', 'GET'])
@login_required
def user_logout():
    logout_user()
    return jsonify({'sucess': True, 'info': ''})


@user.route('/email_captcha', methods=['POST'])
def send_captcha_email():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'success': False, 'info': '请输入你注册绑定的邮箱'})
    # user = User.query.filter_by(email=email).first()

    if r.get_val(f'user_1:get_captcha'):
        return jsonify({'success': False, 'info': '验证码已发送, 请稍后再试'})

    captcha = get_captcha()
    mail = {
        'subject': f'恰了木有验证码',
        'content': f'<div>感谢您使用恰了木有APP, 您的验证码为</div><span style="font-size: 30px;font-weight: 600;background: #313131;color: #6dc4ff;">{captcha}</span><div>请在5分钟之内完成验证</div>'}
    r.set_val(f'user_1:get_captcha', captcha, 300)
    sender.send(email, mail)
    return jsonify({'success': True, 'info': ''})


@user.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "GET":
        print(r.get_val('hello'))
        return jsonify({'msg': 'method GET ok'})

    if request.method == "POST":
        r.set_val("hello", 123, 10)
        print('ok')
        # data = request.get_json()
        # nickname = data.get('nickname')
        # phone = data.get('phone')
        # gender = data.get('gender')
        # password = make_password(data.get('password'))
        # age = data.get('age')
        # user = User(nickname=nickname, phone=phone, age=age,
        #             password=password, gender=gender, avatar='/static/avatar/default.jpg')
        # db.session.add(user)
        # db.session.commit()

        return jsonify({'msg': 'OK'})
