from redis import Redis

redis_connection = Redis(decode_responses=True)

# przypisanie własnych wartości
klucz ="jagoda"
wartosc ="styczen"

# odczytanie wartości
redis_connection.set(klucz, wartosc)
print(redis_connection.get(klucz))

# dodanie wartości poprzez append
redis_connection.append(klucz, "-teraz")
print(redis_connection.get(klucz))

# usunięcie klucza poprzez delete
redis_connection.delete(klucz)
print(redis_connection.get(klucz))

