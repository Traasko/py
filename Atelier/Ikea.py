import requests
from bs4 import BeautifulSoup

class IkeaCouchScraper:
    def __init__(self):
        self.base_url = "https://www.ikea.com"
        self.meubles_url = "/fr/fr/cat/canapes-fu003/"

    def fetch_couches_data(self):
        url = self.base_url + self.meubles_url
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            couches = []

            for product in soup.find_all("div", class_="product-compact"):
                price = product.find("span", class_="product-compact__price__value").text
                name = product.find("span", class_="product-compact__name").text
                rating = product.find("span", class_="product-compact__rating__stars")["style"]
                seats = product.find("div", class_="product-compact__seats").text.strip()
                comfort_type = product.find("div", class_="product-compact__comforts").text.strip()

                couch_data = {
                    "price": price,
                    "name": name,
                    "rating": rating,
                    "seats": seats,
                    "comfort_type": comfort_type
                }
                couches.append(couch_data)

            return couches
        else:
            print("Error fetching data from Ikea website")
            return []

# Utilisation de la librairie
if __name__ == "__main__":
    scraper = IkeaCouchScraper()
    couches = scraper.fetch_couches_data()

    for couch in couches:
        print("Nom:", couch["name"])
        print("Prix:", couch["price"])
        print("Note des avis:", couch["rating"])
        print("Nombre de places:", couch["seats"])
        print("Type de confort:", couch["comfort_type"])
        print("=" * 40)
