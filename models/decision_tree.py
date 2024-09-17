
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

def decision_tree_strategy():
    # Load the strategy data
    df = pd.read_csv(f'../data/processed_data/2330_strategy.csv')

    # Features: ROE and Debt_to_Asset
    X = df[['ROE', 'Debt_to_Asset']]
    y = df['Strategy'].apply(lambda x: 1 if x == 'Buy' else 0)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Decision tree model
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Model accuracy
    accuracy = clf.score(X_test, y_test)
    print(f"Decision Tree model accuracy: {accuracy:.2f}")

# Example usage
decision_tree_strategy()
