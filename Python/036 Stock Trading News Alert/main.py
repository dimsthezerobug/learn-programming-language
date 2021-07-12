import os
import datetime as dt
import requests
from twilio.rest import Client


# Date ------------------------------------------------------------------------
class Date:
    def __init__(self):
        self.now = dt.datetime.now()
        self.today = self.now.date()
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weekday = dt.date(self.now.year, self.now.month, self.now.day).weekday()
        print(f"{self.weekdays[self.weekday]}, {self.today}")
        if self.weekday == 0:
            self.yesterday = self.today - dt.timedelta(days=3)
        else:
            self.yesterday = self.today - dt.timedelta(days=1)


# Stock Price -----------------------------------------------------------------
class Stock:
    def __init__(self, stock, today, yesterday):
        self.PARAMS = {
            "function": "TIME_SERIES_DAILY",
            "symbol": stock,
            "apikey": "E1199E59XRPMW66M",
        }
        self.response = requests.get(url="https://www.alphavantage.co/query?", params=self.PARAMS)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.today_price = float(self.data["Time Series (Daily)"][f"{today}"]["4. close"])
        self.yesterday_price = float(self.data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
        self.precentage = round((self.today_price - self.yesterday_price) / self.yesterday_price * 100, 1)


# Get News --------------------------------------------------------------------
def get_news(company_name, today, yesterday):
    PARAMS = {
        "q": company_name,
        "from": yesterday,
        "to": today,
        "sortBy": "popularity",
        "apiKey": "4952848596204662828579c3de1fd423",
    }
    response = requests.get(url="https://newsapi.org/v2/everything?", params=PARAMS)
    response.raise_for_status()
    data = response.json()
    news = {
        "headline": data["articles"][0]["title"],
        "url": data["articles"][0]["url"]
    }
    return news


# Send SMS --------------------------------------------------------------------
def send_sms(message: str):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=message,
                        from_='+14804053941',
                        to='+6287837123646'
                    )

    print(message.status)


# Main Program ----------------------------------------------------------------
def main():
    # STOCK_API_KEY = "E1199E59XRPMW66M"
    # NEWS_API_KEY = "4952848596204662828579c3de1fd423"
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    date = Date()
    today = date.today
    yesterday = date.yesterday
    weekday = date.weekday

    if weekday != 5 and weekday != 6:
        stock = Stock(STOCK, today, yesterday)
        precentage = stock.precentage
        if precentage >= 0:
            precentage = "🔺" + str(precentage) + "%"
            news = get_news(COMPANY_NAME, today, yesterday)
        elif precentage <= 0:
            precentage = "🔻" + str(precentage)[1:] + "%"
            news = get_news(COMPANY_NAME, today, yesterday)
        message = f'{STOCK}: {precentage}\nHeadline: {news["headline"]}.\nUrl: {news["url"]}'
        send_sms(message)
    else:
        print("Today is closed.")


if __name__ == "__main__":
    main()
