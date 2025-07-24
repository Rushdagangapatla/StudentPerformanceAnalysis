# Student Performance Predictor

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#import kagglehub


# 1. Load dataset
url = "http://bit.ly/w-data"  # Dataset: Hours vs Scores
#path = kagglehub.dataset_download("himanshunakrani/student-study-hours")
df = pd.read_csv(url)
print("📊 First 5 rows of the data:\n", df.head())

# 2. Visualize data
plt.scatter(df['Hours'], df['Scores'], color='blue')
plt.title('Hours Studied vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# 3. Prepare data
X = df[['Hours']]  # Independent variable
y = df['Scores']   # Dependent variable

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Compare predictions
result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\n📈 Predictions vs Actual:\n", result)

# 8. Evaluate model
mse = mean_squared_error(y_test, y_pred)
print("\n📉 Mean Squared Error:", mse)

# 9. Predict custom input
hours = 9.25
predicted_score = model.predict([[hours]])
print(f"\n📚 A student studying {hours} hours is expected to score {predicted_score[0]:.2f} marks.")

# 10. Plot regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')  # Regression line
plt.title('Regression Line (Hours vs Scores)')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.grid(True)
plt.show()
