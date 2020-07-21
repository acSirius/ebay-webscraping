import requests
from bs4 import BeautifulSoup

URL = 'https://www.ebay.ie/itm/Gigabyte-GeForce-RTX-2080-Ti-Gaming-OC-RGB-82-mm-Triple-Fan-Graphics-Card-11GB/184253686145?hash=item2ae6602181:g:kgYAAOSw5JFelinB'

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')

price_str = soup.find(id='prcIsum').get_text()

def remove_comma(): # We need to remove comma from the price string to be able to convert it into a float, we also need to remove any characters such as £ or EUR
    price_digits = ''
    for i in price_str:
        if i.isdigit() or i == '.':
            price_digits += i

    price = float(price_digits)
    return price

price = remove_comma() # This is now the price as a float

print(price)

desired_price = float(input('How much are you willing to pay for this product?  '))

if price > desired_price:
    print(f'Sorry, but it is too expensive. Current price of {price}')
else:
    print(f'Good news! You can now buy the product for the desired price of or under! {price} ')
