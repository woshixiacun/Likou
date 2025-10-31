flights = input().split(",")

flights.sort(key=lambda x: (x[0:2], x[2:]))

print(",".join(flights))