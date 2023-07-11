from bs4 import BeautifulSoup
import requests

url="https://www4.sincoerp.com/SincoConsGalias_Nueva/V3/Marco/Login.aspx"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

#imprime elemento pagina como string y mas leible
print(soup.prettify())

##Para navegar estructura
#extraer titulo
print(soup.title.string)

#extrae etiqueta "p"
print(soup.p)

#extraer URLS en texto
ls=[]
for link in soup.find_all("a"):
    y=link.get("href")
    y=str(y)
    if "http" in y:
     ls.append(y)

print(ls)

#extraer texto
#print(soup.get_text())


##Para navegar por tags
#Tag en documento HTML original
tag=soup.footer
#el nombre del tag se puede cambiar tag.name="nombre_nuevo"
print(type(tag),tag.name)

#un tag tiene atributos
print(tag.attrs)
#se pueden borrar, adicionar, remover y modificar como si fuera diccionario
tag["name"]="buena_la_avena"
print(tag)

#atributos multivaluados. Mas comun: class
#print(soup.a["class"])
#obtener todos los atributos
#print(soup.p.get_attribute_list("input"))

##Para navegar en strings
tag.string  #es de tipo NavigableString
print(str(tag.string))#tipo str
#replace_with("texto a reemplazar")


