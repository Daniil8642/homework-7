# main.py
from mongoengine import connect
from models import Author, Quote
from load_data import load_authors, load_quotes
from search_quotes import search_quotes

# Замініть 'your_connection_string' на реальний рядок підключення з MongoDB Atlas
connect(host='your_connection_string')

def main():
    # Завантаження даних у базу даних
    load_authors()
    load_quotes()

    while True:
        user_input = input("Enter command (e.g., 'name: Steve Martin', 'tag: life', 'tags: life,live', 'exit'): ")
        if user_input.lower() == 'exit':
            break
        command, value = user_input.split(':')
        search_quotes(command.strip(), value.strip())

if __name__ == '__main__':
    main()
