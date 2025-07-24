# score = int(input("Enter score: "))

# def grade(score):
#     if score >= 80:
#         print("Grade A")
#     elif score >= 70:
#         print("Grade B")
#     elif score >= 60:
#         print("Grade C")

# grade()

# def my_cum(a, b):
#     cum = a * b
#     return cum

# print(my_cum(2, 5))

# def price_cal1(a, p):
#     price = (a * p) * 1.07
#     return price

# while True:
#     menu = int(input("1 - Continue     2 - Exit\n:"))
#     if menu == 1:
#         a = int(input("Amout: "))
#         p = int(input("Price: "))
#         print(price_cal1(a, p))
#         break
        
#     if menu == 2:
#         print("Thank You")
#         break

# def price_cal():
#     while True:
#         menu = int(input("1 - Continue     2 - Exit\n:"))
#         if menu == 1:
#             a = int(input("Amout: "))
#             p = int(input("Price: "))
#             print(price_cal1(a, p))
#             break
        
#         if menu == 2:
#             print("Thank You")
#         break
# price_cal()             call function


# my_dick = {"name": "BOMBA", "age": 69}
# # print(my_dick["name"])
# my_dick["IT"] = 0
# print(my_dick)

# room = [
#     {"Name": "A", "Age": 1, "Gender": "Male"},
#     {"Name": "B", "Age": 2, "Gender": "Female"},
#     {"Name": "C", "Age": 3, "Gender": "Male"}
# ]
# for i in room:
#     print(i["Age"])

movie_lists = [
    {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
    {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
    {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
    {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
    {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

def show_movies(movie_list):
    for i in movie_list:
        lists = i['movie_name']
        price = i['ticket_price']
        price_list = lists, price
        return price_list
print(show_movies(movie_lists))