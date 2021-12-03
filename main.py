import string
import random
import webbrowser

def web():
  alpha = list(string.ascii_letters) 
  digit = list(string.digits)

  url = "https://prnt.sc/"
  for i in range(3):
    url = url + str(random.choice(alpha)).lower()
  for i in range(3):
    url = url + str(random.choice(digit))

  url = url + "/"
  webbrowser.open(url)
  print(url)
  

while True:
  web()
  new = input("Another? ")
