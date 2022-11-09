def get_population(country_dict):
  population_dict={
    "2022":int(country_dict["2022 Population"]),
    "2020":int(country_dict["2020 Population"]),
    "2015":int(country_dict["2015 Population"]),
    "2010":int(country_dict["2010 Population"]),
    "2000":int(country_dict["2000 Population"]),
    "1990":int(country_dict["1990 Population"]),
    "1980":int(country_dict["1980 Population"]),
    "1970":int(country_dict["1970 Population"])
  }
  labels=population_dict.keys()
  values=population_dict.values()
  return labels,values

def population_by_countries(data,country):
  result=list(filter(lambda item:item["Country/Territory"]==country,data))
  return result

#sacar lista de paises, sacar lista de valores World Population Percentage
def population_percentage(data):
  countries=[]
  pop_perc=[]
  for x in data:
    countries.append(x["Country/Territory"])
    pop_perc.append(x["World Population Percentage"])
  datos=list(zip(countries,pop_perc))
  resul={countries:pop_perc for (countries,pop_perc) in datos}
  labels2=resul.keys()
  values2=resul.values()
  return labels2,values2
