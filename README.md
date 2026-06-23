# 🏠 House Price Prediction using Machine Learning

## Project Overview

This project focuses on building a Machine Learning regression model that predicts house prices using two important property features:

- Square Footage
- Number of Bedrooms

The model learns the relationship between these structural characteristics and house prices, then predicts property values for unseen data.

---

## Objective

The main objective of this project is to create a predictive model capable of estimating house prices based on core housing attributes while demonstrating the complete machine learning workflow:

- Data generation
- Data preprocessing
- Model training
- Model evaluation
- Data visualization

---

## Dataset

This project uses a **synthetically generated realistic real estate dataset** designed to simulate practical housing market trends.

### Features Used

| Feature | Description |
|-----------|-------------|
| `Square_Footage` | Continuous numerical value ranging from 800–4000 sq ft |
| `Bedrooms` | Number of bedrooms ranging from 1–4 |

### Target Variable

| Variable | Description |
|-----------|-------------|
| `Actual_Price` | Estimated property value generated using feature relationships and realistic market variations |

---

## Technologies & Libraries Used

### Data Manipulation
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
  - `LinearRegression`
  - `train_test_split`

### Model Evaluation
- `mean_absolute_error`
- `root_mean_squared_error`

### Data Visualization
- Matplotlib

---

## Project Workflow

### 1. Data Generation
A synthetic housing dataset is created using randomized but realistic relationships between house size, bedroom count, and property prices.

### 2. Data Splitting
The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

This helps evaluate model performance on unseen data.

### 3. Model Training
A **Linear Regression** algorithm is used to learn the relationship between:

- Property size
- Bedroom count

and the corresponding house price.

### 4. Model Evaluation

Performance metrics used:

**Mean Absolute Error (MAE)**  
Measures the average prediction error.

**Root Mean Squared Error (RMSE)**  
Measures prediction accuracy while giving larger penalties to bigger errors.

### 5. Data Visualization

The project visualizes:

- Actual house prices
- Predicted house prices
- A 45° reference line

This graphical representation helps assess how closely predictions align with real values.

---

## Expected Output

The model predicts house prices with a strong linear relationship between actual and predicted values, indicating good performance.

---

## Future Improvements

Possible enhancements include:

- Adding more housing features such as:
  - Location
  - Number of bathrooms
  - Property age
  - Garage availability
  - Nearby facilities

- Trying advanced regression models:
  - Random Forest Regression
  - Decision Trees
  - Gradient Boosting

- Training on real-world housing datasets

---

## Conclusion

This project demonstrates a complete end-to-end machine learning workflow for regression problems. It provides practical experience in generating datasets, training models, evaluating performance, and visualizing predictions.

---

⭐ If you found this project useful, feel free to star the repository.
