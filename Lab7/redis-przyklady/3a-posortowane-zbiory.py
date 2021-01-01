from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("posortowane_klucze",{"klucz1": 2})
redis_connection.zadd("posortowane_klucze",{"klucz2": 8})
redis_connection.zadd("posortowane_klucze",{"klucz3": 24})
redis_connection.zadd("posortowane_klucze",{"klucz4": 48})

# wyświetlenie wsyzstkich kluczy
print(redis_connection.zrange("posortowane_klucze", 0, -1))