import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} posts.")
        return df
    except FileNotFoundError:
        print(f" {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
