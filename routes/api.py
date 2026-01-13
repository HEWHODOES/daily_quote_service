
from flask import Blueprint, jsonify
from scripts.db_connection import get_quotes_db

api_bp = Blueprint('api', __name__, url_prefix='/api')

#route for fetching categories

@api_bp.route('/categories')
def categories():

    conn = get_quotes_db()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT category_name FROM categories")
    categories = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({'categories': categories})

