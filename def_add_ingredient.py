def add_ingredient():
    lista_agregados=[]
    agregar=input("¿Queres agregar algo a la lista de ingredientes a evitar?, Responde con Sí o No: ")

    if agregar=="No":
        return "Gracias"
    else:
        ingredient=input("Introduci el nombre del ingrediente que queres agregar, acordate que debe ser un ingrediente de origen animal")
#acordate de incluir una opcion para agregar listas de ingredientes y no solo ingredientes individuales
        if ingredient not in ingredientes_animales:
            lista_agregados.append(ingredient)
            ingredientes_animales.extend(lista_agregados)



#también es importante agregar variantes regionales de ciertos nombres de ingredientes, al menos si las conoces
            
#def add_translation():
    translation=input("Para agregar el equivalente de un ingrediente en otro idioma, introducilo aquí:")

    #habria que encontrar una forma de convertir el input en un diccionario con el equivalente del ingrediente en el idioma en cuestion
    #base de datos??

