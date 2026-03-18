import pandas as pd

def load_data(base_path):
    data = {
        "RIGHT": pd.read_csv(f"{base_path}/RIGHT.csv"),
        "LEFT": pd.read_csv(f"{base_path}/LEFT.csv"),
        "UP": pd.read_csv(f"{base_path}/UP.csv"),
        "DOWN": pd.read_csv(f"{base_path}/DOWN.csv"),
    }
    return data