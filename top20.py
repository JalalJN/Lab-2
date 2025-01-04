import csv

def analyze_books(file_path):
    unique_publishers = set()
    book_data = []

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=';')

            for record in csv_reader:
               
                if len(record) < 7:
                    continue

                isbn, title, author, year, publisher, downloads, price = record
                unique_publishers.add(publisher)

                try:
                    
                    download_count = int(downloads)
                    book_data.append((title, author, publisher, download_count))
                except ValueError:
                    print(f"Invalid downloads value: {downloads}")

       
        top_books = sorted(book_data, key=lambda book: book[3], reverse=True)[:20]

        print("Unique Publishers:")
        for pub in sorted(unique_publishers):
            print(pub)

        print("\nTop 20 Books by Download Count:")
        for book in top_books:
            print(f"Title: {book[0]}, Author: {book[1]}, Publisher: {book[2]}, Downloads: {book[3]}")

    except FileNotFoundError:
        print("Error: The specified CSV file was not found.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


file_path = 'books-en.csv'
analyze_books(file_path)
