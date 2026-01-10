from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON okuma
def read_json(filename='products.json'):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception:
        return []

# CSV okuma
def read_csv(filename='products.csv'):
    products = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products

# SQLite okuma
def read_sqlite(filename='products.db'):
    products = []
    try:
        conn = sqlite3.connect(filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    # Kaynağa göre veri çek
    if source == "json":
        products_list = read_json()
    elif source == "csv":
        products_list = read_csv()
    elif source == "sql":
        products_list = read_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # ID filtreleme
    if id_param:
        try:
            id_value = int(id_param)
            filtered = [p for p in products_list if p["id"] == id_value]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=[])
            products_list = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid ID", products=[])

    return render_template('product_display.html', products=products_list, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
