from pizza import Pizza

#imprimir el menú de ingrediente
print("---Menú de Ingredientes---\n")
print(f"Tipos de Masa : {Pizza.tipos_masa} ")
print(f"Ingredientes Proteicos : {Pizza.proteicos}")
print(f"Ingredientes Vegetales : {Pizza.vegetales}")
print(f"Precio = {Pizza.precio}\n")

#verificar si el elemento 'salsa de tomate' está presente en la lista de ingredientes
print(f"El elemento salsa de tomate {'si' if Pizza.validar('salsa de tomate', ['salsa de tomate', 'salsa bbq']) else 'no'} se encuentra presente en la lista\n ")

#crear una instancia de la clase Pizza y luego llamar al metodo .pedido para solicitar un pedido
solicitud_pizza = Pizza()
solicitud_pizza.pedido()

#imprimir los ingredientes seleccionados por el usuario y validar la solicitud
print(f"Los ingredientes seleccionados son:\n"
      f"- Tipo de masa: {solicitud_pizza.masa}\n"
      f"- Proteico: {solicitud_pizza.proteico_1}\n"
      f"- 1° Vegetal: {solicitud_pizza.vegetal_1}\n"
      f"- 2° Vegetal: {solicitud_pizza.vegetal_2}\n"
      f"La solicitud de la Pizza {'es' if solicitud_pizza.validacion else 'no es'} válida\n\n")


# Acceder al atributo de clase directamente sin instanciar,esto arrojara un error
if Pizza.validacion:
    print("La clase Pizza representa una pizza válida.")
else:
    print("La clase Pizza no representa una pizza válida.")