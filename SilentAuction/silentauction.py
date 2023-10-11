
from art import logo

print(logo)


dict = {

}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")



while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    dict[name] = bid
    ask = input("Are there other users who wants to bid? 'yes' or 'no'").lower()
    if ask == 'no':
        find_highest_bidder(dict)
        break





    


