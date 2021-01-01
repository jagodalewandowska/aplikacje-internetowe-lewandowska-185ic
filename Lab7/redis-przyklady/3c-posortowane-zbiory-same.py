from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("posortowane_klucze",{"klucz1": 1})
redis_connection.zadd("posortowane_klucze",{"klucz2": 1})
redis_connection.zadd("posortowane_klucze",{"klucz3": 1})
redis_connection.zadd("posortowane_klucze",{"klucz4": 1})

# wyświetlenie wsyzstkich kluczy
print(redis_connection.zrange("posortowane_klucze", 0, -1, withscores=True))