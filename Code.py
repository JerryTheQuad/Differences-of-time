a_hour = int(input())
a_min = int(input())
a_sec = int(input())

b_hour = int(input())
b_min = int(input())
b_sec = int(input())

a_sec += (a_hour * 3600) + (a_min * 60)
b_sec += (b_hour * 3600) + (b_min * 60)

result = b_sec - a_sec

print(result)
