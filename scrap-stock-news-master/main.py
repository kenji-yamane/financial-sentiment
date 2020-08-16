from config import APIConnection

api = APIConnection()

api.get_news(['FB', 'AMZN', 'AAPL', 'NFLX'], 50)

