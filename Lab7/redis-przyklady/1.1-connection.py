# import redisa po instalacji
from redis import Redis
redis_connection = Redis()
# redis uruchomiony jest na standardowym porcie bez hasła,
# więc łączy się do localhost:6379, dane uznawane za domyślne
print(redis_connection.ping())