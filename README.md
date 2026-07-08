 Potato Disease Classification using Deep Learning

An end-to-end Deep Learning web application that classifies potato leaf diseases using TensorFlow, FastAPI, and a simple HTML/CSS/JavaScript frontend.

Live Demo: (Add after deployment)

Project Demo: (Add GIF/video here)

 Overview

Potato crops are vulnerable to diseases such as Early Blight and Late Blight, which can significantly reduce crop yield if not detected early.

This project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset to classify potato leaf images into three categories:

 Healthy
 Early Blight
 Late Blight

The trained model is exposed through a FastAPI REST API, allowing users to upload an image through a web interface and receive predictions in real time.

 Features
Image classification using TensorFlow/Keras
FastAPI backend for inference
Responsive frontend built with HTML, CSS and JavaScript
Upload and preview leaf images
Displays predicted disease and confidence score
REST API for easy integration
Ready for Docker/AWS deployment
📷 Screenshots

(Insert screenshots here)

Home Page

(Insert image)

Prediction Example

(Insert image)

 Demo

(Insert GIF or video)

🛠 Tech Stack
Machine Learning
TensorFlow
Keras
NumPy
Pillow
Backend
FastAPI
Uvicorn
Frontend
HTML5
CSS3
JavaScript
Tools
Git
GitHub
Jupyter Notebook
VS Code
📂 Project Structure
potato-disease-classification/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── 1.keras
│
├── training/
│   └── training.ipynb
│
├── README.md
└── .gitignore
🧠 Model Pipeline
Leaf Image
      │
      ▼
Resize
      │
      ▼
Rescaling
      │
      ▼
CNN
      │
      ▼
Softmax
      │
      ▼
Healthy
Early Blight
Late Blight
📊 Dataset

The model was trained using the PlantVillage dataset.

Classes:

Healthy
Early Blight
Late Blight

The dataset consists of labeled potato leaf images captured under controlled conditions.

⚙️ Model Training

Training workflow:

Data loading using TensorFlow
Data preprocessing
Image resizing
Image normalization
Data augmentation
CNN training
Model evaluation
Model export as .keras

Training notebook:

training/training.ipynb
📈 Model Performance
Test Accuracy
≈98%

The model performs well on the PlantVillage test set and correctly classifies most unseen images from the same distribution.

 Real-world Testing

The model was additionally tested on images collected from Google.

Observations:

Performs well on clear images of individual potato leaves.
Performance decreases on images containing multiple overlapping leaves or cluttered backgrounds.
This behavior is expected because the training dataset primarily contains single-leaf images captured under controlled conditions.
 Running the Project
Clone
git clone https://github.com/<username>/potato-disease-classification.git

cd potato-disease-classification
Install dependencies
pip install -r backend/requirements.txt
Start Backend
uvicorn backend.main:app --reload

Backend:

http://127.0.0.1:8000

Swagger API:

http://127.0.0.1:8000/docs
Start Frontend

Open

frontend/index.html

using Live Server.

 API
POST /predict

Uploads a potato leaf image and returns the predicted disease.

Request:

multipart/form-data

Response:

{
  "class": "Late Blight",
  "confidence": 99.42
}
⚠️ Limitations
Trained primarily on the PlantVillage dataset.
Best results are obtained with a single potato leaf in the image.
Performance may decrease on field images containing multiple leaves, complex backgrounds, or varying lighting conditions.
This project is intended for educational and research purposes and should not replace expert agricultural diagnosis.
🔮 Future Improvements
Fine-tune using real field images
Improve robustness with advanced data augmentation
Deploy backend using Docker
Deploy application on AWS
Add Grad-CAM visualization to explain model predictions
Support mobile-friendly interface
Extend to additional crop diseases
 What I Learned

Through this project, I gained practical experience with:

Convolutional Neural Networks
TensorFlow/Keras
Transfer Learning concepts
Image preprocessing
FastAPI
REST API development
Frontend–Backend integration
Model serialization and inference
Git & GitHub workflow
End-to-end Machine Learning deployment pipeline
