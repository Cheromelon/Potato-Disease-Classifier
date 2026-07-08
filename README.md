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
