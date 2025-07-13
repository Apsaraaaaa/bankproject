import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    try:
        data = []

        # Open and read CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        # Write to JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
csv_file = 'students.csv'
json_file = 'students.json'

csv_to_json(csv_file, json_file)