#Proyecto Integrador
import random 

#Decorador: En este fragmento se define el decorador
def reg_intentos(func): #Se usa una función genérica para volver a usar el decorador, si es necesario
    def wrapper(*args, **kwargs):
        print("Bienvenido/a")
        resultado = func(*args, **kwargs) #Se llama a nuestra función de juego
        print("Juego finalizado. ¡Gracias por jugar! 🎉")
        return resultado
    return wrapper

#Generador de palabras (Lo definimos)
def gen_palabras(lista_palabras):
    while True:
        yield random.choice(lista_palabras)

@reg_intentos #Se usa el decorador en nuestra función jugar
def jugar(palabras=None, **kwargs): #Los kwargs indican que puede haber más parámetro a colocar.
    if palabras is None: #Si el usuario no agrega una lista de palabras, las palabras por defalt serán "palabras":
        palabras = ["programacion", "escuela", "computadora", "github", "python", "java", "codigo", "estudiar"]
    palabra_gen = gen_palabras(palabras)
    vidas_i = kwargs.get("vidas", 5) #Se obtiene el valor de kwargs. Si el usuario no puso nada, su valor default es 5. 
    c_vidas = "💚"*vidas_i #Se agregan la cantidad de corazones correcpondientes a las vidas que puso el usuario, o el default.
    while True:
        palabra_sec = next(palabra_gen)
        l = len(palabra_sec)
        palabra_oc = ["_"]* l
        palabra_unida = "".join(palabra_oc)
        vidas = vidas_i #Aquí se vuelven a llenar las vidas si el usuario elige volver a jugar.
        
        ##Comienza el juego
        print("Comienza el juego 👀🦑")
        print(palabra_unida)
        print(f"La palabra oculta tiene {l} letras")
        print(f"Comienzas con {vidas} vidas {c_vidas}") 

        while "_" in palabra_oc and vidas > 0:  # Mientras que no se acaben los espacios en blanco y nos sigan quedando vidas, el juego continua.
            letra = input("Ingrese una letra: ").lower().strip()
            #Validación de entrada
            while not (len(letra) == 1 and letra.isalpha()):
                letra = input("Su entrada es inválida. Ingrese una letra: ").lower().strip() #Sólo permitimos la entrada de un solo caracter alfabético a la vez

            if letra in palabra_sec: #Después que el usuario diga una letra, recorremos la palabra con un for in range
                for i in range(len(palabra_sec)):
                    if palabra_sec[i] == letra:
                        palabra_oc[i] = letra
                print("😍 Correcto, acertaste la letra") #Si le atina la palabra, aparece esto:
                print(f"Tienes {vidas} vidas {c_vidas}")
            else:
                print("La letra no se encuentra en la palabra. Vuelve a intentarlo") #Si no le atina, se le quita una vida
                vidas -= 1
                c_vidas = "💚"*vidas
            print("".join(palabra_oc)) #Se imprime el status de la palabra que se está adininando
            print(f"Te quedan {vidas} vidas {c_vidas}")

        #Fin del juego. Se evalúa si ya no quedan espacios en blanco. Si es así, lanza un mensaje que el usuario ha ganado
        if "_" not in palabra_oc:
            print("Ganaste el juego. ¡Felicidades! 🙌")
            print(f"La palabra secreta es {palabra_sec}")
        else: 
            print("Perdiste 😪 ")
            print(f"La palabra secreta era {palabra_sec}")
        while True: #Este while True sirve para preguntarle al usuario si quiere jugar de nuevo o no
            juego_nuevo = input("¿Quieres jugar nuevamente? S/N ").strip().lower()
            if juego_nuevo == "s":
                print("¡Genial! Juguemos nuevamente 🙌")
                break  # Sale del bucle y empieza una nueva partida
            elif juego_nuevo == "n":
                print("Gracias por jugar. Hasta la próxima 🥰")
                return  # Sale de la función y termina el juego
            else:
                print("Respuesta inválida. Por favor elije S o N.") #Hasta que el usuario ingrese algo válido (S/N), esto se seguirá ejecutando


#jugar(palabras=["comida", "juego", "moraleja", "mouse"], vidas=3)
jugar()
#jugar(vidas=4)