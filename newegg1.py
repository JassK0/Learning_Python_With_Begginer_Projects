#this finds what is in the strong tag on the newegg site
import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.ca/asrock-radeon-rx-6700-xt-rx6700xt-cld-12g/p/N82E16814930056"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text = "$")
parent = prices[0].parent
#print parent to find the tag of what you need first
strong = parent.find ("strong")
print(strong.string)