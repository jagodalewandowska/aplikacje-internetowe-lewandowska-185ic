from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

redis_connection.set("key1",11)

script ="""
local arg1 = redis.call('get','key1')
redis.call('set', 'key2', arg1 + KEYS[1])
return nil
"""

# wyświetla none, bo "return nil"
print(redis_connection.eval(script,1,5))  

# wynik dodawania
print(redis_connection.get("key2"))