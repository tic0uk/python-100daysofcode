import requests
from twilio.rest import Client

STOCK = "TSLA"
STOCKS_Endpoint = "https://www.alphavantage.co/query"

stocks_parameters = {
    "apikey": "removed",
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
}

response = requests.get(STOCKS_Endpoint, stocks_parameters)
response.raise_for_status()
daily_stock_data = response.json()["Time Series (Daily)"].items()
last_two_days_list = list(daily_stock_data)[0:2]

closing_values = [value["4. close"] for (key, value) in last_two_days_list]
yesterday_close = float(closing_values[0])
two_days_ago_close = float(closing_values[1])

percentage_change = round((yesterday_close - two_days_ago_close) / two_days_ago_close * 100, 2)

NEWS_Endpoint = "http://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
news_parameters = {
    "apikey": "removed",
    "q": COMPANY_NAME,
    "pageSize": 3,
    "sortBy": "popularity"
}

response = requests.get(NEWS_Endpoint, news_parameters)
response.raise_for_status()
articles = response.json()["articles"]

def send_message():
    account_sid = "removed"
    auth_token = "removed"
    for item in range(0, 3):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                body=f"TSLA: {formatted_percentage}\n"
                     f"Headline: {articles[item]['title']}\n"
                     f"Brief: {articles[item]['description']}",
                from_='+removed',
                to='+removed'
                )
        print(message.status)


if percentage_change > 5:
    formatted_percentage = f"👆{percentage_change}%"
    send_message()
elif percentage_change < -5:
    formatted_percentage = f"👇️{percentage_change}%"
    send_message()
