import pytesseract
from PIL import Image
import os
from gtts import gTTS
import sys


ingredientes_animales=["dulce de leche", "Dulce De Leche", "Dulce de Leche", " Dulce de Leche", "manjar blanco","carne","vacuna","vacuno","huevo", "queso", "yema de huevo", "clara de huevo" "miel de abeja", "manteca", "pollo","cerdo", "pescado","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "leche", "lácteo", "lácteos", "cangrejo", "jamón", "panceta", "tocino", "grasa bovina", "mejillones", "berberechos", "pulpo" "pescado", "pescados", "anchoas", "sardinas", "gelatina", "pato", "caviar", "atún", "atun", "kanikama", "leche condensada", "crema de leche"]

ing_animales_mayuscula= []
ing_animales_titlecase=[]
offending_ingredients=[]

for i in ingredientes_animales:

  ing_animales_mayuscula.append(i.upper()) #agrega cada uno de los elementos de la lista ingredientes_animales a la lista ing_animales_mayuscula, pero con todos los caracteres convertidos en mayusculas

for i in ingredientes_animales:   
  ing_animales_titlecase.append(i.title())
#print (ing_animales_mayuscula)
#print(ing_animales_titlecase)
def create_product_list_string():


   image_file= input("Please enter a filename for a picture of the ingredient list/Introduci un nombre para la foto: ")

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
    if ingredient in ingredientes_animales or ingredient in ing_animales_mayuscula or ingredient in ing_animales_titlecase:
      offending_ingredients.append(ingredient)
   if len(offending_ingredients)>0:
     return "Este producto contiene: {0}".format(offending_ingredients),"no es vegano"
    
    #  print("NO es vegano")
   else:
     return "Este producto es vegano"
   return resultado
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

    if agregar=="No":
        return "Gracias"
    else:
        ingredient=input("Introduci el nombre del ingrediente que queres agregar, acordate que debe ser un ingrediente de origen animal: ")
#acordate de incluir una opcion para agregar listas de ingredientes y no solo ingredientes individuales
        if ingredient not in ingredientes_animales: #Si el ingrediente no está en la lista de ingredientes animales...
            lista_agregados.append(ingredient) #lo agrega a la lista vacía de ingredientes a agregar
            ingredientes_animales.extend(lista_agregados) #y combina esta lista de ingredientes a agregar con la lista de ingredientes animales que teniamos al comenzar
            return "ingrediente agregado" #luego te pone esta frase
        else: # si el ingrediente ya está en la lista 
           return "ese ingrediente ya está en la lista" #escribe esto
text_to_speech(str((check()))) #convierte el resultado de la verificacion de ingredientes en audio

print(add_ingredient())
#print(ingredientes_animales)

#parece que hay que guardar la lista en un archivo a medida que se va modificando, para que se vayan guardando los cambios,
#de lo contrario solo se agrega la primera vez a la lista original pero después no quedan


 
# Save the original stdout
original_stdout = sys.stdout
 
# Redirect stdout to a file
with open('nonos_actualizados.txt', 'a') as f:
    sys.stdout = f
    
    print(ingredientes_animales)

    

    # ahora está agregando correctamente los ingredientes que le pido que agregue pero cuando intente agregar "cuy" (que ya está en la lista)
    # no me dice que está repetido, parece que lo sobreescribe

    #creo que lo que tengo que hacer para que realmente haga los cambios al ir agregando, tengo que ir leyendo el archivo
    # Open the file in read mode

###revisar lo de abajo de nuevo###
#recorda que tenes que reemplazar \ por / en el path para que no haya error, o bien usar \\ o r antes del path
#file_path = 'C:\\Users\\Mabel Zacur\\Desktop\\rebuild_of_vegsearch\\nonos_actualizados.txt'
 # agregar r y / no esta funcionando, probar \\
#try:
#    with open(file_path, 'a') as file:
        # Read the content of the file
#        file_content = file.read()
         
        # Print the content
 #       print("File Content:\n", file_content)

        
 
#except FileNotFoundError:
 #   print(f"File '{file_path}' not found.")
#except Exception as e:
#    print(f"An error occurred: {e}")