# This Project is about the Chicken Disease Classification. This project classifies chicken diseases from images using a Convolutional Neural Network (CNN). It is part of a poultry AI pipeline that automates disease detection to help farmers and poultry businesses monitor flock health efficiently.

## My Project Workflows
1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration.py (manager) in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
├── artifacts/ # DVC-managed data and model artifacts
├── src/ # Source code including data pipeline, training, etc.
├── app.py # Streamlit web application for disease prediction
├── dvc.yaml # DVC pipeline configuration
├── requirements.txt # Python dependencies
├── .env # Environment variables (AWS credentials, etc.)
├── setup.py # Project packaging file
└── README.md # Project documentation

## 🚀 Features

- End-to-end pipeline using DVC (Data Version Control)
- Custom CNN for image classification
- Trained on AWS S3-hosted dataset
- Web-based inference app built with Bootstrap
- Modular and production-ready Python structure

## 🛠️ Setup Instructions
### 1. Clone the repository

git clone https://github.com/Aaish-Developer26/chicken-disease-classification.git
cd chicken-disease-classification

### 2. Create and activate virtual environment

python -m venv chicken
source chicken/bin/activate     # On Windows: chicken\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up environment variables

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region

### 5. Reproduce the pipeline

If this is your first time setting up the project:
dvc pull               # Pulls data from S3
dvc repro              # Runs the complete pipeline

### 6. Train the model (Optional)

If you'd like to retrain the model:
python src/CnnClassifier/training.py

### 7. Launch the Frontend App

python app.py

### 8. Packaging

To make the project pip-installable (optional):
pip install -e .

### 9. 📌 TODOs and Future Work

 - Add mobile support to the Streamlit app

 - Deploy the model with FastAPI or on cloud platforms

 - Improve dataset with real-world chicken farm images

 - Introduce multi-class disease detection

   






