from random import *
bal = 0 #your total balance of money
storewood = 0
woodprice = 0
woodinv = 0
storesteel = 0
steelprice = 0
steelinv = 0
pricechangewood = 0
pricechangesteel = 0
displaypricechangewood = 0
woodchange = "You shouldn't see this. Anyway, hi!"


storewood += 24
woodprice += 153
bal += 123456
steelprice += 500
storesteel += 100
def command():
    global bal
    c = raw_input(">")
    if c in ("Store", "store", "S", "s"):
        NY()
    elif c == "momoney":
        mm = input("How much do you want?")
        bal += mm
        command()
    elif c in ("Balance", "balance", "Bal", "bal"):
        print "Your balance is $%d dollars." % (bal)
        command()
    elif c in ("Buy", "buy", "B", "b"):
        buy()
    elif c in ("Sell", "sell", "S", "s"):
        sell()
    elif c in ("Inventory", "inventory", "Inv", "inv"):
        print "You have %d wood and %d steel." % (woodinv, steelinv)
        command()
    elif c in ("Advance", "advance", "Adv", "adv", "A", "a"):
        nextday()
    elif c in ("Help", "help"):
        print "Available commands are store, balance, buy, sell, advance, and inventory."
        command()
    else:
        print "Command not recognized."
        command()
def buy():
    global storewood
    global woodprice
    global bal
    global woodinv
    global storesteel
    global steelprice
    global steelinv
    print "What would you like to buy?"
    b = raw_input(">")
    if b in ("Wood", "wood"):
        print "How much would you like to buy?(There is %d left.)" % (storewood)
        amount = input(">")
        pp = amount * woodprice
        if amount > storewood:
            print "There isn't that much product left."
            buy()
        elif amount * woodprice > bal:
            print "You don't have enough funds to complete the transaction."
            command()
        elif amount < 0:
            print "You can't buy negative wood."
            command()
        else:
            print "You are buying %d wood at $%d a piece, for a total of $%d, leaving you with a balance of $%d" % (amount, woodprice, pp, bal - pp)
            confirm = raw_input("Purchase?\n>")
            if confirm in ("Yes", "yes", "Y", "y"):
                storewood -= amount
                woodinv += amount
                bal -= pp
                print "Purchase completed."
                command()
            else:
                print "Transaction canceled."
                command()
    elif b in ("Steel", "steel"):
        print "How much would you like to buy? (there is %d left.)" % (storesteel)
        steelamount = input(">")
        spp = steelamount * steelprice
        if steelamount > storesteel:
            print "There isn't that much product left."
            buy()
        elif steelamount * steelprice > bal:
            print "You don't have enough funds to complete the transaction."
            command()
        elif steelamount < 0:
            print "You can't buy negative steel."
            command()
        else:
            print "You are buying %d steel at $%d a piece, for a total of $%d, leaving you with a balance of $%d" % (steelamount, steelprice, spp, bal - spp)
            confirm = raw_input("Purchase?\n>")
            if confirm in ("Yes", "yes", "Y", "y"):
                storesteel -= steelamount
                steelinv += steelamount
                bal -= spp
                print "Purchase completed."
                command()
            else:
                print "Transaction canceled."
                command()
    else:
        print "Command not recongnized."
        command()
def sell():
    global storewood
    global woodprice
    global bal
    global woodinv
    global storesteel
    global steelprice
    global steelinv
    print "What would you like to sell?"
    s = raw_input(">")
    if s in ("Wood", "wood"):
        if woodinv == 0:
            print "You do not have any wood to sell."
            command()
        print "How much would you like to sell? You have %d." % (woodinv)
        amount = input(">")
        sp = amount * woodprice
        if amount < 0:
            print "You can't sell negative wood."
            sell()
        elif amount > woodinv:
            print "You don't have that much wood."
            command()
        print "You are selling %d wood at $%d a piece, for a total of $%d, leaving you with a balance of $%d" % (amount, woodprice, sp, bal + sp)
        confirm = raw_input("Sell?\n>")
        if confirm in ("Yes", "yes", "Y", "y"):
            woodinv -= amount
            bal += sp
            storewood += amount
            print "Transaction completed."
            command()
    elif s in ("Steel", "steel"):
            if steelinv == 0:
                print "You do not have any steel to sell."
                command()
            print "How much would you like to sell? You have %d." % (steelinv)
            steelamount = input(">")
            steelsp = steelamount * steelprice
            if steelamount < 0:
                print "You can't sell negative steel."
                sell()
            elif steelamount > steelinv:
                print "You don't have that much steel."
                command()
            print "You are selling %d steel at $%d a piece, for a total of $%d , leaving you with a balance of $%d" % (steelamount, steelprice, steelsp, bal + steelsp)
            confirm = raw_input("Sell?\n>")
            if confirm in ("Yes", "yes", "Y", "y"):
                steelinv -= steelamount
                bal += steelsp
                storesteel += steelamount
                print "Transaction completed."
                command()
            else:
                print "Transaction canceled."
                command()
    else:
        print "Command not recongnized."
        command()
def NY():
    global storewood
    global woodprice
    print "Welcome to the New York market. There is %d wood at $%d a piece. There is also %d steel at $%d a piece." % (storewood, woodprice, storesteel, steelprice)
    command()
def nextday():
    global woodprice
    global steelprice
    global pricechangewood
    global pricechangesteel
    global displaypricechangewood
    global displaypricechangesteel
    global woodchange
    global steelchange
    print "Proceeding to next day."
    legacywoodprice = '%.2f' % round(woodprice, 2)
    pricechangewood = uniform(.6, 1.4)
    if pricechangewood > 1:
        woodchange = "increase"
    else:
        woodchange = "decrease"
    woodprice *= pricechangewood
    displaywoodprice = '%.2f' % round(woodprice, 2)
    displaypricechangewood = "%.0f%%" % (pricechangewood * 100 - 100)
    legacysteelprice = '%.2f' % round(steelprice, 2)
    pricechangesteel = uniform(.6, 1.4)
    if pricechangesteel > 1:
        steelchange = "increase"
    else:
        steelchange = "decrease"
    steelprice *= pricechangesteel
    displaysteelprice = '%.2f' % round(steelprice, 2)
    displaypricechangesteel = "%.0f%%" % (pricechangesteel * 100 - 100)
    print "The price of wood changed to $%s from $%s, a %s of %s. The price of steel changed to $%s from $%s, a %s of %s" % (displaywoodprice, legacywoodprice, woodchange, displaypricechangewood, displaysteelprice, legacysteelprice, steelchange, displaypricechangesteel)
    command()

command()
