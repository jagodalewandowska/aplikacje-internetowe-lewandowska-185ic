from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="przykladowa-lista"

# wyświetla wartości [1,2,3,4,5], dodanie poprzez rpush
redis_connection.rpush(list_key,1,2,3,4,5)

# pobiranie z listy od indeksu 0 do -1, czyli do końca
print(redis_connection.lrange(list_key,0, -1))

# zwrocenie innych wartosci
print(redis_connection.lrange(list_key,2, 3))