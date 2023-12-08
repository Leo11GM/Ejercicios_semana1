cadena1 = "Hola,Leonardo,cómo,estás"
cadena2 = "Bienvenido"

#Método = dato.método()

#upper: convierte todo a mayúsculas
resultado = cadena1.upper()

#upper: convierte todo a minúsculas
resultado = cadena1.lower()

#capitalize: solo primer letra en mayúscula
resultado = cadena1.capitalize()

#find: buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("o")

#index: buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepción
busqueda_index = cadena1.index("o")

#si es numérico devuelve True, si no es numérico devuelve False
es_numerico = cadena1.isnumeric()

#isalpha: si es alfanumérico devuelve True, sino devuelve False
es_alfanumerico = cadena1.isalpha()

#count: buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o")

#len: contamos cuántos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#startswith: verifica si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("H")

#endswith: verifica si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("a")

#remplace: remplaza un pedazo de la cadena dada, por otra dada, si no encuentra coincidencias, devuelve la original
cadena_nueva = cadena1.replace("Hola" , "Hola me llamo Leonardo")

#split: separa cadenas que le pasemos, creando una lista
cadena_sepearada = cadena1.split(",")
print(cadena_sepearada)




