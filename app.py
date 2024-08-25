from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        }), 200
    
    if request.method == 'POST':
        try:
            data = request.json.get('data', [])
            if not isinstance(data, list):
                raise ValueError("Invalid input format. 'data' should be a list.")

            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]

            highest_lowercase_alphabet = [max([char for char in alphabets if char.islower()])] if any(char.islower() for char in alphabets) else []

            response = {
                "is_success": True,
                "user_id": "Tanniru_Leela_Sai_Ram_21BCE9789",
                "email": "sai.21bce9789@vitapstudent.ac.in",
                "roll_number": "21BCE9789",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet
            }

            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({
                "is_success": False,
                "error": str(e)
            }), 400

if __name__ == '__main__':
    app.run(debug=True)
