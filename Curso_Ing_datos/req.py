import requests

#al llamar el metodo get se obtiene un objeto response
response=requests.get("http://www.platzi.com/cursos")
response.encoding="utf-8"
#info en jupiter response? codigo fuente en jupyter response??
#response??
#para saber que metodos se pueden usar para este objeto
#print(dir(response))
#print(response.status_code)
#print(response.headers)
#obtener texto de respuesta: ej html,js y css
#print(response.text)
import bs4
#se selecciona parser de html
soup=bs4.BeautifulSoup(response.text,"html.parser")
#se accede a atributos,titulo
#print(soup.title.text,soup.select("meta[name=description]")[0]["content"])
link_cursos=soup.select(".Course")
cursos=[e["href"] for e in link_cursos]
for i in cursos:
    print(i)
