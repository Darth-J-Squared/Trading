bal = 0 #your total balance of money
storewood = 0
woodp = 0
woodinv = 0
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
        print "Your balance is %d dollars." % (bal)
        command()
    elif c in ("Buy", "buy", "B", "b"):
        buy()
    elif c in ("Sell", "sell", "S", "s"):
        sell()
    elif c in ("Inventory", "inventory", "Inv", "inv"):
        print "You have %d wood." % (woodinv)
        command()
    elif c in ("Help", "help"):
        print "Available commands are store, balance, buy, sell, and inventory."
        command()
    else:
        print "Command not recognized"
        command()
def buy():
    global storewood
    global woodp
    global bal
    global woodinv
    print "What would you like to buy?"
    b = raw_input(">")
    if b in ("Wood", "wood"):
        print "How much would you like to buy?(There is %d left.)" % (storewood)
        amount = input(">")
        pp = amount * woodp
        if amount > storewood:
            print "There isn't that much product left."
            buy()
        elif amount * woodp > bal:
            print "You don't have enough funds to complete the transaction."
            command()
        elif amount < 0:
            print "You can't buy negative wood."
            command()
        else:
            print "You are buying %d wood at %d a piece, for a total of %d dollars, leaving you with a balance of %d" % (amount, woodp, pp, bal - pp)
            confirm = raw_input("Purchase?\n>")
            if confirm in ("Yes", "yes", "Y", "y"):
                storewood -= amount
                woodinv += amount
                bal -= (amount * woodp)
                print "Purchase completed."
                command()
            else:
                print "Input not recognized."
                command()
    else:
        print "Command not recongnized."
        command()
def sell():
    global storewood
    global woodp
    global bal
    global woodinv
    print "What would you like to sell?"
    s = raw_input(">")
    if s in ("Wood", "wood"):
        if woodinv == 0:
            print "You do not have any wood to sell."
            command()
        print "How much would you like to sell? You have %d." % (woodinv)
        amount = input(">")
        sp = amount * woodp
        if amount < 0:
            print "You can't sell negative wood."
            sell()
        elif amount > woodinv:
            print "You don't have that much wood."
            command()
        print "You are selling %d wood at %d a piece, for a total of %d dollars, leaving you with a balance of %d" % (amount, woodp, sp, bal + sp)
        confirm = raw_input("Sell?\n>")
        if confirm in ("Yes", "yes", "Y", "y"):
            woodinv -= amount
            bal += (amount * woodp)
            storewood += amount
            print "Transaction completed."
            command()
        else:
            print "Input not recognized."
            command()
    else:
        print "Command not recongnized."
        command()
def NY():
    global storewood
    global woodp
    print "Welcome to the New York market. There is %d wood at %d a piece." % (storewood, woodp)
    command()
storewood += 24
woodp += 153
bal += 123456
command()
