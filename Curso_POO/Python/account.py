#Para python. Nombre de archivo en minuscula y primera letra de nombre de clase mayuscula
class Account:
     id=int
     name=str
     document=str
     email=str
     password=str

     def __init__(self,name,document):
          self.name=name
          self.document=document