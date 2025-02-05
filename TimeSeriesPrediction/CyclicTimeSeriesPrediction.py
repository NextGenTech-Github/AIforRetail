import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy for random data generation (optional)

try:
    # Sample data (replace with your actual data)
    data = {'date': pd.date_range(start='2024-01-01', periods=52, freq='D')}

    # Check if 'date' column exists and has datetime data type
    if 'date' not in data or not pd.api.types.is_datetime64_dtype(data['date']):
        print("Error: 'date' column is missing or has incorrect data type.")
        exit()  # Exit the program if there's an issue

    df = pd.DataFrame(data)

    # Resample data to weekly (modify 'W' for different frequencies)
    weekly_df = df.resample('W-MON', on='date').agg(mean=('value', 'mean'))

    # Calculate year and week for cyclic analysis
    weekly_df['year'] = weekly_df['date'].dt.year
    weekly_df['week'] = weekly_df['date'].dt.isocalendar().week

    # Group by year for visualization (optional)
    yearly_means = weekly_df.groupby('year')['value'].mean()

    # Plot weekly data (modify as needed)
    plt.figure(figsize=(10, 6))
    plt.plot(weekly_df['date'], weekly_df['value'], marker='o', linestyle='-', label='Weekly Value')

    # Optional: Plot yearly means (uncomment and adjust)
    # plt.plot(yearly_means.index, yearly_means.values, marker='o', linestyle='-', label='Yearly Mean')

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Weekly Data with Cyclic Pattern (Optional: Yearly Means)')
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")