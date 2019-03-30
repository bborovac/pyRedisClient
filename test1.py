import redis

redisServer = "192.168.99.100"

r = redis.Redis(host=redisServer, port=6379, db=0)

a = r.get("examplekey 2")

print (a)

