import random
def primary():
   # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = 13
    rnd = random.randint(0, last)
    print(quotes[rnd])
    print(quotes[random.randint(0, last)])

if __name__== "__main__":
  primary()
