from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    results = {
        "ROC AUC": roc_auc_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "Accuracy": accuracy_score(y_test, y_pred),
        "Confusion Matrix": confusion_matrix(y_test, y_pred)
    }

    return results


def plot_signals(data, labels):
    plt.plot(data[:, labels == 0], 'b')
    plt.plot(data[:, labels == 1], 'r')
    plt.show()

def plot_confusion_matrix(cm):
    display = ConfusionMatrixDisplay(cm)
    display.plot()
    plt.show()

def plot_decision_tree(model):
    if isinstance(model, DecisionTreeClassifier):
        plt.figure(figsize=(20, 5))
        plot_tree(model, filled=True)
        plt.show()