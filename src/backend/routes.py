from flask import Blueprint, render_template, request, jsonify

api = Blueprint('api', __name__)

# Route for serving the HTML
@api.route("/")
def index():
    return render_template("index.html")

# Route for handling a POST request from the frontend
@api.route("/process", methods=["POST"])
def process_data():
    data = request.json
    response = {"message": f"Received: {data}"}
    return jsonify(response)
