

#Imports
import main
from guizero import App, Picture, PushButton, Text, TextBox

#import vegsearch2
#from Nonos import Nonos

#ingredientes_animales=Nonos(["carne", "carne vacuna","vacuna","huevo", "queso", "dulce de leche", "Dulce de Leche","miel de abeja", "manteca", "pollo","cerdo", "pescado", "cordero","mariscos", "langostinos", "camarones", "camarón","pavo", "salchichas", "salmón","leche", "lácteo", "lácteos", "cangrejo", "jamón", "panceta", "mejillones","berberechos","anchoas","pulpo","calamar","tocino"])

#animal_ingredients=Nonos(["meat", "beef","egg","cheese","honey","butter","chicken","poultry","pork","fish","seafood","shrimp","lobster","prawn","prawns","turkey","lamb","sausage","milk", "dairy", "crab", "ham", "bacon", "mussel", "mussels", "anchovies","salmon", "octopus", "squid"])

#Functions

def check():

 text_respuesta.value= "" + str(main.check()
 print (text_respuesta.value)

def get_file_name():
     text.value="Agregaste el archivo:  " + new_ingredient_list.value
     #print("archivo agregado")
    
   
#App

app=App(title="VEGQUEST")    #Creates the app container? (check this later)

#Widgets
message=Text(app, text="Bienvenid@ a VEGQUEST") #creates text widget
paraque_msg=Text(app, text="VEGQUEST lee una etiqueta por vos y te dice si el producto es vegano o no") #creates another text widget
vegan_logo=Picture(app, image="vegan.png", align="top")  #adds image

#vegan_logo.image=25

paraque_msg.text_size=25  #sets text size
paraque_msg.font="impact" #sets font
prompt=Text(app, text="")
text = Text(app, text="Escribí el nombre de archivo donde guardaste la foto de la etiqueta y presioná el botón")
button_add_file=PushButton(app, get_file_name, text="AÑADIR ARCHIVO", align="top") #adds a PushButton to add a file name
new_ingredient_list = TextBox(app, width=35)

#def bar ():
button=PushButton(app, main.check, text="¿ES VEGANO?", align="top") #adds a PushButton #por que al poner el codigo para este boton despues del otro no aparece?
#button_add_file=PushButton(app, get_file_name, text="AÑADIR ARCHIVO", align="top") #adds a PushButton to add a file name
#text = Text(app, text="Escribí el nombre de archivo donde guardaste la foto de la etiqueta y presioná el botón")

#new_ingredient_list = TextBox(app, width=35)
#button=PushButton(app, check, text="ES VEGANO?", align="top") #adds a PushButton


   

text_respuesta = Text(app, text="")

#button_add_song = PushButton(app, add_song, text="Add song")
button_add_file.bg="blue"
button_add_file.text_color="yellow"
button_add_file.text_size=20

button.bg="#D72014 " 
button.text_color="yellow"
button.text_size=25
image_credit=Text(app, text="Ícono diseñado por freepik.com y descargado de flaticon.com",align="bottom")


#app.bg= "red"#"#EEECA9 " #sets background color with corresponding hex code selected from https://htmlcolorcodes.com/
#Display
app.display()  #displays GUI



