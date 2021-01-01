from redis import Redis

redis_connection = Redis(decode_responses=True)

# przypisanie własnych wartości
klucz ="jagoda"
wartosc =24

# odczytanie wartości
redis_connection.set(klucz, wartosc)
print(redis_connection.get(klucz))

# zwiększenie o 240
print(redis_connection.incr(klucz,240))

# odjęcie 2400
print(redis_connection.decr(klucz,2400))
