
import json
import os

def fetch_financial_data(stock_id):
    # Simulate fetching financial data
    data = {
        "stock_id": stock_id,
        "financials": [
            {"year": 2022, "revenue": 1000, "net_income": 100, "equity": 500, "total_assets": 2000, "total_liabilities": 800},
            {"year": 2023, "revenue": 1200, "net_income": 150, "equity": 600, "total_assets": 2200, "total_liabilities": 900}
        ]
    }
    # Save the data
    file_path = f"../data/raw_data/{stock_id}.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    print(f"Financial data for {stock_id} saved.")

# Example usage
fetch_financial_data("2330")
