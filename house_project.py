import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.model_selection import train_test_split

# 1. Generate realistic synthetic house data to save download time
np.random.seed(42)
n_samples = 200
sq_ft = np.random.randint(800, 4000, n_samples)
bedrooms = np.random.randint(1, 5, n_samples)
prices = 50000 + (sq_ft * 150) + (bedrooms * 25000) + np.random.normal(0, 15000, n_samples)

df = pd.DataFrame(
    {"Square_Footage": sq_ft, "Bedrooms": bedrooms, "Actual_Price": prices}
)

# 2. Features and Target split
X = df[["Square_Footage", "Bedrooms"]]
y = df["Actual_Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict and Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)

print(f"--- Model Evaluation ---")
print(f"Mean Absolute Error (MAE): ${mae:.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:.2f}\n")

# 5. Build the Matplotlib Canvas
plt.figure(figsize=(8, 5))
plt.scatter(y_test, predictions, color="purple", alpha=0.7, label="Predicted Houses")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "k--",
    lw=2,
    label="Perfect Prediction Line",
)
plt.title("Actual vs Predicted House Prices")
plt.xlabel("Actual Price ($)")
plt.ylabel("Predicted Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
