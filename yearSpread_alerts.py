import alertScraper
import json

def process(inp_wl):
    ###############################################
    j1 = alertScraper.just_scrape(inp_wl)
    w1 = j1.scrape_data()
    yrSpread_dict = {}
    #Makes a dictionary of Price : 52-week spread
    for tkr in w1:
        tempp = []
        for k, v in (tkr.items()):
            if (k == '$ticker'):
                tempp.append(v)
            if (k == 'price'):
                tempp.append(v)    
            if (k == '52 Week-range'):
                hooh = (v.split(' -'))
        yrSpread_dict[tuple(tempp)] = hooh
                
    for k, v in yrSpread_dict.items():
        if(float(k[1]) >= (0.9 * float(v[1]))):
            for tkr in w1:
                if(str(tkr.get('$ticker')) == str(k[0])):
                    tkr['Alerts'] += 'Trading near All Time High!'
            print('Stock: ' + str(k[0]) + ' is trading near ATH')
        else:
            for tkr in w1:
                if(str(tkr.get('$ticker')) == str(k[0])):
                    tkr['Alerts'] = 'None'
    return w1, yrSpread_dict

def main():
    spacs = ['QQQ', 'GSAH', 'GIK', 'APXT', 'THCB', 'TTCF', 'CCIV']
    while(True):
        print("Your current watchlist contains the following stocks: " + str(spacs))
        try:
            inp1 = int(input("Press 1 to enter more stocks or press 0 to continue: "))
            if(inp1 == 1):
                inp2 = input("Enter the stock ticker that you want to add to the watchlist: ")
                spacs.append(inp2)
            else:
                break
        except:
            print("Please Enter either 1 or 0")
    try:
        soup = process(spacs)
        main_soup = soup[0]
        with open('dailyreport.json', 'w') as df:
            for tkr in main_soup:
                json.dump(tkr, df, indent = 2) 
    except:
        print('One of the tickers you entered is unavailable, please try again')
    
if __name__ == "__main__":
    main()