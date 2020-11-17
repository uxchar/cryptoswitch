

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#CoinMarketCap API Connection

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol': 'BTC,ETH,XRP,LTC,BNB',
  'convert': 'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'cb5b41c0-fe01-40ef-89c6-3265f1603332',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#Welcome screen that shows what cryptocurrency is currently supported by the application

def main():
    print("***********************")
    print("Welcome!")
    print("This app uses USD for conversions")
    print("Here are some cryptocurrency options: BTC ETH XRP LTC BNB")
    print("***********************")
    print()

    crypto_support = set(['BTC', 'ETH', 'XRP', 'LTC', 'BNB'])

    def yes_no(answer):
        yes = set(['yes','y'])
        no = set(['no','n'])

        while True:
            choice = input(answer).lower()
            if choice in yes:
               return True
            elif choice in no:
               return False
            else:
               print("Please respond with yes or no to continue")

    start_con = yes_no("Would you like to perform a conversion? Y/N")

#Main loop, user may exit the program by typing "N" to exit at the end
    while start_con is True:
        option = input("Please type (1) USD to Crypto or (2) Crypto to USD  ")
        coin_second = input("What currency you would like to convert to. BTC ETH XRP LTC BNB  ").upper()

        if coin_second in crypto_support:
            pass
        else:
            coin_second = input("Please type in a supported cryptocurrency.  ").upper()


        amount = float(input("Please choose the amount of currency to convert.  "))

#Conversation code from USD to Crypto

        if option == '1':
            def convert_1():
                if  coin_second == 'BTC':
                    coin = data['data']['BTC']['symbol']
                    rate = data['data']['BTC']['quote']['USD']['price']
                    conversion = 1 / rate
                    print("1", 'USD', "=", coin, conversion)
                    print(amount, 'USD', "=", coin, conversion * amount)
                elif coin_second == 'ETH':
                    coin = data['data']['ETH']['symbol']
                    rate = data['data']['ETH']['quote']['USD']['price']
                    conversion = 1 / rate
                    print("1", 'USD', "=", coin, rate)
                    print(amount, 'USD', "=", coin_second, conversion * amount)
                elif coin_second == 'XRP':
                    coin = data['data']['XRP']['symbol']
                    rate = data['data']['XRP']['quote']['USD']['price']
                    conversion = 1 / rate * amount
                    print("1", 'USD', "=", coin, conversion)
                    print(amount, 'USD', "=", coin, conversion * amount)
                elif coin_second == 'LTC':
                    coin = data['data']['LTC']['symbol']
                    rate = data['data']['LTC']['quote']['USD']['price']
                    conversion = 1 / rate
                    print("1", 'USD', "=", coin, conversion)
                    print(amount, 'USD', "=", coin, conversion * amount)
                elif coin_second == 'BNB':
                    coin = data['data']['BNB']['symbol']
                    rate = data['data']['BNB']['quote']['USD']['price']
                    conversion = 1 / rate
                    print("1", 'USD', "=", coin, conversion)
                    print(amount, 'USD', "=", coin, conversion * amount)
                else:
                    print("This cryptocurrency doesn't exist or is not yet supported by this app.")
            convert_1()
            print()
            start_con = yes_no("Would you like to perform another conversion? Y/N")



        else:

#Conversation code from Crypto to USD

            def convert_2():
                if  coin_second == 'BTC':
                    coin = data['data']['BTC']['symbol']
                    rate = data['data']['BTC']['quote']['USD']['price']
                    conversion = rate * amount
                    print("1", coin, "=", 'USD', rate)
                    print(amount, coin, "=", 'USD', conversion)
                elif coin_second == 'ETH':
                    coin = data['data']['ETH']['symbol']
                    rate = data['data']['ETH']['quote']['USD']['price']
                    conversion = rate * amount
                    print("1", coin, "=", 'USD', rate)
                    print(amount, coin, "=", 'USD', conversion)
                elif coin_second == 'XRP':
                    coin = data['data']['XRP']['symbol']
                    rate = data['data']['XRP']['quote']['USD']['price']
                    conversion = rate * amount
                    print("1", coin, "=", 'USD', rate)
                    print(amount, coin, "=", 'USD', conversion)
                elif coin_second == 'LTC':
                    coin = data['data']['LTC']['symbol']
                    rate = data['data']['LTC']['quote']['USD']['price']
                    conversion = rate * amount
                    print("1", coin, "=", 'USD', rate)
                    print(amount, coin, "=", 'USD', conversion)
                elif coin_second == 'BNB':
                    coin = data['data']['BNB']['symbol']
                    rate = data['data']['BNB']['quote']['USD']['price']
                    conversion = rate * amount
                    print("1", coin, "=", 'USD', rate)
                    print(amount, coin, "=", 'USD', conversion)
                else:
                    print("This cryptocurrency doesn't exist or is not yet supported by this app.")
            convert_2()
            print()
            start_code = yes_no("Would you like to perform another conversion? Y/N")

main()
