import xml.etree.ElementTree as ElementTree

def extract_currency_details(file_path):
    try:
        # Load and parse the XML file
        xml_tree = ElementTree.parse(file_path)
        root_element = xml_tree.getroot()

        currency_list = []

        # Loop through each 'Valute' element
        for valute in root_element.findall('Valute'):
            num_code = int(valute.find('NumCode').text) if valute.find('NumCode') is not None else None
            char_code = valute.find('CharCode').text if valute.find('CharCode') is not None else None
            nominal_value = int(valute.find('Nominal').text) if valute.find('Nominal') is not None else None
            currency_name = valute.find('Name').text if valute.find('Name') is not None else None
            exchange_value = float(valute.find('Value').text.replace(',', '.')) if valute.find('Value') is not None else None
            unit_rate = float(valute.find('VunitRate').text.replace(',', '.')) if valute.find('VunitRate') is not None else None

            currency_list.append({
                'Numeric Code': num_code,
                'Character Code': char_code,
                'Nominal': nominal_value,
                'Currency Name': currency_name,
                'Exchange Value': exchange_value,
                'Unit Rate': unit_rate
            })

        return currency_list

    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ElementTree.ParseError:
        print("Error: Failed to parse the XML file.")
        return []
    except Exception as error:
        print(f"Unexpected error: {error}")
        return []

# Example usage
file_path = 'currency.xml'
currency_details = extract_currency_details(file_path)

for currency in currency_details:
    print(currency)
