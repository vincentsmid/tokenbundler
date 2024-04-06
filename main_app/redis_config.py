import redis


def get_redis_client():
    return redis.Redis(host="redis", port=6379, db=0, decode_responses=True)


async def redis_dependency():
    client = get_redis_client()
    try:
        yield client
    finally:
        client.close()
