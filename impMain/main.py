import news_scrape

def main():
    ticker = str(input("Please enter the Stock ticker that you would like to analyze: "))
    
    totalChoices = 3

    print()
    print("What would you like to know about this stock?")
    print("(1) Get recent news")
    print("(2) Analyze Moving Average")
    print("(3) Compare correlation with another stock")
    print("(0) Exit")
     
    while(True):
        try:
            print()
            i = int(input("Please Enter your selection: "))
            if (i < 0 or i > totalChoices):
                # print()
                print("ERROR: Please enter an integer value between 0-3")
            else:
                break
        except Exception:
            # print()
            print("ERROR: Please enter an integer value between 0-3")
            continue
    if (i == 1):
        news_scrape.scrape_news(ticker)

if __name__ == "__main__":
    main()