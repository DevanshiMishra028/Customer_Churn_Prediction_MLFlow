# Customer Churn Prediction with MLflow (MLOps Project)

This project demonstrates an **end-to-end MLOps workflow** for a **Customer Churn Prediction** problem using **MLflow** for experiment tracking and model management.

The repository covers model development, experiment tracking, and production-ready project structure.

---

## 📌 Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their services.  
In this project, we:

- Build a churn prediction model
- Track experiments using **MLflow**
- Maintain clean version control using **Git & GitHub**
- Connect to **Dagshub** to host Mlflow on Dagshub server instead on local machine
- Embed the **champion** model into an API using **FastAPI**
- Prepare the project for deployment using **Docker**

---

## 🧱 Project Structure

```text
Customer_Churn_Prediction_MLFlow/
│
├── main.py # Model training & MLflow logging
├── requirements.txt # Project dependencies
├── Dockerfile # Docker configuration
├── .gitignore # Git ignore rules
├── .dockerignore # Docker ignore rules
│
├── model/
│ ├── init.py
│ └── load_model.py # Model loading utilities
│
├── MLOPS-pipeline_Customer_Churn_prediction.ipynb
│ # Notebook for experimentation
│
└── README.md # Project documentation
 ```

---


## ⚙️ Tech Stack

- **Python**
- **Scikit-learn**
- **MLflow**
- **Docker**
- **Git & GitHub**

---

## 📊 MLflow Usage

MLflow is used for:
- Experiment tracking
- Logging metrics and parameters
- Model versioning

Run MLflow UI locally using:
```bash
mlflow ui
```

Then open:
```text
http://localhost:5000
```

---

## 🐳 Docker Support

To build the Docker image:

```bash
docker build -t churn-prediction .
```

To run the container:
```bash
docker run -p 5000:5000 churn-prediction
```

---

## 🚀 How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/DevanshiMishra028/Customer_Churn_Prediction_MLFlow.git
cd Customer_Churn_Prediction_MLFlow
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run training
```bash
python main.py
```

---

## 📈 Future Enhancements

- CI/CD pipeline
- Cloud Deployment (AWS/ECS)
- Model monitoring & Drift Detection(Data drift & Concept drift)

---

## 👤 Author

**Devanshi Mishra**

Machine Learning | MLOps Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps!😊

---
