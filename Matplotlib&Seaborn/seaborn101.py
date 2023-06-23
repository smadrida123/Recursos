#estructurada para soportar dataframes de Pandas
import seaborn as sns
import matplotlib.pyplot as plt
#estructura basica
##tipo de grafica(datos,x,y,hue=variable de agrupamiento (opcional))
#set:comando para cambiar estilos. Afectando a todos los graficos
sns.set(style='whitegrid', palette='icefire', font="DejaVu Sans", font_scale=0.5)
sns.barplot(x=["A","B","C"],y=[1,3,2])
plt.show()