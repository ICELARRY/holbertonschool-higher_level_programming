from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# JSON okuma
def read_json(filename='products.json'):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception as e:
        return []

# CSV okuma
def read_csv(filename='products.csv'):
    products = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV verilerini uygun tipe çevir
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source == "json":
        products_list = read_json()
    elif source == "csv":
        products_list = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # id filtreleme
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
