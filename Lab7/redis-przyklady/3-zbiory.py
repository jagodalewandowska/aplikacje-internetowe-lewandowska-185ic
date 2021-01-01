from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("klucz","jagoda")
redis_connection.sadd("klucz","magdalena")
redis_connection.sadd("klucz","gdynia")
redis_connection.sadd("klucz","grudziadz")

print(redis_connection.smembers("klucz"))