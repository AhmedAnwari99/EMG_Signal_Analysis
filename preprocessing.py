import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def create_up_down_dataset(up, down):
    X = np.concatenate([up.iloc[:, 1:].values, down.iloc[:, 1:].values], axis=1)
    y = np.append(np.ones(30), np.zeros(30))
    return X, y

def create_left_right_dataset(left, right):
    X = np.concatenate([left.iloc[:, 1:].values, right.iloc[:, 1:].values], axis=1)
    y = np.append(np.ones(30), np.zeros(30))
    return X, y

def split_and_scale(X, y):
    X = X.T  # transpose like in your notebook

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        shuffle=True,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test