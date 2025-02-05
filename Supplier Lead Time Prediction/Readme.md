Here’s a Python example to predict supplier lead times using a regression model. This code uses Random Forest Regressor with synthetic data for demonstration.


##Code Walkthrough
- Synthetic Data Generation: The data simulates supplier-related features like order size, distance, historical delays, and ratings.
- Feature and Target Separation: X includes features, while y is the target (lead time).
- Model Training: A Random Forest Regressor predicts lead time.
- Evaluation: MAE and MSE measure model performance.
- Prediction: Predict lead time for a new hypothetical order.

## Variables Description and Sources

Order_Size
* Description: Represents the quantity of goods ordered. Larger orders may require more time to process.

Distance_to_Supplier
* Description: The distance (in kilometers or miles) from the supplier to the delivery location. Greater distances usually increase lead time.

Historical_Delay
* Description: The average delay (in days) historically recorded for a supplier. A higher delay indicates an unreliable supplier.

Supplier_Rating
* Description: A rating for the supplier based on past performance, on a scale from 3.0 (low) to 5.0 (high). Higher ratings indicate better reliability and shorter lead times.

Lead_Time
* Description: The actual time (in days) required to fulfill the order, including procurement, production, and delivery.
