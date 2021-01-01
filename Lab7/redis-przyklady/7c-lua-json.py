from redis import Redis
from json import dumps

redis_connection = Redis(decode_responses=True, db=0)

script ="""
local json_data = KEYS[1]
local decoded_data = cjson.decode(json_data)
return decoded_data['a'] + decoded_data['b']
"""

# wynik to 27
print(redis_connection.eval(script,1, dumps({'a': 15,'b': 12})))