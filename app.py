from flask import Flask, request, jsonify
import parse_resume  # Import your parsing function

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    data = request.json
    resume_text = data.get('resume', '')
    parsed_resume = parse_resume.parse_resume(resume_text)
    return jsonify(parsed_resume)

if __name__ == '__main__':
    app.run(debug=True)
