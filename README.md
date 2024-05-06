# NSL-KDD Dataset Analysis and Model Deployment
This repository contains the code and resources for analyzing the [NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd/data) dataset, a network traffic dataset designed for cybersecurity analysis and intrusion detection. The dataset has been preprocessed and analyzed using various machine learning techniques, and a model has been deployed using Flask and Docker.

## Data Preprocessing Steps
* Outlier Removal: Outliers were removed from the data using the median replacement method.
* One-Hot Encoding: Categorical variables were encoded using one-hot encoding to prepare them for modeling.
* Feature Scaling: RobustScaler was applied to scale the features to mitigate the impact of outliers.
* Dimensionality Reduction: Principal Component Analysis (PCA) was explored to reduce the dimensionality of the dataset.

##  Machine Learning Models
Several machine learning models were trained and evaluated using the preprocessed data, including:
* Random Forest Classifier
* Decision Tree Classifier
  
Model evaluation metrics were used to compare the performance of these models, and hyperparameter tuning was performed to optimize their performance.

## Model Deployment
The trained model was deployed using Flask, a lightweight web framework, and Docker, a containerization platform. This allows for easy deployment and scalability of the model in production environments.

## Repository Structure
model_training/: Jupyter notebooks used for data preprocessing, model training, and evaluation.
app.py: Flask application for serving the deployed model.
Dockerfile: Docker configuration file for containerizing the Flask application.
requirements.txt: Python dependencies required for running the Flask application.

## Usage
1. Clone the repository:
```bash
git clone https://github.com/your-username/nsl-kdd-analysis.git
cd nsl-kdd-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```
4. Access the deployed model via http://localhost:5000 in your web browser. 
