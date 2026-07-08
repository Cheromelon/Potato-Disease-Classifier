# Potato Disease Classification using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00.svg)](https://www.tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)

An end-to-end deep learning web application for classifying potato leaf diseases using Convolutional Neural Networks (CNNs). The project provides a complete machine learning pipeline—from model training to deployment through a FastAPI backend and an interactive web interface.

The model classifies potato leaf images into one of the following categories:

- Healthy
- Early Blight
- Late Blight

The application allows users to upload a potato leaf image through a web interface and receive the predicted disease along with the model's confidence score in real time.

---

# Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Training Pipeline](#model-training-pipeline)
- [Model Architecture](#model-architecture)
- [Performance](#performance)
- [Application Workflow](#application-workflow)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Future Improvements](#future-improvements)
- [Limitations](#limitations)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

---

# Project Overview

Potato is one of the world's most important food crops. Diseases such as **Early Blight** and **Late Blight** can significantly reduce crop yield if they are not detected at an early stage.

This project aims to automate disease identification using Deep Learning. A Convolutional Neural Network was trained on the PlantVillage dataset to classify potato leaf diseases. The trained model is then deployed behind a FastAPI REST API and connected to a lightweight frontend built using HTML, CSS, and JavaScript.

The project demonstrates the complete machine learning workflow including:

- Dataset preprocessing
- Model development
- Training and evaluation
- Saving trained models
- Backend API development
- Frontend integration
- Model inference
- Deployment-ready project structure

---

# Features

- Deep Learning based potato leaf disease classification
- Image upload and preview
- FastAPI REST API for prediction
- TensorFlow/Keras inference
- Confidence score for every prediction
- Simple and responsive frontend
- Clean project structure
- Deployment-ready backend
- Easily extendable to additional plant diseases

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| Image Processing | NumPy, Pillow |
| Backend | FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git, GitHub |
| Development | Jupyter Notebook, VS Code |

---

# Project Structure

```text
potato-disease-classification/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── __pycache__/
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
│   ├── training.ipynb
│   └── PlantVillage/
│
├── README.md
└── .gitignore
```

---

# Dataset

The model was trained using the **PlantVillage** dataset.

The dataset contains labeled potato leaf images belonging to three categories:

| Class | Description |
|--------|-------------|
| Healthy | Healthy potato leaf |
| Early Blight | Potato leaf infected with Early Blight |
| Late Blight | Potato leaf infected with Late Blight |

The PlantVillage dataset provides images captured under controlled conditions with clean backgrounds, making it well suited for supervised image classification tasks.

The dataset directory is excluded from this repository using `.gitignore` because of its large size.

---

# Dataset Preprocessing

Before training, the dataset undergoes several preprocessing steps.

- Images resized to **256 × 256**
- Pixel normalization using `Rescaling(1/255)`
- Data augmentation
    - Random horizontal flip
    - Random vertical flip
    - Random rotation
- Dataset caching
- Prefetching for faster training
- Train, Validation and Test split

These preprocessing steps improve training efficiency while helping the model generalize better on unseen images.

---

# Data Augmentation

The following augmentation techniques were used during training:

- Random Horizontal Flip
- Random Vertical Flip
- Random Rotation

Data augmentation helps reduce overfitting by exposing the model to multiple transformed versions of the same image.

---
# Model Architecture

Two different approaches were explored during the development of this project:

1. A custom Convolutional Neural Network (CNN)
2. Transfer Learning using ResNet50

Although both models were trained and evaluated, the custom CNN model was selected for deployment due to its lightweight architecture, good performance, and faster inference.

The deployed model is stored in:

```text
models/1.keras
```

---

# Custom CNN Architecture

The deployed CNN consists of the following layers:

| Layer | Output |
|--------|---------|
| Input Image | 256 × 256 × 3 |
| Resizing | 256 × 256 |
| Rescaling | Pixel values normalized to [0,1] |
| Data Augmentation | Random Flip & Rotation |
| Conv2D (32 filters) + ReLU | Feature Extraction |
| MaxPooling2D | Downsampling |
| Conv2D (64 filters) + ReLU | Feature Extraction |
| MaxPooling2D | Downsampling |
| Conv2D (64 filters) + ReLU | Feature Extraction |
| MaxPooling2D | Downsampling |
| Flatten | Converts feature maps into a vector |
| Dense (64) + ReLU | Fully Connected Layer |
| Dense (3) + Softmax | Disease Classification |

The model predicts one of the following classes:

- Healthy
- Early Blight
- Late Blight

---

# Training Configuration

| Parameter | Value |
|-----------|-------|
| Framework | TensorFlow / Keras |
| Image Size | 256 × 256 |
| Batch Size | 32 |
| Loss Function | Sparse Categorical Crossentropy |
| Optimizer | Adam |
| Output Activation | Softmax |
| Epochs | 50 |
| Number of Classes | 3 |

---

# Training Pipeline

The complete training workflow is shown below.

```text
PlantVillage Dataset
          │
          ▼
Load Dataset
          │
          ▼
Train / Validation / Test Split
          │
          ▼
Resize Images
          │
          ▼
Rescale Pixel Values
          │
          ▼
Data Augmentation
          │
          ▼
CNN Training
          │
          ▼
Model Evaluation
          │
          ▼
Save Trained Model (.keras)
          │
          ▼
FastAPI Inference API
          │
          ▼
Frontend Prediction
```

---

# Model Performance

The trained model achieved excellent performance on the PlantVillage test dataset.

| Metric | Value |
|--------|--------|
| Test Accuracy | ~98% |
| Number of Classes | 3 |
| Model Format | Keras (.keras) |

The model successfully classifies healthy potato leaves along with Early Blight and Late Blight under controlled conditions.

---

# Prediction Pipeline

Once the backend receives an uploaded image, the following operations are performed.

```text
Uploaded Image
        │
        ▼
Read Image using Pillow
        │
        ▼
Convert to NumPy Array
        │
        ▼
Expand Batch Dimension
        │
        ▼
CNN Prediction
        │
        ▼
Softmax Probabilities
        │
        ▼
Predicted Class
        │
        ▼
Confidence Score
        │
        ▼
JSON Response
```

Example response:

```json
{
    "class": "Late Blight",
    "confidence": 99.42
}
```

---

# Evaluation on Real-World Images

Although the model achieves approximately **98% accuracy** on the PlantVillage test dataset, additional testing was performed using real-world potato leaf images collected from Google.

The following observations were made:

- The model performs reliably on images containing a single potato leaf.
- Performance decreases when multiple overlapping leaves are present.
- Complex backgrounds such as soil, vegetation, or shadows can affect predictions.
- Cropping a single infected leaf from a complex image significantly improves prediction accuracy.

These observations highlight the difference between controlled datasets and real-world agricultural environments.

---

# Current Limitations

The model was trained exclusively on the PlantVillage dataset.

PlantVillage images generally contain:

- Single leaf
- Plain background
- Controlled lighting
- Minimal noise

Real-world field images often contain:

- Multiple leaves
- Different camera angles
- Natural lighting
- Soil background
- Occlusions
- Shadows

Consequently, prediction accuracy may decrease for images captured in natural farming environments.

For best results, users are encouraged to upload a clear image containing a single potato leaf.

---

# Sample Predictions

The following section can be updated with screenshots after deployment.

| Input Image | Prediction | Confidence |
|-------------|------------|------------|
| *(Insert Image)* | Healthy | 99.83% |
| *(Insert Image)* | Early Blight | 98.47% |
| *(Insert Image)* | Late Blight | 99.12% |

---

# Screenshots

## Home Page

> Insert screenshot of the application's home page here.

---

## Prediction Page

> Insert screenshot showing image upload and prediction.

---

## API Documentation

> Insert screenshot of FastAPI Swagger documentation.

---

# Demonstration

A short demonstration video or GIF illustrating the application workflow can be added here.

Example workflow:

1. Upload potato leaf image.
2. Preview image.
3. Click **Predict**.
4. Receive predicted disease and confidence score.

# Installation

## Clone the Repository

```bash
git clone https://github.com/<your-github-username>/potato-disease-classification.git
```

Navigate into the project directory.

```bash
cd potato-disease-classification
```

---

# Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# Install Dependencies

Install all required Python packages.

```bash
pip install -r backend/requirements.txt
```

If a `requirements.txt` file is not available, install the required libraries manually.

```bash
pip install tensorflow
pip install fastapi
pip install uvicorn
pip install numpy
pip install pillow
pip install python-multipart
```

---

# Running the Backend

Navigate to the project root.

```bash
cd potato-disease-classification
```

Start the FastAPI server.

```bash
uvicorn backend.main:app --reload
```

If the server starts successfully, you should see:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

The backend will now be available at

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

Both interfaces allow users to test the API directly from the browser.

---

# Running the Frontend

The frontend is a static web application.

Open the **frontend** directory in Visual Studio Code.

Run **Live Server**.

The application will open in your browser, usually at:

```
http://127.0.0.1:5500
```

The frontend communicates with the FastAPI backend through HTTP requests.

---

# Backend Endpoints

## Health Check

**GET**

```
/ping
```

Response

```json
"hello,there"
```

---

## Disease Prediction

**POST**

```
/predict
```

Request Type

```
multipart/form-data
```

Request Body

| Parameter | Type | Description |
|-----------|------|-------------|
| file | Image | Potato Leaf Image |

Example Response

```json
{
    "class": "Late Blight",
    "confidence": 99.42
}
```

---

# API Workflow

```text
Frontend
     │
     ▼
Upload Image
     │
     ▼
FastAPI Backend
     │
     ▼
Image Preprocessing
     │
     ▼
TensorFlow Model
     │
     ▼
Prediction
     │
     ▼
JSON Response
     │
     ▼
Frontend Displays Result
```

---

# Frontend Overview

The frontend was intentionally kept lightweight to demonstrate complete frontend-backend integration.

### Components

- HTML
- CSS
- JavaScript

### Features

- Image Upload
- Image Preview
- Prediction Button
- Disease Prediction
- Confidence Score
- Error Handling

---

# Backend Overview

The backend is implemented using **FastAPI**.

Responsibilities include:

- Receiving uploaded images
- Reading images using Pillow
- Converting images to NumPy arrays
- Passing images through the trained TensorFlow model
- Returning predictions as JSON

The trained model is loaded only once during application startup, ensuring low inference latency.

---

# Model Inference Pipeline

```text
User Uploads Image
          │
          ▼
Read using Pillow
          │
          ▼
Convert to NumPy Array
          │
          ▼
Expand Batch Dimension
          │
          ▼
Model.predict()
          │
          ▼
Softmax Probabilities
          │
          ▼
Argmax
          │
          ▼
Disease Class
          │
          ▼
Confidence Score
```

---

# Deployment

The project is designed with deployment in mind.

The architecture separates the frontend and backend, allowing them to be deployed independently.

### Local Development

```
Frontend  → Live Server
Backend   → FastAPI
Model     → TensorFlow
```

### Production Deployment

```
Frontend
    │
    ▼
Vercel / Static Hosting

        │
        ▼

FastAPI Backend

        │
        ▼

Docker Container

        │
        ▼

AWS EC2
```

This architecture allows the frontend and backend to scale independently.

---

# Repository Contents

| Folder | Description |
|---------|-------------|
| backend | FastAPI application |
| frontend | Web interface |
| models | Trained CNN model |
| training | Model development notebook |
| README.md | Project documentation |

---

# Requirements

The project was developed using the following software versions.

| Software | Version |
|----------|---------|
| Python | 3.11 |
| TensorFlow | 2.x |
| FastAPI | Latest |
| Uvicorn | Latest |
| NumPy | Latest |
| Pillow | Latest |

Newer versions should also work with minimal or no modification.
