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
            print('Stock: ' + str(k[0]) + ' is trading near ATH')
        print('min requiried: ' + str(0.9 * float(v[1])))
        print(round((float(v[1]) - float(k[1])), 2))
    return w1, yrSpread_dict

def main():
    spacs = ['GSAH', 'GIK', 'APXT', 'THCB', 'TTCF', 'CCIV']
    soup = process(spacs)
    main_soup = soup[0]
    s2 = soup[1]
    # print(main_soup)
    print('\n')
    print(s2)
    with open('dailyreport.json', 'w') as df:
        for tkr in main_soup:
            json.dump(tkr, df, indent = 2) 

if __name__ == "__main__":
    main()

    