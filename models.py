from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

def get_models():
    return {
        "KNN": KNeighborsClassifier(),
        "SVM": SVC(),
        "DecisionTree": DecisionTreeClassifier(),
        "LogisticRegression": LogisticRegression()
    }