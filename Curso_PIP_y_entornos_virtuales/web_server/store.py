import requests

def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    #viene en formato string
    print(r.text)
    #transformar en formato python
    categories=r.json()
    for category in categories:
        print(category["name"])