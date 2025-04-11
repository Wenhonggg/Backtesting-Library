import pandas as pd

class DataLoader:
    def load_data(file_path):
        data = pd.read_csv(file_path)
        if not all(col in data.columns for col in ['timestamp', 'price', 'signal']):
            raise ValueError("CSV must contain 'timestamp', 'price', and 'signal' columns")
        return data