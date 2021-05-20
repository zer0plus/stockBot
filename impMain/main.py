import news_scrape
import moving_avg
import correlation
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
                print("ERROR: Please enter an integer value between 0-3")
            elif(i == 0):
                break
            elif(i == 1):
                news_scrape.scrape_news(ticker)
            elif(i == 2):
                moving_avg.move_avg(ticker)
            elif(i ==3):
                ticker2 = str(input("Please enter the Stock ticker that you would like to compare: "))
                correlation.correlate(ticker, ticker2)

        except Exception as e:
            print("ERROR: Please enter an integer value between 0-3")
            continue


if __name__ == "__main__":
    main()