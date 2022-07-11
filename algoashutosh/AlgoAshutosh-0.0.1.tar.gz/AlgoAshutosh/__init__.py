# Algo Trading Library for Python3 by Ashutosh Aswani

    #=============================================================================================

import csv

    #=============================================================================================

class AlgoTrade:

    #=============================================================================================
    # returns the number rounding off to the closest fifty. For example rounds off 12340 to 12350.

    def closestFifty(self,a):
        base = (int(int(a)/int(50)))*50
        remainder = int(a)%50
        if(remainder>=25):
            return (base+50)
        else:
            return base

    #=============================================================================================
    # pass 2022,3,5--> it will return it in a yyyy-mm-dd date format like 2022-03-05.

    def dateGeneration(self,year,month,entry):
        dateString=""
        dateString=dateString+str(year)+"-"
        if(int(month)<10):
            dateString=dateString+"0"+str(month)+"-"
        else:
            dateString=dateString+str(month)+"-"
        if(int(entry)<10):
            dateString=dateString+"0"+str(entry)
        else:
            dateString=dateString+str(entry)

        return dateString

    #=============================================================================================
    # returns the number of unique months and their expiry dates in a dictionary format

    def numberOfMonthsInFile(self,file):
        months = {"1":"1"}
        months.clear()
        with open(file, 'r') as f:
            spotFile = csv.reader(f)
            next(spotFile)
            for row in spotFile:
                month = (str(row[2]))
                expiry = str(row[4])
                if(not(month in months)):
                    months[month] = expiry

        return months

    #=============================================================================================

    #it returns the value of the spot price for the given month and entry date
    #the spot price is rounded of to the next closest smaller integral value and returned.

    def returnSpotPrice(self,file,month,entry):
        currentDay = 0
        with open(file, 'r') as f:
            spotFile = csv.reader(f)
            next(spotFile)
            for row in spotFile:
                currentMonth = (row[2])
                if(int(month) == int(currentMonth)):
                    currentDay+=1
                if(int(currentDay)==int(entry)):
                    return str(int(float(row[5])))

    #=============================================================================================

    # returns the net profit calculated by accepting a dictionary storing the past month changes.

    def netProfit(self,list):
        amount = 100000
        for ratios in list:
            amount = int(amount) * int(ratios)
        return amount

    #=============================================================================================

class optionPrices:

    #=============================================================================================

    #It returns the price of the put option that has been sold for the strike price given.

    def returnPutPrice(self,file,month,entry,strike):
        currentDay = 0
        with open(file, 'r') as f:
            putFile = csv.reader(f)
            next(putFile)
            for row in putFile:
                currentMonth = int(row[2])
                strikePrice = int(row[6])
                if(int(month) == int(currentMonth) and strike==strikePrice):
                    currentDay+=1
                if(int(currentDay)==int(entry)):
                    return str(int(float(row[7])))

    #=============================================================================================

    #It returns the price of the call option that has been sold for the strike price given.

    def returnCallPrice(self,file,month,entry,strike):
        currentDay = 0
        with open(file, 'r') as f:
            callFile = csv.reader(f)
            next(callFile)
            for row in callFile:
                currentMonth = int(row[2])
                strikePrice = int(row[6])
                if(int(month) == int(currentMonth) and strike==strikePrice):
                    currentDay+=1
                if(int(currentDay)==int(entry)):
                    return str(int(float(row[7])))

    #=============================================================================================

class ironCondor:

    #=============================================================================================

    # The short strangle strategy is  selling otm call and put options.

    def ironCondorStrategy(self,putFile,callFile,spotFile,sellPut,sellCall,buyCall,buyPut,entry,exit,lotSize):
        algo = AlgoTrade()
        priceOfOption = optionPrices()
        listOfMonths = algo.numberOfMonthsInFile(spotFile)
        profit = {"1":"1"}
        month=" "
        ratioChange=" "
        profit.clear()
        for key in listOfMonths:
            month = str(key)
            expiryDate = int(listOfMonths[key][7:9])
            spotPrice = algo.returnSpotPrice(spotFile,key,entry)
            spotPriceRounded = algo.closestFifty(spotPrice)

            sellCallStrike = (spotPriceRounded+sellCall)
            buyCallStrike = (spotPriceRounded+buyCall)
            sellPutStrike = (spotPriceRounded-sellPut)
            buyPutStrike = (spotPriceRounded-buyPut)

            sellCallPrice = priceOfOption.returnCallPrice(callFile,month,entry,sellCallStrike)
            buyCallPrice = priceOfOption.returnCallPrice(callFile,month,entry,buyCallStrike)
            sellPutPrice = priceOfOption.returnPutPrice(putFile,month,entry,sellPutStrike)
            buyPutPrice = priceOfOption.returnPutPrice(putFile,month,entry,buyPutStrike)

            premiumReceived = (int(sellCallPrice) + int(sellPutPrice)) - (int(buyCallPrice) + int(buyPutPrice))

            sellCallPriceExit = priceOfOption.returnCallPrice(callFile,month,(expiryDate - exit),sellCallStrike)
            buyCallPriceExit = priceOfOption.returnCallPrice(callFile,month,(expiryDate - exit),buyCallStrike)
            sellPutPriceExit = priceOfOption.returnPutPrice(putFile,month,(expiryDate - exit),sellPutStrike)
            buyPutPriceExit = priceOfOption.returnPutPrice(putFile,month,(expiryDate - exit),buyPutStrike)

            premiumAtExit = (int(sellCallPriceExit) + int(sellPutPriceExit)) - (int(buyCallPriceExit) + int(buyPutPriceExit))

            profit[month]  = (int(sellCallPriceExit) + int(sellPutPriceExit)) * int(lotSize)
            print("Profit per lot is =",((premiumReceived - premiumAtExit)*int(lotSize)))

    #=============================================================================================

class shortStraddle:

    #=============================================================================================

    # The short straddle strategy is  selling atm call and put options.

    def shortStraddleStrategy(self,putFile,callFile,spotFile,entry,exit,lotSize):
        algo = AlgoTrade()
        priceOfOption = optionPrices()
        listOfMonths = algo.numberOfMonthsInFile(spotFile)
        profit = {"1":"1"}
        month=" "
        ratioChange=" "
        profit.clear()
        for key in listOfMonths:
            month = str(key)
            expiryDate = int(listOfMonths[key][7:9])
            spotPrice = algo.returnSpotPrice(spotFile,key,entry)
            spotPriceRounded = algo.closestFifty(spotPrice)

            sellCallPrice = priceOfOption.returnCallPrice(callFile,month,entry,spotPriceRounded)
            sellPutPrice = priceOfOption.returnPutPrice(putFile,month,entry,spotPriceRounded)

            premiumReceived = (int(sellCallPrice) + int(sellPutPrice))

            sellCallPriceExit = priceOfOption.returnCallPrice(callFile,month,(expiryDate - exit),spotPriceRounded)
            sellPutPriceExit = priceOfOption.returnPutPrice(putFile,month,(expiryDate - exit),spotPriceRounded)

            premiumAtExit = (int(sellCallPriceExit) + int(sellPutPriceExit))

            profit[month]  = (int(sellCallPriceExit) + int(sellPutPriceExit)) * int(lotSize)
            print("Profit per lot is =",((premiumReceived - premiumAtExit)*int(lotSize)))

    #=============================================================================================

class shortStrangle:

    #=============================================================================================

    # The iron condor strategy is  selling otm call and put options and
    # buying further otm call and put options to hedge the strategy.

    def shortStrangleStrategy(self,putFile,callFile,spotFile,sellPut,sellCall,entry,exit,lotSize):
        algo = AlgoTrade()
        priceOfOption = optionPrices()
        listOfMonths = algo.numberOfMonthsInFile(spotFile)
        profit = {"1":"1"}
        month=" "
        ratioChange=" "
        profit.clear()
        for key in listOfMonths:
            month = str(key)
            expiryDate = int(listOfMonths[key][7:9])
            spotPrice = algo.returnSpotPrice(spotFile,key,entry)
            spotPriceRounded = algo.closestFifty(spotPrice)

            sellCallStrike = (spotPriceRounded+sellCall)
            sellPutStrike = (spotPriceRounded-sellPut)

            sellCallPrice = priceOfOption.returnCallPrice(callFile,month,entry,sellCallStrike)
            sellPutPrice = priceOfOption.returnPutPrice(putFile,month,entry,sellPutStrike)

            premiumReceived = (int(sellCallPrice) + int(sellPutPrice))

            sellCallPriceExit = priceOfOption.returnCallPrice(callFile,month,(expiryDate - exit),sellCallStrike)
            sellPutPriceExit = priceOfOption.returnPutPrice(putFile,month,(expiryDate - exit),sellPutStrike)

            premiumAtExit = (int(sellCallPriceExit) + int(sellPutPriceExit))

            profit[month]  = (int(sellCallPriceExit) + int(sellPutPriceExit)) * int(lotSize)
            print("Profit per lot is =",((premiumReceived - premiumAtExit)*int(lotSize)))

    #=============================================================================================
