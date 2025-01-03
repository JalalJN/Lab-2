import random
import csv

def generate_references(file_path, num_records=20):
    try:

        formatted_references = []

    
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            rows = list(csv_reader)

         
            selected_rows = random.sample(rows, k=min(num_records, len(rows)))

           
            for row in selected_rows:
                author = row[2] if len(row) > 2 else "Author Unknown"
                title = row[1] if len(row) > 1 else "Title Unknown"
                year = row[4] if len(row) > 4 else "Year Unknown"
                reference = f"{author}. {title} ({year})"
                formatted_references.append(reference)

     
        with open('references_output.txt', mode='w') as output_file:
            for index, ref in enumerate(formatted_references, start=1):
                output_file.write(f"{index}. {ref}\n")

        print("References successfully written to 'references_output.txt'.")

    except FileNotFoundError:
        print("Error: The file specified was not found.")
    except ValueError as e:
        print(f"Error: {e}. Ensure the file contains sufficient rows.")
    except Exception as e:
        print(f"Unexpected error: {e}")


generate_references('books-en.csv')
