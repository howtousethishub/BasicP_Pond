# haverice = True
# havespoon = False

# if haverice:
#     if havespoon:
#         print("กินข้าว")

# x = bool(input("Give me something.--> "))
# print(x)        Always true if input is real

#---------------------------------------------------------------------------------------

# score = float(input("Enter score: "))
# if 100 >= score:
#     if score >= 80:
#         print("Grade A")             # Ver1
#     if 80 > score >= 70:             # Value between can only use in Python!!  
#         print("Grade B")
#     if 70 > score >= 60:
#         print("Grade C")
#     if 60 >score >= 50:
#         print("Grade D")
#     if score < 50:
#         print("Ai Kwai")
# if score > 100:
#     print("cappa")

#---------------------------------------------------------------------------------------

# score = int(input("Enter score: "))
# if score >= 0:
#     if score <= 100:                 # Ver 2
#         if score >= 80:              # Nested if ***
#             print("Grade A")
#         if score >= 70:
#             if score < 80:
#                 print("Grade B")
#         if score >= 60:
#             if score < 70:
#                 print("Grade C")
#         if score >= 50:
#             if score < 60:
#                 print("Grade D")
#         if score >50:
#             print("Ai Kwai")
    
#---------------------------------------------------------------------------------------

# for x in range(0, 16, 2):
#     print(x)

# i = 0
# while i != 5:
#     i = i + 1
#     print(i)

#---------------------------------------------------------------------------------------
    
while True:
    choice = int(input("Type '1' to START, '2' to EXIT : "))

    if choice == 1:
        num = int(input("Amount of number u want to sum: "))
        summation = 0

        for i in range(num):
            num1 = int(input("Give number: "))
            summation = summation + num1

        print("Result:", summation)

    if choice == 2:
        print("Bye Bye")
        break