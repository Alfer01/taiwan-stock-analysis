
# Taiwan Stock Financial Report Analysis and Strategy

## Project Overview
This project analyzes financial reports of Taiwanese companies and generates buy or sell strategies based on financial indicators such as ROE and Debt-to-Asset ratio.

## Project Structure
```
/data
    /raw_data         # Raw financial data
    /processed_data   # Cleaned financial data
/scripts
    data_fetch.py     # Fetch financial data
    data_cleaning.py  # Clean the data
    financial_analysis.py # Financial indicator calculations and strategy generation
/models
    decision_tree.py  # Decision tree model for strategy
README.md
requirements.txt
```

## Installation
1. Install required Python libraries:
   ```
   pip install -r requirements.txt
   ```

2. Fetch financial data:
   ```
   python scripts/data_fetch.py
   ```

3. Clean the data:
   ```
   python scripts/data_cleaning.py
   ```

4. Generate financial indicators and strategy:
   ```
   python scripts/financial_analysis.py
   ```

5. Run decision tree model:
   ```
   python models/decision_tree.py
   ```

## License
This project is licensed under the MIT License.
