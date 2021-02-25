from config.global_params import redis
import json


class Redis(object):
    '''custom redis object'''

    def get_val(self, key: str):
        res = redis.get(key)
        if res:
            try:
                res = json.loads(res)
            except json.JSONDecodeError:
                pass
        return res

    def set_val(self, key: str, val, ex: int):
        try:
            if not isinstance(val, str):
                val = json.dumps(val)
            return redis.set(key, val, ex=ex)
        except:
            raise Exception(f'{type(val)} val jsonify failed. :{val}')


r = Redis()