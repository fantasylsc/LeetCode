'''
They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢), your program would output 44—the number of ways to make 44¢ with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢

'''


# recursion

def change_possibilities_top_down(amount_left, denominations, current_index=0):

  # Base cases:
  # We hit the amount spot on. yes!
  if amount_left == 0:
      return 1

  # We overshot the amount left (used too many coins)
  if amount_left < 0:
      return 0

  # We're out of denominations
  if current_index == len(denominations):
      return 0

  print("checking ways to make %i with %s" % (
      amount_left,
      denominations[current_index:],
  ))

  # Choose a current coin
  current_coin = denominations[current_index]

  # See how many possibilities we can get
  # for each number of times to use current_coin
  num_possibilities = 0
  while amount_left >= 0:
      num_possibilities += change_possibilities_top_down(
          amount_left,
          denominations,
          current_index + 1,
      )
      amount_left -= current_coin

  return num_possibilities


# DP

def change_possibilities_bottom_up(amount, denominations):

  ways_of_doing_n_cents = [0] * (amount + 1)
  ways_of_doing_n_cents[0] = 1

  for coin in denominations:
      for higher_amount in range(coin, amount + 1):
          higher_amount_remainder = higher_amount - coin
          ways_of_doing_n_cents[higher_amount] += (
              ways_of_doing_n_cents[higher_amount_remainder]
          )

  return ways_of_doing_n_cents[amount]

