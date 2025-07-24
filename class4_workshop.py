
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
        price_list = lists + price
        return price_list
    
def main():

    while True:
        menu = int(input("1 - Show Lists     2 - Buy Ticket\n:"))
        if menu == 1:
            show_movies()


        if menu == 2:
            print("Thank You")
        break
