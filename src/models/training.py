import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_model(data_path):
    """
    Loads preprocessed data, trains a logistic regression model,
    evaluates it, and saves the trained model.
    """
    # Load the preprocessed data
    X_train, X_test, y_train, y_test = joblib.load(data_path)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='spam')
    recall = recall_score(y_test, y_pred, pos_label='spam')
    f1 = f1_score(y_test, y_pred, pos_label='spam')

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    # Save the trained model
    joblib.dump(model, 'models/spam_model.pkl')
    print("Logistic Regression Model saved to models/spam_model.pkl")

    # Train a Naive Bayes model
    nb_model = MultinomialNB()
    nb_model.fit(X_train, y_train)

    # Make predictions with Naive Bayes
    y_pred_nb = nb_model.predict(X_test)

    # Evaluate the Naive Bayes model
    accuracy_nb = accuracy_score(y_test, y_pred_nb)
    precision_nb = precision_score(y_test, y_pred_nb, pos_label='spam')
    recall_nb = recall_score(y_test, y_pred_nb, pos_label='spam')
    f1_nb = f1_score(y_test, y_pred_nb, pos_label='spam')

    print("\n--- Naive Bayes Model ---")
    print(f"Accuracy: {accuracy_nb:.4f}")
    print(f"Precision: {precision_nb:.4f}")
    print(f"Recall: {recall_nb:.4f}")
    print(f"F1 Score: {f1_nb:.4f}")

    # Save the Naive Bayes model
    joblib.dump(nb_model, 'models/nb_model.pkl')
    print("Naive Bayes Model saved to models/nb_model.pkl")

if __name__ == '__main__':
    train_model('data/processed_data.pkl')