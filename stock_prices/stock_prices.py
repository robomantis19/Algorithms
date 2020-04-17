#!/usr/bin/python

import argparse

def find_max_profit(prices):

  for i in range(len(prices)):
    print(i)
    first = prices[i]
    if i >= 1: 
      last = prices[i-1]
      if first < last: 
        lowest = prices[i]
      if first > last: 
        highest = prices[i]
        return highest - lowest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))