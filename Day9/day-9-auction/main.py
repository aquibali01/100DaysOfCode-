from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the secret auction program.")


any_other_bidders = True
bidders = {}

while any_other_bidders:
  bidder = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[bidder] = bid
  another_bidder = input("Are there any other bidders? Type 'yes' or no.\n").lower()

  clear()
  if another_bidder == "no":
    any_other_bidders = False

#max bidder and max bid
  bids = []
  for bidder, bid in bidders.items():
    bids.append(bid)
    max_bid = max(bids)
    if bid == max_bid:
      max_bidder_name = bidder

print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")