from yahoo_finance import Share

symbolfile = open("symbollist.txt")
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split("\n")


for symbol in newsymbolslist:
    yahoo = Share(symbol)
    print 'Price of {} is {}'.format(symbol, yahoo.get_price())
