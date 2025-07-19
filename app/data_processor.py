import pandas as pd
from .config import CSV_PATH

class DataProcessor:
    def __init__(self, raw_data):
        self.df = pd.DataFrame(raw_data)

    def clean(self):
        self.df.dropna(subset=["assetName"], inplace=True)

    def save_to_csv(self):
        self.df.to_csv(CSV_PATH, index=False)

    def get_dataframe(self):
        return self.df
