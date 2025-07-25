# 🎓 Student  Performance  Analysis

A Machine Learning project to analyze and predict student exam scores based on study hours using Python, pandas, matplotlib, and scikit-learn.

## 📋 Table of Contents
- [Overview] (#overview)
- [Dataset] (#dataset)
- [Project Structure] (#project-structure)
- [Installation & Setup] (#installation--setup)
- [Usage] (#usage)
- [Results] (#results)
- [Evaluation] (#evaluation)
- [Customize Prediction] (#customize-prediction)
- [License] (#license)

---

## 🧠 Overview
This repo implements a simple linear regression model to predict student scores based on hours studied. It covers:
- Data visualization (scatter plot)
- Train-test split
- Model training
- Predicting and evaluating using Mean Squared Error
- Custom prediction example (e.g., 9.25 study hours)

---

## 📚 Dataset
A two-column CSV hosted online:
- `Hours` – Number of study hours.
- `Scores` – Corresponding exam score.
  
Dataset URL: `http://bit.ly/w-data`

---

## 📂 Project Structure
 student_performance_predictor.py # Main script

---

## ⚙️ Installation & Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/Rushdagangapatla/StudentPerformanceAnalysis.git
   cd StudentPerformanceAnalysis
2.Create a virtual environment (optional but recommended):
          
          python3 -m venv venv
       source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    
3.Install dependencies:

        pip install pandas matplotlib scikit-learn


RUN

    python student_performance_predictor.py

This is how output looks:

-->Load and display the first 5 rows of data

-->Show a scatter plot (Hours vs Score)

-->Train/test split and fit a linear regression model

-->Predict on the test set and display actual vs predicted scores

-->Print the Mean Squared Error

-->Predict score for a custom input (9.25 hours)

-->Display the regression line plot

📈 Results


A table comparing actual vs predicted scores on the test set

MSE value output in the terminal

Two visualizations: scatter plot & regression line

🧪 Evaluation


The model is evaluated using:
mean_squared_error(y_test, y_pred)

Lower MSE values indicate a better fit.

✏️ Customize Prediction


You can change the custom input hours like this:
    
    hours = 7.5
    predicted_score = model.predict([[hours]])
    print(f"Expected score for {hours} study hours is {predicted_score[0]:.2f}")

📝 License

This project is open source under the MIT License.

Google CoLab link:
          
    https://colab.research.google.com/drive/1GO3LalagUI6-ZK4HYTMpLpynRXEEj1Rr?usp=sharing

    
Enjoy your journey into Machine Learning with this student performance predictor!

