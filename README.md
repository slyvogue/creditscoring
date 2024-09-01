# Credit Score Prediction using Machine Learning

## Overview
This project presents a machine learning approach to assigning credit scores. The focus is on constructing a new credit scoring model that enhances the accuracy of creditworthiness assessment. The project evaluates and compares traditional and modern machine learning techniques, ultimately showcasing how machine learning can replace conventional credit scoring methods.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Ethical Considerations](#ethical-considerations)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Structure
The project is divided into the following chapters:
1. *Introduction*: Provides background, motivation, problem statement, and objectives of the study.
2. *Literature Review*: Discusses traditional credit scoring methods and the application of machine learning in credit scoring.
3. *Methodology*: Details data collection, preprocessing, model development, and evaluation techniques.
4. *Design and Implementation*: Covers data structure, model building, and performance metrics.
5. *Results and Analysis*: Analyzes the results obtained from the machine learning models and compares them with traditional models.
6. *Evaluation and Conclusion*: Summarizes the findings, discusses challenges, and suggests areas for future work.

## Key Features
- *Data Preprocessing*: Handling missing values, outlier detection, normalization, and feature engineering.
- *Model Development*: Implementation of various models including Logistic Regression, Decision Trees, Random Forest, and XGBoost.
- *Model Evaluation*: Performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- *Web Application*: A user-friendly interface for real-time credit score prediction using Streamlit.
- *Ethical Considerations*: Addressing bias and fairness in credit scoring models.

## Technologies Used
- *Programming Language*: Python
- *Libraries*: Scikit-learn, XGBoost, Streamlit
- *Tools*: Jupyter Notebook, Pandas, NumPy, Matplotlib

## Installation
1. Clone the repository: git clone https://github.com/slyvogue/creditscoring.git

  
   
2. Navigate to the project directory

   
3. Install the required packages: pip install -r requirements.txt
 
   
   

## Usage
1. Prepare your dataset and place it in the directory.
2. Run the Jupyter Notebook to train and evaluate the models.
3. Launch the Streamlit application for real-time credit score prediction: streamlit run app.py
   
   

## Model Performance
- *Best Model*: XGBoost
  - *Accuracy*: 81.6%
  - *Precision*: 81.7%
  - *Recall*: 81.6%
  - *F1-Score*: 81.5%

## Ethical Considerations
The project emphasizes the importance of fairness in credit scoring models. Techniques such as balanced datasets and fairness-aware algorithms are employed to minimize bias.

## Future Work
- *Feature Engineering*: Incorporate additional financial and behavioral indicators.
- *Algorithmic Refinement*: Further hyperparameter tuning and model optimization.
- *Real-Time Data Integration*: Enhance the model with live data updates.

## Acknowledgements
I would like to express my gratitude to my supervisor, Dr. Glen Hopkinson, for his guidance and support throughout this project.

## Contact
For any inquiries or contributions, please contact Sylvester Eric Okogbe at [slyvogue@gmail.com].
