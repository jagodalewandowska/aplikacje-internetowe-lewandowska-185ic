from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='test'

while True:
    # nowe elementy $ zamiast 0-0
    message = redis_connection.xread({stream_name: '$'}, block=10, count=1)
    print(message)