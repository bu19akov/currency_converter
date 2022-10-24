import requests
import json

code = input("Enter which currency you have: ")
r = requests.get(f"http://www.floatrates.com/daily/{code.lower()}.json")
my_dict = json.loads(r.text)
cache = dict()
if code.lower() != "usd":
    cache["usd"] = my_dict["usd"]["rate"]
if code.lower() != "eur":
    cache["eur"] = my_dict["eur"]["rate"]
while True:
    exchange = input("Enter the currency you want to buy: ").lower()
    if exchange == "":
        break
    print("Checking the cache...")
    if exchange not in cache.keys():
        print("Sorry, but it is not in the cache!")
        cache[exchange] = my_dict[exchange]["rate"]
    else:
        print("Oh! It is in the cache!")
    amount = float(input("Input the amount of money: "))
    print(f"You received {round(cache[f'{exchange}'] * amount, 2)} {exchange.upper()}.")

