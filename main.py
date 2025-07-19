from app.api_client import LansweeperClient
from app.data_processor import DataProcessor
from app.server import run_server

def main():
    print("🛰️  Recupero dati da Lansweeper...")
    client = LansweeperClient()
    raw_data = client.fetch_assets()

    print("🧹 Pulizia e salvataggio...")
    processor = DataProcessor(raw_data)
    processor.clean()
    processor.save_to_csv()

    print("🚀 Avvio del server Flask...")
    run_server()

if __name__ == "__main__":
    main()
