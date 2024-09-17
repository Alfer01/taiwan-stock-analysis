
import pandas as pd
import json

def clean_financial_data(stock_id):
    # Load the raw data
    with open(f'../data/raw_data/{stock_id}.json') as f:
        raw_data = json.load(f)

    # Convert JSON to DataFrame
    df = pd.DataFrame(raw_data['financials'])

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Save cleaned data to CSV
    df.to_csv(f'../data/processed_data/{stock_id}_cleaned.csv', index=False)
    print(f"Cleaned data for {stock_id} saved.")

# Example usage
clean_financial_data("2330")
