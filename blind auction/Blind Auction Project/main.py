import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
print(art.logo)

def highestBidder(bid_dict):
    winner = ""
    highest_bid = 0
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
answer = True

while answer:
    name = input("What is your full name?  ")
    price = int(input("What is your bidding price? $"))
    bids[name] = price
    ask = input("Are there other bidders? 'yes' or 'no':  \n").lower()
    if ask == "no":
        answer = False
        highestBidder(bids)
    elif ask == "yes":
        print("\n" * 20)








# print("\n" * 20)