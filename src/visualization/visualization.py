import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

def visualize_results(data_path, model_path):
    """
    Loads data and a trained model, generates and saves visualizations
    of the model's performance.
    """
    # Load the preprocessed data and the model
    _, X_test, _, y_test = joblib.load(data_path)
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X_test)

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    print("Confusion matrix saved to confusion_matrix.png")

    # Calculate metrics
    precision = precision_score(y_test, y_pred, pos_label='spam')
    recall = recall_score(y_test, y_pred, pos_label='spam')
    f1 = f1_score(y_test, y_pred, pos_label='spam')

    # Plot metrics
    metrics = {'Precision': precision, 'Recall': recall, 'F1 Score': f1}
    plt.figure(figsize=(8, 5))
    plt.bar(metrics.keys(), metrics.values())
    plt.ylim(0, 1)
    plt.title('Model Performance Metrics')
    for i, v in enumerate(metrics.values()):
        plt.text(i, v + 0.02, f"{v:.4f}", ha='center')
    plt.savefig('performance_metrics.png')
    print("Performance metrics plot saved to performance_metrics.png")

if __name__ == '__main__':
    visualize_results('data/processed_data.pkl', 'models/spam_model.pkl')
