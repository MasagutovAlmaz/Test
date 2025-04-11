import pytest
import httpx
from fastapi.testclient import TestClient
from datetime import datetime
from src.models.tron import Tron
from datetime import datetime


from main import app
from src.models.tron import Tron

client = TestClient(app)

address = "TYnyEXrFS2GjZSLz3JSrJDLicJyDWS3VJw"

def test_check_address_data():
    # Arrange
    request_data = {"address": address}

    # Act
    response = client.post("/tron", json=request_data)

    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["address"] == address
    assert "balance" in response_data
    assert "bandwidth" in response_data
    assert "energy" in response_data


def test_create_tron_with_all_fields():
    balance = 1000
    bandwidth = 500
    energy = 200
    created_at = datetime.now()

    # Act
    tron = Tron(
        address=address,
        balance=balance,
        bandwidth=bandwidth,
        energy=energy,
        created_at=created_at
    )

    # Assert
    assert tron.address == address
    assert tron.balance == balance
    assert tron.bandwidth == bandwidth
    assert tron.energy == energy
    assert tron.created_at == created_at
    assert tron.id is None
