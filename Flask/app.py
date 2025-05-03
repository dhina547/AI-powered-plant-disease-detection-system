import os
from flask import Flask, render_template, jsonify, request
from markupsafe import Markup
from model import predict_image
import google.generativeai as genai

# ✅ Define Flask App (Must be at the top before any @app.route)
app = Flask(__name__)

# ✅ Set Google Gemini API Key directly in the code (Replace with your actual API key)
GEMINI_API_KEY = "A000000000000"  # ⬅️ Replace this with your actual Gemini API key

# ✅ Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def fetch_disease_insights(disease_name):
    """Fetch additional disease details using Gemini AI."""
    try:
        prompt = f"""
        Provide detailed information about the plant disease "{disease_name}". Cover the following aspects:
        
        1. **Cause of the Disease** – What are the primary factors leading to this disease?
        2. **Symptoms** – What are the visible and internal symptoms in affected plants?
        3. **Spread Mechanism** – How does this disease spread among plants?
        4. **Prevention and Control** – What are the best practices to prevent and control this disease?
        5. **Impact on Crops** – How does this disease affect crop yield and quality?
        
        Provide scientific insights, latest research findings, and practical solutions for farmers.
        """

        response = model.generate_content(prompt)

        # Debugging: Print response to check if API is working
        print("🌍 Gemini API Raw Response:", response)

        return response.text.replace("\n", "<br>") if response.text else "⚠️ No insights available."

    except Exception as e:
        print("❌ Gemini API Error:", str(e))
        return "⚠️ Error retrieving AI insights."


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handles file upload, predicts the disease, and fetches information from Gemini AI."""
    if 'file' not in request.files:
        return render_template('index.html', status=400, res="No file uploaded")

    try:
        file = request.files['file']
        img = file.read()

        # Predict disease name using the model
        disease_name = predict_image(img)
        print("🔍 Predicted Disease:", disease_name)

        # Fetch AI-generated disease insights
        ai_insights = fetch_disease_insights(disease_name)
        print("📝 Gemini AI Response:", ai_insights)

        return render_template(
            'display.html',
            status=200,
            result=disease_name,
            ai_info=Markup(ai_insights)  # Ensures HTML formatting in UI
        )

    except Exception as e:
        print("❌ Error:", str(e))
        return render_template('index.html', status=500, res=f"Internal Server Error: {str(e)}")


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API Endpoint for disease prediction & AI-generated insights."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        file = request.files['file']
        img = file.read()

        # Get the disease prediction from the model
        disease_name = predict_image(img)
        print("🔍 Predicted Disease:", disease_name)

        # Fetch AI insights from Gemini
        ai_insights = fetch_disease_insights(disease_name)

        return jsonify({
            "disease": disease_name,
            "ai_insights": ai_insights
        }), 200

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
