import json
import os
from db_connection import get_quotes_db

conn = get_quotes_db()
cursor = conn.cursor()

json_file = input("Type in the name of the file you want to include into quotes.db (filename.json): \n")

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, json_file)

try:
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for quote_data in data['quotes']:
        
        cursor.execute("""
            INSERT INTO quotes (quote, author, source)
            VALUES (?, ?, ?)
        """, (quote_data['quote'], quote_data.get('author'), quote_data.get('source')))
        
        quote_id = cursor.lastrowid
        
        for category_name in quote_data['categories']:

            cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES (?)", (category_name,))            
            cursor.execute("SELECT id FROM categories WHERE category_name = ?", (category_name,))
            category_id = cursor.fetchone()[0]
            
            cursor.execute("""
                INSERT INTO quote_categories (quote_id, category_id)
                VALUES (?, ?)
            """, (quote_id, category_id))

    conn.commit()
    print(f"{len(data['quotes'])} quotes loaded into the database!")

except FileNotFoundError:
    print(f"\nFile {json_file} not found.")
except json.JSONDecodeError:
    print(f"\nFile {json_file} is not a valid JSON file.")
except KeyError as e:
    print(f"Error: missing key in {json_file}:", e)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()