import os

# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_FOLDER = os.path.join(BASE_DIR, 'statics')
STATIC_PATH = '/static'

# upload file absolute directory
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

SALT = r'0.3qxl9vc_j7kv!ja'
KEY = r'734&jai<,oqe).ac'


REDIS_USER = ''
REDIS_PWD = ''  # r"R3D1Su@er"
REDIS_HOST = r'localhost'
REDIS_PORT = r'6379'
REDIS_DB = 0

REDIS_URL=f"redis://{REDIS_USER}:{REDIS_PWD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"


EMAIL_NICKNAME = r'恰了木有APP'
EMAIL_ACCOUNT = r'2855829886@qq.com'
EMAIL_AUTH = r'tdlzctihcooodgbc'


HTTP_HOST = 'http://127.0.0.1:9096'


TAG_COLOR = {
    0: '#cccccc',
    1: '#808089',
    2: '#aa3030',
    3: '#ff00ff',
    4: '#0000ff',
    5: '#00ffff',
    6: '#00ff00',
    7: '#cccc00',
    8: '#ff5500',
    9: '#ff0000',
}

# TODO: Constract the ORDER_STATUS code with list, and the numeric status code should be index of the list

ORDER_CANCELED = 0
ORDER_UNPAY = 1
ORDER_PAID = 2
ORDER_ACCEPTED = 3
ORDER_COMMNETED = 4
ORDER_COMPLETE = 5
ORDER_REFUNDING = 6

ORDER_STATUS = {
    ORDER_CANCELED: 'orderCanceled',
    ORDER_UNPAY: 'orderUnpay',
    ORDER_PAID: 'orderPaid',
    ORDER_ACCEPTED: 'orderAccept',
    ORDER_COMMNETED: 'orderCommented',
    ORDER_COMPLETE: 'orderComplete',
    ORDER_REFUNDING: 'orderRefund'
}

ORDER_STATUS_REVERSE = {
    'orderCanceled': ORDER_CANCELED,
    'orderUnpay': ORDER_UNPAY,
    'orderPaid': ORDER_PAID,
    'orderAccept': ORDER_ACCEPTED,
    'orderCommented': ORDER_COMMNETED,
    'orderComplete': ORDER_COMPLETE,
    'orderRefund': ORDER_REFUNDING
}
