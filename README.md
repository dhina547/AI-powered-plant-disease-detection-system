# 🌿 Plant-AI: AI-Powered Plant Disease Detection System

Plant-AI is an intelligent web-based application that uses deep learning to detect plant diseases from leaf images. It helps farmers, researchers, and agriculturists identify plant health issues early and take preventive action — enhanced with weather-based analysis for accurate prediction.

---

## 🚀 Features

- ✅ Deep Learning model (CNN) for plant disease classification
- ✅ Weather data integration for disease risk assessment
- ✅ User-friendly web interface (Flask + Bootstrap + Jinja2)
- ✅ Real-time prediction with confidence scores
- ✅ Dockerized for easy deployment and portability
- ✅ API endpoint for external integrations

---

## 📸 How It Works

1. Upload a plant leaf image.
2. The AI model analyzes the image to detect disease.
3. Weather conditions are fetched to validate prediction.
4. Results are displayed with diagnosis and recommendations.

---

## 🧠 Tech Stack

- Python, Flask
- TensorFlow / Keras
- OpenCV, NumPy, Pandas
- Jinja2, Bootstrap
- Docker, REST API
- OpenWeatherMap API (for weather data)

---

## 🐳 Run with Docker

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/plant-ai.git
cd plant-ai

# Step 2: Build the Docker image
docker build -t plant-ai .

# Step 3: Run the container
docker run -p 5000:5000 plant-ai
