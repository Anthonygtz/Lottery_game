import matplotlib.pyplot as pl
import random

class LotterySimulation:

    # initialization method that sets default values for ticket cost, odds of winning, jackpot value, and weeks to simulate
    def __init__(self, ticket_cost = 2, odds_of_winning = 0.0000000300347201, jackpot_value = 40000000, weeks_to_simulate = 520):
        self.ticket_cost = ticket_cost
        self.odds_of_winning = odds_of_winning
        self.jackpot_value = jackpot_value
        self.weeks_to_simulate = weeks_to_simulate
        self.money_spent = 0
        self.money_won = 0
        self.weeks_simulated = 0

    # runs the simulation
    def run_simulation(self):
        # if weeks to simulate is greater than 0, simulate for the specified number of weeks
        if self.weeks_to_simulate > 0:
            for x in range(self.weeks_to_simulate):
                self.weeks_simulated = self.weeks_simulated + 1
                self.money_spent = self.money_spent + self.ticket_cost
                # if the user wins the lottery, add the jackpot value to the money won
                if self.play_lottery() == True:
                    self.money_won = self.money_won + self.jackpot_value

        # if weeks to simulate is 0, keep simulating until the user wins the jackpot
        if self.weeks_to_simulate == 0:
            won_jackpot = False
            while won_jackpot == False:
                self.weeks_simulated = self.weeks_simulated + 1
                self.money_spent = self.money_spent + self.ticket_cost
                # if the user wins the lottery, set the won_jackpot flag to True and add the jackpot value to the money won
                if self.play_lottery() == True:
                    won_jackpot = True
                    self.money_won = self.jackpot_value

    
    # plays the lottery and returns True if the user wins and False if the user loses
    def play_lottery(self):
        if random.random() <= self.odds_of_winning: 
            return True
        else:
            return False

    # returns a summary of the simulation
    def get_summary(self):
        return ("Money spent:     " + str(self.money_spent) + "\nMoney won:       " + str(self.money_won) + "\nWeeks simulated: " + str(self.weeks_simulated))


# Test code 1
# creates a LotterySimulation object and runs a simulation for 52000 weeks
sim = LotterySimulation(weeks_to_simulate=52000)
sim.run_simulation()
summary = sim.get_summary()
print(summary)

# Test code 2
# creates a LotterySimulation object and keeps running simulations until the user wins the jackpot
sim = LotterySimulation(odds_of_winning=.00000300347201, weeks_to_simulate=0)
sim.run_simulation()
summary = sim.get_summary()
print(summary)

# modifiers for the varibales
# initializes some variables to track money spent, money won, weeks simulated, and profit
money_spent = 0
money_won = 0
get_weeks_simulated = 0
profit = 0

# modifiers for the list varibales
# initializes some lists to track the amount of money spent and won each year, as well as the net profit
lost = []
gain = []
net_profit = []

simulation = LotterySimulation()

# Loop to simulate playing the lottery 1000000 times, each for 52 weeks
for x in range(1000000):
    for y in range(52):
        simulation.play_lottery() # simulate playing the lottery
        get_weeks_simulated = get_weeks_simulated + 1
        money_spent = money_spent + simulation.ticket_cost # add ticket cost to money spent
        if simulation.play_lottery() == True: # if player wins the jackpot
            money_won = money_won + simulation.jackpot_value # add the jackpot amount to money won
        if get_weeks_simulated == 5200: # if 5200 weeks have passed
            profit = money_won - money_spent # calculate profit
            net_profit.append(profit) # add the profit to the net_profit list
            get_weeks_simulated = 0 # reset weeks simulated counter
            lost.append(money_spent) # add the money spent to lost list
            gain.append(money_won) # add the money won to gain list

# Create a list of x-axis labels
x_label = list(range(10000))

# Plot the net profit, money spent, and money won on a graph
pl.plot(x_label, net_profit, 'r--', label = "Profit")
pl.plot(x_label, lost, 'b:', label = "Spent")
pl.plot(x_label, gain, 'g-.', label = "Won")

# Add x and y axis labels and a title to the graph
pl.xlabel("Years")
pl.ylabel("Money($)")
pl.title("Lottery")

# Set the size of the figure
fig = pl.gcf()
fig.set_size_inches(8,6)

# Add a legend to the graph and save it as an image file
pl.legend(loc="upper left")
fig.savefig('lottery_profit.png')

# Show the graph
pl.show()