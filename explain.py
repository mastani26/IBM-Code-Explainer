from flask_cors import CORS
from flask import Flask, request, jsonify
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.credentials import Credentials

# --- IBM watsonx credentials ---
api_key = "X7bpf2_v-CPYlhYsGcYa7_JRGUbKXXp12ZbqhbL_gjSl"
project_id = "0382c4b8-5319-4424-8756-61bd6484fcb0"
region = "us-south"  # or your region

credentials = Credentials(
    api_key=api_key,
    url="https://us-south.ml.cloud.ibm.com"
)

model = ModelInference(
    model_id="ibm/granite-20b-code-instruct",
    credentials=credentials,
    project_id=project_id,
    params={
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 500
    }
)

def explain_code(code_snippet):
    prompt = (
        "You are a helpful AI code explainer.\n"
        "Please explain the following code snippet clearly in simple paragraph form, without referring to line numbers or writing explicit steps. "
        "Make it sound like a smooth, easy-to-read explanation for a beginner.\n\n"
        f"Code snippet:\n{code_snippet}\n\n"
        "Explanation:"
    )
    response = model.generate_text(prompt=prompt)
    return response

# --- Flask app ---
app = Flask(__name__)
CORS(app)

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()   # ✅ Corrected line
    code_snippet = data.get("code", "")
    explanation = explain_code(code_snippet)
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(debug=True)
