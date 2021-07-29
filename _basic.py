age = int(input())
payment = [500, 1000, 1500]
if age < 14:
    print(payment[0])
elif age < 17:
    print(payment[1])
else:
    print(payment[2])