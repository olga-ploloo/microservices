from shop_service.app.core.config import settings
import redis

redis = redis.Redis(host=settings.redis.host,
                    port=settings.redis.port,
                    db=settings.redis.db)


class Cart:
    _EXPIRED_TIME: int = settings.EXPIRED_TIME

    @classmethod
    def add_to_cart(cls, **kwargs):
        user_id = kwargs['user_id']
        # check if cart already exists
        for user_carts in redis.scan_iter(f"carts:{user_id}:*"):
            data = {index.decode('utf-8'): value.decode('utf-8') for index, value in redis.hgetall(user_carts).items()}
            if int(data['user_id']) == user_id and int(data['product_id']) == kwargs['product_id']:
                return 'Item already in cart'
            print(data)
        kwargs['row_id'] = uuid.uuid4().hex
        key = f"carts:{user_id}:{kwargs['row_id']}"
        # store cart to redis
        [redis.hset(key, index, value) for index, value in kwargs.items()]
        # set expired shopping cart
        redis.expire(key, cls._EXPIRED_TIME)
        result = {key.decode('utf-8'): value.decode('utf-8') for key, value in redis.hgetall(key).items()}
        return result

    @classmethod
    def carts(cls, user_id):
        result = []
        for user_carts in redis.scan_iter(f"carts:{user_id}:*"):
            data = {index.decode('utf-8'): value.decode('utf-8') for index, value in redis.hgetall(user_carts).items()}
            result.append(data)
        return result

    @classmethod
    def delete_cart(cls, user_id, rowId):
        # if return 1 is true and return 0 is false it's mean data doesn't exists
        return redis.delete(f"carts:{user_id}:{rowId}")

    @classmethod
    def delete_all_carts(cls, user_id):
        [redis.delete(x) for x in redis.scan_iter(f"carts:{user_id}:*")]
