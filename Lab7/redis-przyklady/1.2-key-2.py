from redis import Redis

redis_connection = Redis(decode_responses=True) # <--- zmiana

# przypisanie własnych wartości
klucz ="jagoda"
wartosc ="styczen"

# odczytanie wartości
redis_connection.set(klucz, wartosc)
print(redis_connection.get(klucz))