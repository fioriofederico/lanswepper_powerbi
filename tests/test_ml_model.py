import pandas as pd
from app.ml_model import AssetModel

def test_train_model():
    df = pd.DataFrame({
        "RAM": [8, 16], "CPU": [4, 8], "DiskSpace": [256, 512], "is_faulty": [0, 1]
    })
    model = AssetModel(df)
    model.train()
    assert model.model is not None
