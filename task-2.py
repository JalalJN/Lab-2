import csv

def find_books_by_author(file_path, author_name, minimum_price=200):
    matching_books = []

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=';')

            for record in csv_reader:
             
                if author_name.lower() in record[2].lower():
                    try:
                       
                        book_price = float(record[6].replace(',', '.'))
                        if book_price >= minimum_price:
                            matching_books.append(record)
                    except ValueError:
                        print(f"Invalid price format encountered: {record[6]}")

        return matching_books

    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


file_path = 'books-en.csv'
author_name = input("Enter the author's name to search for: ")

books = find_books_by_author(file_path, author_name)

if books:
    print(f"\u001b[44mBooks by {author_name} priced above 200:\u001b[0m")

    total_books = 0
    for book in books:
        print(f"Title: {book[1]}, Price: {book[6]}")
        total_books += 1

    print(f"Total number of matching books: {total_books}")
else:
    print(f"No books found by {author_name} priced above 200.")
