from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
gradio_client = Client("https://pranavkd-chikkugptwa.hf.space/")

@app.route('/predict', methods=['GET'])
def predict():
    prompt = request.args.get('prompt', '')
    
    if prompt:
        result = gradio_client.predict(prompt, api_name="/predict")
        return jsonify(result)
    else:
        return jsonify({"error": "Please provide a prompt."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
