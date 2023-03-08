"""The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually. 
"""

#from replit import clear
#from art import logo
#HINT: You can call clear() to clear the output in the console.
#print(logo)
print("Welcome to Secret-Auction-Program.")

secret_dict = {} # {name : bid_price}

def highest_bid_value(bidding_record): #bidding_record = secret_dict
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_price = bidding_record[bidder] 
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} and bid_price is Rs.{highest_bid}")

ask_bidder = True
while ask_bidder:
    name = input("What is your Name: ")
    amount = int(input("What is your Bid price: Rs."))
    secret_dict[name] = amount
    should_continue = input("there are other users who want to bid? type 'yes' or type 'no': ")
    if should_continue  == "yes":
      ask_bidder = True
       #clear()
    else:
      ask_bidder = False
      highest_bid_value(bidding_record=secret_dict)
        
      