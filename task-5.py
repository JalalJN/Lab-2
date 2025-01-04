import pandas as pd

# Load the CSV file with appropriate delimiter and encoding
file_path = 'books-en.csv'  # Replace with the actual path to your CSV file
books_df = pd.read_csv(file_path, delimiter='\t', encoding='ISO-8859-1')

# Extract unique publishers
unique_publishers = books_df['Publisher'].dropna().unique()

# Convert to a list
unique_publishers_list = list(unique_publishers)

# Print the unique publishers
for publisher in unique_publishers_list:
    print(publisher)
