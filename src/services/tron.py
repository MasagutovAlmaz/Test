from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.exceptions import AddressNotFound


def get_account_info(address: str):
    try:
        provider = HTTPProvider(
            endpoint_uri="https://api.trongrid.io",
            api_key="8951fd36-4981-493a-b026-960d080d582b"
        )
        client = Tron(provider=provider)

        try:
            balance = client.get_account_balance(address)
            resource = client.get_account_resource(address)

            return {
                "balance": balance,
                "bandwidth": resource.get("freeNetLimit", 0),
                "energy": resource.get("EnergyLimit", 0),
            }
        except AddressNotFound:
            return {
                "balance": 0,
                "bandwidth": 0,
                "energy": 0
            }

    except Exception as e:
        raise Exception(f"Ошибка при получении информации об аккаунте: {str(e)}")