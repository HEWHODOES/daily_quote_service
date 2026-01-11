import os
import sqlite3

def get_quotes_db():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'data')
    db_path = os.path.join(data_dir, 'quotes.db')
    
    os.makedirs(data_dir, exist_ok=True)
    
    return sqlite3.connect(db_path)