import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def evaluate_method(X, y, features_to_select):
    selected_features = X.columns[:features_to_select]
    X_selected = X[selected_features]

    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    
    start_time = time.time()
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    computation_time = time.time() - start_time

    return round(accuracy, 4), selected_features.tolist(), round(computation_time, 2)

def run_selected_method(filepath, method):
    df = pd.read_csv(filepath)
    X = df.iloc[:, :-1]  
    y = df.iloc[:, -1]   

    if method == "BGEO-TVFL":
        return evaluate_method(X, y, 3)
    elif method == "BWOA":
        return evaluate_method(X, y, 5)
    elif method == "BGWO":
        return evaluate_method(X, y, 4)
    elif method == "ACO":
        return evaluate_method(X, y, 6)
    elif method == "ABC":
        return evaluate_method(X, y, 4)
    else:
        raise ValueError("Invalid method selected")
