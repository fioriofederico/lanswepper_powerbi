from app.data_processor import DataProcessor

def test_clean_and_save():
    data = [{"assetName": "PC1"}, {"assetName": None}]
    processor = DataProcessor(data)
    processor.clean()
    assert processor.get_dataframe().shape[0] == 1
