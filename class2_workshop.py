dist = float(input("How far do u want to deliver? "))
print("You want to deliver", dist,"km")
if dist > 5:
    if dist > 500:
        price = 45
    elif 301 <= dist <= 500:
        price = 35
    elif 101 <= dist <= 300:
        price = 25
    elif 51 <= dist <= 100:
        price = 15
    if dist < 51:
        price = 10
    print("You need to pay", price, "baht")
else:
    print("Nah I'd bid")
    

# Descending order can prevent error.
