# blind auction program that allows users to enter name and bid without seeing others bids 
# then works out highest bid. 
# uses a dictionary within a list

from replit import clear # uses repl.it module
from art import logo # uses separate file not included
print(logo)
print("Welcome to the secret auction program.")
auction = []
end = False
def add_new_bid(name_input, bid_input):        
        auction.append({
            "name" : name_input,
            "bid"  : bid_input
        })
 
while not end:
        name = input("What is your name?: ")
        bid = input("What is your bid?: $")
        other_bidders = input("Are there any other bidders? Type 'yes', or 'no'.\n").lower()
        
        add_new_bid(name_input=name, bid_input=bid)
        if other_bidders == "yes":
            end = False
            clear()
        elif other_bidders == "no":
            end = True
top_bid = 0
for item in auction:
    position = auction.index(item)
    bid_amount = int(auction[position]["bid"])
    bid_user = auction[position]["name"]
    if bid_amount > top_bid:
        top_bid = bid_amount
        top_bidder = bid_user
clear()

print(f"The winner is {top_bidder} with a bid of ${top_bid}")
