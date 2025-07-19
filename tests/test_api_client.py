from app.api_client import LansweeperClient
import pytest

def test_fetch_assets():
    client = LansweeperClient()
    try:
        data = client.fetch_assets()
        assert isinstance(data, list)
    except Exception as e:
        pytest.fail(f"API call failed: {e}")
