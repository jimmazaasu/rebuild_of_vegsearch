import pytesseract
from PIL import Image
import os
from gtts import gTTS
import sys

import importlib
#import sys
import json

# Check if the file exists, if not create it
try:
    with open('nonos_actualizados.txt', 'r') as f:
        read_file = f.read()
except FileNotFoundError:
    # If the file doesn't exist, create it by opening in 'w' mode
    with open('nonos_actualizados.txt', 'w') as f:
        pass  # Just create the file, no need to write anything



ingredientes_animales=[ "carne", "carne vacuna","vacuna","huevo", "queso", "dulce de leche", "Dulce de Leche","miel de abeja", "manteca", "pollo","cerdo", "pescado", "cordero","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "salmón","leche", "lácteo", "lácteos", "cangrejo", "jamón", "panceta", "mejillones","berberechos","anchoas","pulpo","calamar","tocino","foie gras","medallon de lomito","medallón de lomito", "carne molida", "medallones de lomito","lomito", "ojo de bife", "carne vacuna", "carne de vacuno","pata de pollo","carne de oveja", "leche en polvo","dulce de leche", "Dulce De Leche", "Dulce de Leche", " Dulce de Leche", "manjar blanco","carne","vacuna","vacuno","huevo", "huevo de codorniz","queso", "muzzarella", "mozzarella", "queso mozzarella", "queso sardo", "queso azul", "queso roquefort","queso de cabra", "queso fontina", "burrata", "mascarpone", "queso mascarpone", "requeson", "requesón", "yema de huevo", "clara de huevo", "miel de abeja", "manteca", "pollo", "pechuga de pollo", "presa de pollo","cerdo", "pescado","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "chorizo","leche", "lácteo", "suero de leche", "lácteos", "cangrejo", "jamón", "jamon", "jamón de pavo", "jamon de pavo", "pavo ahumado", "jamón crudo", "jamon crudo", "jamón serrano", "jamon serrano", "jamon de tipo serrano", "jamón de tipo serrano",  "panceta", "tocino", "grasa bovina", "grasa de cerdo","mejillones", "berberechos", "pulpo","surubí","calamar" "pescado", "pescados", "anchoas", "sardinas", "gelatina", "pato", "caviar", "atún", "atun", "kanikama", "leche condensada", "crema de leche"]

#ing_animales_mayuscula= []
#ing_animales_titlecase=[]
offending_ingredients=[]
carnes=["foie gras","medallon de lomito", "medallón de lomito","lomito","carne molida","ojo de bife", "carne vacuna","pollo","presa de pollo" "pechuga de pollo","carne de vacuno","cerdo","pata de pollo","carne de oveja", "pescado","mariscos", "langostinos", "camarones", "camarón","pavo", "jamón de pavo", "pavo ahumado", "salchichas", "chorizo", "cangrejo", "jamón", "jamon","panceta", "tocino", "grasa bovina", "grasa de cerdo","mejillones", "berberechos", "pulpo", "pescado", "pescados", "anchoas", "sardinas", "pechuga de pollo","gelatina", "jamon crudo", "pato", "caviar", "atún", "atun", "kanikama","jamón serrano", "jamon serrano","jamon de tipo serrano", "jamón de tipo serrano","surubí","calamar"]
egg_ok=[ "carne", "carne vacuna","vacuna", "queso", "dulce de leche", "Dulce de Leche","miel de abeja", "manteca", "pollo","cerdo", "pescado", "cordero","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "salmón","leche", "lácteo", "lácteos", "cangrejo", "jamón", "panceta", "mejillones","berberechos","anchoas","pulpo","calamar","tocino","foie gras","medallon de lomito","medallón de lomito", "carne molida", "medallones de lomito","lomito", "ojo de bife", "carne vacuna", "carne de vacuno","pata de pollo","carne de oveja", "leche en polvo","dulce de leche", "Dulce De Leche", "Dulce de Leche", " Dulce de Leche", "manjar blanco","carne","vacuna","vacuno","queso", "muzzarella", "mozzarella", "queso mozzarella", "queso sardo", "queso azul", "queso roquefort","queso de cabra", "queso fontina", "burrata", "mascarpone", "queso mascarpone", "requeson", "requesón",  "miel de abeja", "manteca", "pollo", "pechuga de pollo", "presa de pollo","cerdo", "pescado","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "chorizo","leche", "lácteo", "suero de leche", "lácteos", "cangrejo", "jamón", "jamon", "jamón de pavo", "jamon de pavo", "pavo ahumado", "jamón crudo", "jamon crudo", "jamón serrano", "jamon serrano", "jamon de tipo serrano", "jamón de tipo serrano",  "panceta", "tocino", "grasa bovina", "grasa de cerdo","mejillones", "berberechos", "pulpo","surubí","calamar" "pescado", "pescados", "anchoas", "sardinas", "gelatina", "pato", "caviar", "atún", "atun", "kanikama", "leche condensada", "crema de leche"]
# Write the list to the file in JSON format
with open('nonos_actualizados.txt', 'a') as f:
    json.dump(ingredientes_animales, f)  # Write the list in JSON format
    f.write('\n')  # Add a newline for readability


#for i in ingredientes_animales:

 # ing_animales_mayuscula.append(i.upper()) #agrega cada uno de los elementos de la lista ingredientes_animales a la lista ing_animales_mayuscula, pero con todos los caracteres convertidos en mayusculas

#for i in ingredientes_animales:  
#  ing_animales_titlecase.append(i.title())
#print (ing_animales_mayuscula)
#print(ing_animales_titlecase)

#with open('nonos_actualizados.txt', 'a') as f:
 #   json.dump(ing_animales_mayuscula, f)  # Write the list in JSON format
 #   f.write('\n')  # Add a newline for readability

#with open('nonos_actualizados.txt', 'a') as f:
#    json.dump(ing_animales_titlecase, f)  # Write the list in JSON format
#    f.write('\n')  # Add a newline for readability



def create_product_list_string():


   image_file= input("Please enter a filename for a picture of the ingredient list/Introduci un nombre para la foto: ")
#AQUI A LO MEJOR HABRIA QUE HACER QUE EL INPUT SEA EL DEL BOTON "AÑADIR ARCHIVO"
   #image_file=vegsearchGUI.get_file_name()
#added_text.value= "Agregaste el archivo " + new_ingredient_list.value

#new_ingredient_list = TextBox(app, width=30)



   img=Image.open(image_file) #abre la imagen escaneada para después convertirla en string
#img=Image.open(added_text.value)

   product_list=pytesseract.image_to_string(img) #product_list = esta va a ser la lista de ingredientes escaneada del envase y convertida en texto

   return product_list





def format_step1():

   product_list=create_product_list_string() #esta funcion sale del archivo de vegsearch 2 linea 25
   if "," in product_list:
      product_list=product_list.split(sep=",")  #convierte el string de la lista de ingredientes en una lista de strings separados por la coma
   elif "-" in product_list:
      product_list=product_list.split(sep="-") #si hay guiones en lugar de comas, separa la lista de ingredientes usando los guiones
   if ":" in product_list[0]:
      product_list[0]= product_list[0].split(":") #separa la primera palabra del primer elemento de la lista (usualmente es la palabra "ingredientes" del primer ingrediente usando los dos puntos como separador si están presentes

    #  print(product_list[0])

      product_list[0]=product_list[0][1] #redefine el primer elemento de la lista como el segundo elemento de la lista que se obtuvo en el paso anterior con split
      print(product_list[0])
   elif "\n" in product_list[0]: #si los dos puntos no están presentes en el primer elemento pero hay un newline, utiliza esto para separar los componentes
      product_list[0]= product_list[0].split("\n")
      product_list[0]=product_list[0][1]
   #print(product_list[0]) #VER POR QUÉ NO ESTÁ IMPRIMIENDO ESTE ELEMENTO EN EL SEGUNDO EJEMPLO DE PRUEBA
      print(product_list[0])
   return product_list

#print(format_step1())

def format_step2():

      product_list=format_step1()
      product_list_2=[]  #crea una nueva lista vacía que será la lista formateada
      for ingredient in product_list:
           ingredient=ingredient.strip()

           product_list_2.append(ingredient)
      return product_list_2
#print(format_step2())

#def format_step3():
#     product_list=format_step2()
#     product_list_3=[]
#     for ingredient in product_list:            #por cada ingrediente en la lista original de ingredientes...
 #          ingredient=ingredient.replace("\n"," ")  #reemplaza los newline characters por un espacio
#           product_list_3.append(ingredient)        # y agrega cada ingrediente a la nueva lista creada recién (porque las listas son inmutables y no se puede modificar la original
    # return product_list_3

#print(format_step3())


def check():
  #product_list = esta va a ser la lista de ingredientes escaneada del envase y convertida en texto
 #  img=Image.open("ingredient_list1.jpeg")
#la linea 5 entonces no queda redundante? 
 #  product_list=pytesseract.image_to_string(img)

    product_list=format_step2()
   
    for ingredient in product_list:
        if ingredient.lower() in ingredientes_animales:
            offending_ingredients.append(ingredient.lower())
    if len(offending_ingredients)>0:
        return "Este producto contiene: {0}".format(offending_ingredients),"no es vegano"

    #  print("NO es vegano")
    
    return "Este producto es vegano"
#print(check())


#hay un problema con este for loop. El print statment probablemente tiene que estar por fuera

def text_to_speech(text):
   #Initialize gTTS with the text to be converted
  # text=check()
   speech=gTTS(text, lang= "es")
   #Save the audio file in a temporary file
   speech_file="speech.mp3"
   speech.save(speech_file)
   #Play the audio file
   os.system("reproductor multimedia"+speech_file)
   # Play the audio file using the appropriate command for your OS
   if os.name == 'nt':  # Windows
       os.system("start speech.mp3") 
   elif os.name == 'posix':  # Linux or macOS
       os.system("afplay speech.mp3") 
   else:
       print("Unsupported OS. Cannot play audio")


#text_to_speech("Hola mundo. Esta es una segunda prueba")

###comentar desde acá si no funciona###

def add_ingredient():
    lista_agregados=[]
    agregar=input("¿Queres agregar algo a la lista de ingredientes a evitar?, Responde con Sí o No: ")
    
    if not agregar.lower()=="no":
        ingredient=input("Introduci el nombre del ingrediente que queres agregar, acordate que debe ser un ingrediente de origen animal: ")
        #acordate de incluir una opcion para agregar listas de ingredientes y no solo ingredientes individuales
        if ingredient not in ingredientes_animales: #Si el ingrediente no está en la lista de ingredientes animales...
            lista_agregados.append(ingredient) #lo agrega a la lista vacía de ingredientes a agregar
            ingredientes_animales.extend(lista_agregados) #y combina esta lista de ingredientes a agregar con la lista de ingredientes animales que teniamos al comenzar
            return "ingrediente agregado" #luego te pone esta frase
        else: # si el ingrediente ya está en la lista 
           return "ese ingrediente ya está en la lista" #escribe esto
    else:
       return "Gracias!"
text_to_speech(str((check()))) #convierte el resultado de la verificacion de ingredientes en audio

print(add_ingredient())
#print(ingredientes_animales)

#parece que hay que guardar la lista en un archivo a medida que se va modificando, para que se vayan guardando los cambios,
#de lo contrario solo se agrega la primera vez a la lista original pero después no quedan


 
# Save the original stdout
original_stdout = sys.stdout
 
# Redirect stdout to a file
with open('nonos_actualizados.txt', 'r') as f: #por qué tres veces open??? (23/vi/2025)
    read_file = f.read()   #30/vi/2025 (el problema se soluciono al leer el archivo en modo "r" en la linea anterior)
    sys.stdout = f #aparentemente, con estas tres lineas abris en modo append para poder agregar elementos, lo lees y guardas lo de la consola en el archivo...confirmar
    
 #   print(ingredientes_animales)
with open('nonos_actualizados.txt', 'r') as f:
    read_file = f.read()

with open('nonos_actualizados.txt', 'a') as f:
    sys.stdout = f
    print(ingredientes_animales)

# Reset sys.stdout to its original state
import sys
sys.stdout = sys.__stdout__   #al comentar esta linea y la anterior sale error (30/vi/2025)

#activate_vegsearch=foo()    

    # ahora está agregando correctamente los ingredientes que le pido que agregue pero cuando intente agregar "cuy" (que ya está en la lista)
    # no me dice que está repetido, parece que lo sobreescribe

    #creo que lo que tengo que hacer para que realmente haga los cambios al ir agregando, tengo que ir leyendo el archivo
    # Open the file in read mode

###revisar lo de abajo de nuevo###
#recorda que tenes que reemplazar \ por / en el path para que no haya error, o bien usar \\ o r antes del path
file_path = 'C:\\Users\\Mabel Zacur\\Desktop\\rebuild_of_vegsearch\\nonos_actualizados.txt'
 # agregar r y / no esta funcionando, probar \\

 #10/vii/2025: probe con \\ pero no funciono, invoca el error como dice en la linea 244 y dice 'not readable'
try:
    with open(file_path, 'a+') as file:
        # Read the content of the file
        file_content = file.read()
         
        # Print the content
        print("File Content:\n", file_content)

        
 
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
#except Exception as e:
 #   print(f"An error occurred: {e}")

except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")
