import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print('{}) {}'.format(rnd,quotes[rnd]))

  # intCounter = 0
  # while intCounter < len(quotes):
      # print('{}) {}'.format(intCounter+1,quotes[intCounter]))
      # intCounter +=1

if __name__== "__main__":
  primary()
