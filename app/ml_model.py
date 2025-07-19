from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

class AssetModel:
    def __init__(self, df):
        self.df = df
        self.model = RandomForestClassifier()

    def train(self):
        X = self.df[["RAM", "CPU", "DiskSpace"]]
        y = self.df["is_faulty"]
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)

    def save_model(self, path="model.pkl"):
        joblib.dump(self.model, path)

    def load_model(self, path="model.pkl"):
        self.model = joblib.load(path)
