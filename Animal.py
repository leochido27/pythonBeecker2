class Animales():
    def __init__(self,nombre,edad,color):
        self.nombre= nombre
        self.edad = edad
        self.color = color

    def gatos(self,nombre,edad,color):
        print (f"el nombre es : {nombre}")
        print (f"la edad es : {edad}")
        print (f"el color es : {color}")

    def perros(self,nombre,edad,color):
        print (f"el nombre es : {nombre}")
        print (f"la edad es : {edad}")
        print (f"el color es : {color}")




firulais = Animales.perros(
    nombre="firulais",
    edad="4 años",
    color="negro"

)

            