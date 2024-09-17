
import pandas as pd

def calculate_indicators(stock_id):
    # Load cleaned data
    df = pd.read_csv(f'../data/processed_data/{stock_id}_cleaned.csv')

    # Calculate ROE and Debt to Asset ratio
    df['ROE'] = df['net_income'] / df['equity']
    df['Debt_to_Asset'] = df['total_liabilities'] / df['total_assets']

    # Generate buy/sell strategy based on simple conditions
    df['Strategy'] = df.apply(lambda row: 'Buy' if row['ROE'] > 0.15 and row['Debt_to_Asset'] < 0.5 else 'Sell', axis=1)

    # Save the strategy
    df.to_csv(f'../data/processed_data/{stock_id}_strategy.csv', index=False)
    print(f"Strategy for {stock_id} calculated.")

# Example usage
calculate_indicators("2330")
