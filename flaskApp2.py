from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC", "lat": 38.89, "lon": -77.01}
]

next_id = 4


@app.route("/")
def index():
    return ("""<h1>Hello! Welcome to my application. It provides information about FIU's several campuses.</h1>
            <p> Try these endpoints: </p>
            <ul>
                <li><a href="/hello">/api/hello</a></li>
                <li><a href="/data">/api/data</a></li>
                <li><a href="/api/health">/api/health</a></li>
                <li><a href="/api/items">/api/items</a></li>
                <li><a href="/api/items/1">/api/items/1</a></li>
            </ul>
            """)

@app.route("/hello")
def hello():
    return jsonify({"message": "Welcome to my FIU Campus API!"}), 200


@app.route("/data", methods=["GET", "POST"])
def manage_data():
    if request.method == "POST":
        # Logic to add a new item via POST
        new_entry = request.get_json()
        DATA.append(new_entry)
        return jsonify({"message": "Data added successfully", "added": new_entry}), 201

    return jsonify({"campuses": DATA}), 200

@app.route("/api/health")
def health():
    return jsonify({"message": "OK"}), 200


@app.route("/api/items")
def items():
    return jsonify({"items": DATA}), 200

@app.route("/api/items/<int:id>")
def get_item_by_id(id):
    for i in DATA:
        if i["id"] == id:
            return jsonify(i), 200
    return jsonify({"message": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)