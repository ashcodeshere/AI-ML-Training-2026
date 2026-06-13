# Currency Converter
import requests
import os
class CurrencyConverter:
    def __init__(self,apikey):
        self.__apikey=apikey
        pass
    def convert_currency(self,amount,from_currency,to_currency):
        try:
            data=requests.get(f"https://v6.exchangerate-api.com/v6/{self.__apikey}/pair/{from_currency}/{to_currency}/{amount}",timeout=5).json()
            if data["result"]=="success":                               #WebSite Used to Collect data - ExchangeRate.com
                converted_res=data["conversion_result"]
                rate=data["conversion_rate"]
                return rate,converted_res
            else:
                return None,None
        except Exception as e:
            print("Connection Error, Team is working on it")

from_currency=input("Enter currency from which to be converted: ").upper()
amount=float(input("Enter Amount: "))
tocurrency=input("Enter currency to which to be converted: ").upper()
o1=CurrencyConverter("f28922165152b257472bffb0")  #This API key is now Deactivated
rate,result=o1.convert_currency(amount,from_currency,tocurrency)
if rate:
    print(f"{amount}{from_currency}={result}{tocurrency}")
    print(f"Exchange Rate: 1{from_currency}={rate}{tocurrency}")
else:
    print("Conversion Failed. Check your API Key and currency Codes")