from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

# nazwa strumienia
stream_name ='strumien'

# dodanie nowego klucza
redis_connection.xadd(stream_name,{'klucz': 'wartosc'})
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1)
print(message)