import csv

def count_expensive_books(file_path):
    total_count = 0

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=';')

            for record in csv_reader:
             
                if len(record[1]) > 30:
                    try:
                    
                        book_price = float(record[6].replace(',', '.'))
                        if book_price >= 200:
                            total_count += 1
                    except ValueError:
                        print(f"Invalid price encountered: {record[6]}")

        print("Total books meeting the criteria:", total_count)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_path = 'books-en.csv'
count_expensive_books(file_path)
