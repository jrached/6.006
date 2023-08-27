from flix_chill import FlixChillManager

fcm = FlixChillManager()

for i in range(1,101):
    fcm.insert(i,i,i)

print(fcm)

print(fcm.highest(40))
