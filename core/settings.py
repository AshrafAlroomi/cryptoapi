from enum import Enum

API_BASE_URL = "https://sandbox-api.coinmarketcap.com/v1/"
API_KEY = "14a27bdb-20a2-4be1-9a8a-c54aa17431cb"


class EndPoints(Enum):
    OHCL = "cryptocurrency/ohlcv/latest"

