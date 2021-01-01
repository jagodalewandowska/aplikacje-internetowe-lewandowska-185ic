from redis import Redis

redis_connection = Redis()

# przypisanie własnych wartości
klucz ="jagoda"
wartosc ="styczen"

# odczytanie wartości
redis_connection.set(klucz, wartosc)
print(redis_connection.get(klucz))