import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import random
import statistics

# # btc = yf.Ticker('BUSD-USD')
# # his = btc.history(period="MAX")

# # gap = 20
# lenbtc = len(his['Close'])
# mvavg = []
# pr = []
# stdev = []
# stdevupp = []
# stdevdown = []
# ind = []

# for i in range(lenbtc-200,lenbtc):
#     his['Close'][i:i+gap]
#     mean = his['Close'][i:i+gap].mean()
#     mvavg.append(mean)
#     stdevupp.append(mean+2*his["Close"][i:i+gap].std())
#     stdevdown.append(mean-2*his["Close"][i:i+gap].std())
#     ind.append(i)

# # plt.plot(ind, mvavg)
# # plt.plot(ind, stdevupp)
# # plt.plot(ind, stdevdown)
# # plt.show()

# pd.DataFrame([mvavg, stdevupp, stdevdown])
table = pd.read_html("https://finance.yahoo.com/cryptocurrencies")
split = list(table[0]["Symbol"])
cryptodict = {}
for i in split: 
    tick = yf.Ticker(i)
    his = tick.history(period="MAX")
    cryptodict[i] = his

tick = yf.Ticker('BTC-USD')
btc = tick.history(period="MAX")
link = cryptodict["LINK-USD"]

x = []
y = []
tickers = []
for tick in cryptodict.keys():
    gap = 5
    predict = 5
    sec = cryptodict[tick]
    merged = pd.merge(btc, sec, left_index=True, right_index=True)
    # print(merged)
    lenstock = len(merged)-gap
    start = random.choice(range(0, lenstock))
    mvavg = []
    pr = []
    stdev = []
    stdevupp = []
    stdevdown = []
    ind = []
    osc = []
    prs = []
    prspred = []
    btcpr = []
    btcpred = []
    returnprs = []
    returnbtc = []
    for i in range(start, start+gap):
        mean = merged['Close_x'][i:i+gap].mean()
        mvavg.append(mean)
        stdevupp.append(mean+2*merged['Close_x'][i:i+gap].std())
        stdevdown.append(mean-2*merged["Close_x"][i:i+gap].std())
        ind.append(i)
        osc.append((merged['Close_x'][i]-merged['Close_x'][i+gap])/merged['Close_x'][i+gap])
        prs.append(merged["Close_x"][i])
        prspred.append(merged["Close_x"][i+gap])
        btcpr.append(merged["Close_y"][i])
        btcpred.append(merged["Close_y"][i+gap])
    tempdf = pd.DataFrame([mvavg, stdevupp, stdevdown, osc])
    tempdf = tempdf.T
    tempmerged = merged[start:start+gap]
    tempdf.index = tempmerged.index
    for i in range(0, len(prs)):
        returnprs.append(prspred[i]-prs[-1])
        returnbtc.append(btcpred[i]-btcpr[-1])
    observed=(sum(returnprs)/len(returnprs)-sum(returnbtc)/len(returnbtc))/statistics.stdev(returnprs)
    y.append(observed)
    tickers.append(tick)
    x.append(pd.merge(tempdf, tempmerged, right_index = True, left_index = True))



print(tickers)

