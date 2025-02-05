import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 1: Generate Synthetic Data
# Columns: Order Size, Distance to Supplier, Historical Delay, Supplier Rating
np.random.seed(42)
data = pd.DataFrame({
    'Order_Size': np.random.randint(1, 100, 500),
    'Distance_to_Supplier': np.random.randint(10, 500, 500),
    'Historical_Delay': np.random.uniform(0, 5, 500),  # Average historical delays
    'Supplier_Rating': np.random.uniform(3, 5, 500),   # Rating from 3.0 to 5.0
    'Lead_Time': np.random.uniform(2, 10, 500) + np.random.uniform(-2, 2, 500),  # Simulated Lead Time
})

# Step 2: Prepare Features and Target
X = data[['Order_Size', 'Distance_to_Supplier', 'Historical_Delay', 'Supplier_Rating']]
y = data['Lead_Time']

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict on Test Set
y_pred = model.predict(X_test)

# Step 6: Evaluate Model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")

# Step 7: Predict Lead Time for a New Order
new_order = pd.DataFrame({
    'Order_Size': [50],
    'Distance_to_Supplier': [150],
    'Historical_Delay': [2.5],
    'Supplier_Rating': [4.5],
})
predicted_lead_time = model.predict(new_order)
print(f"Predicted Lead Time for New Order: {predicted_lead_time[0]:.2f} days")
