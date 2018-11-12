import requests
import sys

def main():

    stockSymbol = sys.argv[1]

    price = requests.get(f"https://api.iextrading.com/1.0/stock/{stockSymbol}/price")
    bestClosePrice1m = requests.get(f"https://api.iextrading.com/1.0/stock/{stockSymbol}/chart/1m")
    bestClosePrice1y = requests.get(f"https://api.iextrading.com/1.0/stock/{stockSymbol}/chart/1y")
    crypto = requests.get("https://api.iextrading.com/1.0/stock/market/crypto")
    gainers = requests.get(f"https://api.iextrading.com/1.0/stock/market/list/gainers")
    losers = requests.get(f"https://api.iextrading.com/1.0/stock/market/list/losers")


    bestClosePrice1mData = bestClosePrice1m.json()
    bestClosePrice1yData = bestClosePrice1y.json()
    gainersData = gainers.json()
    losersData = losers.json()
    priceData = price.json()
    cryptoData = crypto.json()

    closeprices1m = [x['close'] for x in bestClosePrice1mData]
    closeprices1y = [x['close'] for x in bestClosePrice1yData]
    companyGainers = [x['companyName'] for x in gainersData]
    companylosers = [x['companyName'] for x in losersData]
    cryptoCurrencyCompanies = [(x['companyName'], x['changePercent']) for x in cryptoData]

    print("")
    print(f"Stock Symbol: {stockSymbol}")
    print("Current Price: " + str(priceData))
    print("Best close price (1m): " + str(max(closeprices1m)))
    print("Best close price (1y): " + str(max(closeprices1y)))
    print("")
    print("-- Winners and Losers --")
    print("")
    print("Winners: ")
    print(*companyGainers, sep='\n')
    print("")
    print("losers: ")
    print(*companylosers, sep='\n')
    print("")
    print("-- Crypto Markets --")
    print("")
    print("Crypto Currency with lowest percent change: " + str(min(cryptoCurrencyCompanies, key = lambda t: t[1])[0]))
    print("Crypto Currency with highest percent change: " + str(max(cryptoCurrencyCompanies, key = lambda t: t[1])[0]))
    print("")

if __name__ == '__main__':
    main()