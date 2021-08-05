class portfolio:
    
    def __init__(self, cash, position=dict(), cost=0):
        self.cash = cash
        self.position = position
    
    def get_capital(self):
        capital = self.cash
        for ticker, info in self.position.items():
            capital += info['shares'] * info['price']
        
        return capital
    
    def sell(self, ticker, shares, cost):
        self.position[ticker]['shares'] -= shares
        earnings = shares * self.position[ticker]['price']
        self.cash += earnings - cost
        print(f"Sell {ticker} : {shares} shares | +{earnings} cash - {cost} cost = {earnings - cost}")
        
    def buy(self, ticker, shares, cost, price=None):
        if ticker in self.position:
            expense = shares * self.position[ticker]['price']
            self.cash -= (expense + cost)
            self.position[ticker]['shares'] += shares
        else:
            expense = price * shares
            self.cash -= expense  - cost
            self.position[ticker] = {'price':price, 'shares':shares}
        print(f"Buy {ticker} : {shares} shares | -{expense} expense - {cost} cost = -{expense + cost}")
    
    def get_balance(self):
        print("Cash: {:>5}".format(self.cash))
        
        for ticker, info in self.position.items():
            print(f"{ticker}: ")
            print("{:>5} {:>5} {:>5}".format('', 'Price:', info['price']))
            print("{:>5} {:>5} {:>5}".format('', 'Shares', info['shares']))

        print("Capital: {:>5}".format(self.get_capital()))

    def update_prices(self, prices):
        for i, ticker in enumerate(self.position):
            self.position[ticker]['price'] = prices[i]

    def holding_percent(self):
        capital = self.get_capital()
        holding_percent = dict()
        for ticker, info in self.position.items():
            holding_percent[ticker + ' holding (%)'] = info['price'] * info['shares'] / capital * 100

        return holding_percent


