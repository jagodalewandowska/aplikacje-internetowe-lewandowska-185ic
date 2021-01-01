from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

# przygotowanie danych

permission ='ADD_BOOKING'

# utworzenie groupy oraz listy o zakresie od 0 do 50
redis_connection.sadd("users_group:2", *list(range(0,50)))

redis_connection.sadd('permissions', permission)

# dodanie skryptu, wszyscy użytkownicy otrzymują uprawnienia - wypełniona jest 
# lista ich ID oraz uprawnienie. sprawdzenie czy jest poprawne i dla każdego 
# użytkownika dodane jest to uprawnienie. duplikaty są zamieniane poprzez 
# user_permissions:ID to SET - nie pozwalając na nie

add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""

print(redis_connection.eval(add_permission_script,2,2, permission))