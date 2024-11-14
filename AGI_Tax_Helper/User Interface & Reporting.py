from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/deductions', methods=['POST'])
def get_deductions():
    data = request.get_json()
    deductions = calculate_deductions(data['income'], data['expenses'])
    return jsonify(deductions=deductions)

if __name__ == '__main__':
    app.run(debug=True)