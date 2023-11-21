from django.shortcuts import render, get_object_or_404, redirect
from .models import Words
from django.contrib import messages
# Create your views here.
import random

def nuevo_juego(request):
    # Lista de palabras para el juego del ahorcado (puedes expandir esta lista según tus necesidades)
    items = ['python', 'django', 'javascript', 'html',  'git', 
             "reggae", "country", "electrónica", "clásica", "rap",
             "bmw", "audi", "volkswagen", "tesla", "hyundai"]
    #items = list(Words.objects.all())
    # Seleccionar una palabra al azar
    random_item = random.choice(items)
    
    palabra_nueva = Words.objects.create(palabra=random_item)
    # Redirigir al jugador a la página del juego recién creado
    return redirect('jugar', juego_letra=palabra_nueva.id)

def inicio(request):
    return render(request, "pages/nuevo_juego.html")


def jugar(request, juego_letra):
    juego = get_object_or_404(Words, pk=juego_letra)
    retornar = False
    
    if request.method == 'POST':
        letra_ingresada = request.POST.get('name', ' ').lower()
        # Verificar si la letra ya fue adivinada o si ya se agotaron los intentos
        if juego.intentos_restantes > 0:
            # Actualizar las letras adivinadas
            if letra_ingresada not in juego.palabra:   
                juego.intentos_restantes -= 1    
                juego.letras_incorrectas += letra_ingresada     
            else:
                juego.letras_adivinadas += letra_ingresada
            
            #Logica
            lista_ingresada = juego.letras_adivinadas + juego.letras_incorrectas
            lista_letras = list(lista_ingresada)
            visited = set()
            dup = {x for x in lista_letras if x in visited or (visited.add(x) or False)}
            # Validacion de si la palabra ya fue ingresada
            if letra_ingresada in dup:                   
                messages.add_message(request=request, level=messages.INFO, message="LA LETRA {} YA FUE INGRESADA".format(letra_ingresada.upper()))
            else:
                pass  
                
            #Verificar si el jugador ha ganado o perdido
            if all(letra in juego.letras_adivinadas for letra in juego.palabra):
                messages.add_message(request=request, level=messages.SUCCESS, message="ADIVINASTE LA PALABRA")
                retornar = True;
            elif juego.intentos_restantes == 0:
                # El jugador ha agotado todos los intentos, puedes manejar la lógica de derrota aquí
                messages.warning(request, message="NO ADIVINASTE LA PALABRA SERAS REDIRIGIDO")

            # Guardar los cambios en la base de datos
            juego.save()

    # # Renderizar la página del juego con la información actualizada
    return render(request, 'pages/juego.html', {"info": juego, "retornar": retornar})