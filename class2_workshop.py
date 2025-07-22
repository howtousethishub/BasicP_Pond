dist = int(input("How far do u want to deliver? \n"))
print("You want to deliver", dist,"km")
if 5 <= dist <= 500:
    if dist < 51:
        price = 10
    elif 51 <= dist <= 100:
        price = 15
    elif 101 <= dist <= 300:
        price = 25
    elif 301 <= dist <= 500:
        price = 35
    elif dist > 500:
        price = 45
    print("You need to pay", price, "baht")
else:
    print("Nah I'd bid")

# Descending order can prevent error.
