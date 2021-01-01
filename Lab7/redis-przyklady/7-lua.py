from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

# Przekazywanie w komendzie eval ciało skryptu napisanego w lua. Redis odbiera kod, 
# wykonuje i zwraca rezultat. Wyświetlenie słowa test. Drugi argument eval to 0, 
# określa ilość argumentów które można przekazać do skrypti/ Lua ideksuje od 1, 
# wszystko przekazane jest do tabeli argv.

script ="""
return "testuje"
"""

print(redis_connection.eval(script,0))