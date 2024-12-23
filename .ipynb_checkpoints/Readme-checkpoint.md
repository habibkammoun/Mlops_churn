# MLOps Project: Customer Churn Prediction

This repository contains the complete implementation of an MLOps pipeline for **Customer Churn Prediction**, offering detailed churn analysis, lifestyle-based insights, and behavior-driven detection. The project adheres to industry-standard MLOps practices, ensuring efficient development, deployment, and monitoring for reliable and scalable outcomes.

---

## Why Customer Churn Prediction?

Customer churn is a critical issue for subscription-based businesses, directly impacting revenue and profitability. Retaining existing customers is more cost-effective than acquiring new ones, making it essential to understand the drivers of churn. This project uses a dataset that provides insights into customer demographics, usage behavior, subscription details, and engagement levels. By leveraging this data, businesses can:

- Identify at-risk customers.
- Enhance retention strategies.
- Foster long-term customer loyalty.

---

## Dataset Overview

The dataset used in this project is designed to help identify and analyze factors contributing to customer churn. Below is a description of the key features:

1. **Age:** The age of the customer.
2. **Gender:** The gender of the customer (e.g., Male, Female).
3. **Usage Frequency:** The frequency with which the customer uses the service.
4. **Support Calls:** The number of support calls made by the customer.
5. **Payment Delay:** The number of days the customer delayed payment.
6. **Subscription Type:** The type of subscription plan the customer is on (e.g., Basic, Standard, Premium).
7. **Contract Length:** The duration of the subscription contract (e.g., Monthly, Quarterly, Annual).
8. **Total Spend:** The total amount spent by the customer during their tenure.
9. **Last Interaction:** The number of days since the customer’s last interaction with the service.
10. **Churn:** A binary variable indicating if the customer has churned (1 for churn, 0 for retention).
11. **Tenure Group:** The tenure of the customer, categorized into ranges (e.g., 1–12 months, 25–36 months).

---

## Key Features

### 1. **Data Workflow**
   - **Data Handling:** Comprehensive CSV datasets with demographic, behavioral, and subscription details.
   - **EDA & Preprocessing:** Performed exploratory data analysis (EDA) and applied robust preprocessing techniques to clean and standardize the data.
   - **Modeling:** Built and trained machine learning models using **MLflow** for experiment tracking and hyperparameter tuning.

### 2. **Version Control**
   - Managed datasets, pipelines, and models with **DVC (Data Version Control)** for reproducibility and traceability.

### 3. **Application Development**
   - Developed a **FastAPI backend** to expose the churn prediction functionality as an API.
   - Built a user-friendly **Streamlit frontend** for intuitive interaction.

### 4. **Testing**
   - Employed **Deepchecks** to validate data quality and model performance.

### 5. **Deployment**
   - Deployed on **Render** with Dockerized services for reliability and scalability.

### 6. **CI/CD Automation**
   - Automated build, test, and deploy processes using **Jenkins**.

### 7. **Monitoring**
   - Integrated **Arize** for end-to-end monitoring of model performance and data drift detection.

---

## Architecture

The MLOps pipeline is designed with modular components:

1. **Data Management**
   - Raw data ingestion and preprocessing pipelines.
   - Versioning with **DVC** for datasets and trained models.

2. **Modeling**
   - Experiment tracking and model registry using **MLflow**.

3. **Application Development**
   - **FastAPI** backend for API development.
   - **Streamlit** frontend for user interaction.

4. **Deployment**
   - Hosted on **Render** for scalability.
   - Containerized services using Docker.

5. **Testing & Validation**
   - Quality assurance with **Deepchecks**.

6. **CI/CD Pipeline**
   - Continuous integration, training, and deployment with **Jenkins**.

7. **Monitoring**
   - **Arize** for monitoring predictions, detecting anomalies, and addressing data drift.

---

## Technologies Used

- **Data Management:** DVC  
- **Model Tracking & Experimentation:** MLflow  
- **Testing:** Deepchecks  
- **Deployment:** Render, Docker  
- **CI/CD:** Jenkins  
- **Monitoring:** Arize  
- **Frontend:** Streamlit  
- **Backend:** FastAPI  

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rami4real/Mlops_churn.git
   cd Mlops_churn
   ```

2. Initialize DVC:
   ```bash
   dvc init
   ```

3. Train the model and track experiments with MLflow:
   ```bash
   mlflow run .
   ```

4. Deploy the application:
   - Configure the `Dockerfile` for deployment on Render.
   - Push the repository to trigger deployment.

5. Automate CI/CD with Jenkins:
   - Use the provided `Jenkinsfile`.
   - Configure the pipeline to automate build, test, and deploy steps.

6. Monitor the model:
   - Integrate Arize for real-time performance tracking.

---

## Contributions

This project was collaboratively developed by:

- **Ahmed Rami Belguith**  
- **Mohamed Hbib Kammoun**  
- **Azza Shell**  

Feel free to fork the repository, report issues, or contribute new features by opening pull requests. Your contributions are welcome!

---

Thank you for exploring the **Customer Churn Prediction MLOps Pipeline**! 🚀

