import alertScraper
import json

def process(inp_wl):
    ###############################################
    j1 = alertScraper.just_scrape(inp_wl)
    w1 = j1.scrape_data()
    yrSpread_dict = {}
    #Makes a dictionary of Price : 52-week spread
    for tkr in w1:
        for k, v in (tkr.items()):
            if (k == 'price'):
                tempp = v 
            if (k == '52 Week-range'):
                hooh = (v.split(' -'))
                yrSpread_dict[tempp] = hooh
    return w1, yrSpread_dict

def main():
    spacs = ['GSAH', 'GIK', 'APXT', 'THCB', 'TTCF']
    soup = process(spacs)
    main_soup = soup[0]
    s2 = soup[1]
    print(main_soup)
    print(s2)
    with open('dailyreport.json', 'w') as df:
        for tkr in main_soup:
            json.dump(tkr, df, indent = 2) 

if __name__ == "__main__":
    main()

    