#En este archivo se tendran las utilidades para el archivo runner.py

#Funcion que retorna info (lista de 1 dict) de pais según el input de capital pedido en runner
def capital_reader(data,capital):
    info=list(filter(lambda x:x["Capital"]==capital,data))
    return info

#Funcion que retorna diccionario con keys y values para graficar de años pais seleccionado
def pop_ages(country_dict):
    info={
        "1970":int(country_dict["1970 Population"]),
        "1980":int(country_dict["1980 Population"]),
        "1990":int(country_dict["1990 Population"]),
        "2000":int(country_dict["2000 Population"]),
        "2010":int(country_dict["2010 Population"]),
        "2015":int(country_dict["2015 Population"]),
        "2020":int(country_dict["1970 Population"]),
    }
    x=info.keys()
    y=info.values()
    return x,y

#Funcion para obtener valores de columna vs pais para graficar
def pop_perc(data):
        labels=list(map(lambda x:x["Country/Territory"],data))
        values=list(map(lambda x:x["World Population Percentage"],data))
        return labels,values




