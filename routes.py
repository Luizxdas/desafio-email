from flask import Blueprint, request, jsonify, render_template
from utils.response_generator import generate_response
from utils.verification import verify_and_read
from utils.classification import classify_message

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/response")
def response():
    return render_template("response.html")

@routes.route("/upload", methods=["POST"])
def upload():
    content = None

    if "text" in request.form and request.form["text"].strip():
        content = request.form["text"].strip()

    elif "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        content = verify_and_read(file)

    else:
        return jsonify({"error": "Nenhum texto ou arquivo enviado"}), 400

    try:
        classification = classify_message(content)
        # generatedResponse = generate_response(content)
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "message": content,
        "classification": classification,
        # "generatedResponse": generatedResponse
    }), 200

