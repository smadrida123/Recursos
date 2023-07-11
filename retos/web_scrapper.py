import requests

from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.futbolred.com/futbol-colombiano/liga-betplay/millonarios-tendra-al-joven-ecuatoriano-sebastian-del-castillo-firmo-hasta-2026-184257"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

ls=[]
# Extract information from the HTML
product_titles = soup.select(".product-title")
response = requests.get(url)

for link in soup.find_all("a"):
    y=link.get("href")
    y=str(y)
    if "http" in y:
        ls.append(y)

print(ls)



"""
#select por nombre de etiqueta
product_reviews = soup.select("li")
#seleccion por nombre de clase
product_ratings = soup.select(".reconsumo-titular")
#selecion por ID
#product_prices = soup.select("#")



# Iterate over the extracted data and print it
for i in range(len(product_ratings)):
    
    title = product_titles[i].text.strip()
    price = product_prices[i].text.strip()
    
    rating = product_ratings[i].text.strip()
  
    review = product_reviews[i].text.strip()
    print("Select", review)
    print("Select por nombre de clase", rating)


    print("Title:", title)
    print("Price:", price)

print("--------------------")
"""
