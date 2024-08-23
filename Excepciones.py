#print("1/0")

numero_var = "hola"
try:
    print (int(numero_var))

except Exception as error:
    print (f"el valor recivido no es entero: {error}")


print ("hola mundo")