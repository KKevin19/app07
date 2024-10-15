import flet as ft
import random

def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario==numero_secreto:
        texto_resultado.value="¡felicidades! adivinaste el numero secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="victoria.mp3",autoplay=True))

    elif adivinanza_usuario < numero_secreto:
        texto_resultado.value="¡fallaste! el numero secreto es mayor"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))
    else:
        texto_resultado.value="¡fallaste! el numero secreto es menor"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))
        
    entrada_numero.value=""
    page.update()    


#funcion principal
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title="adivina el numero"
    
    #generar un numero aleatorio
    numero_secreto=random.randint(1,100)
    
    #crear elementos de la interfaz
    titulo=ft.Text("adivina el numero entre 1 y 100",size=20,color="red")
    entrada_numero=ft.TextField(label="tu adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar", on_click=lambda e: verificar_adivinanza(e, page))
    texto_resultado=ft.Text("",color="red")
    import flet as ft
import random

def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario==numero_secreto:
        texto_resultado.value="¡felicidades! adivinaste el numero secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="victoria.mp3",autoplay=True))

    elif adivinanza_usuario < numero_secreto:
        texto_resultado.value="¡fallaste! el numero secreto es mayor"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))
    else:
        texto_resultado.value="¡fallaste! el numero secreto es menor"
        page.add(ft.Audio(src="boing.mp3",autoplay=True))
        
    entrada_numero.value=""
    page.update()    


#funcion principal
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title="adivina el numero"
    
    #generar un numero aleatorio
    numero_secreto=random.randint(1,100)
    
    #crear elementos de la interfaz
    titulo=ft.Text("adivina el numero entre 1 y 100",size=20,color="red")
    entrada_numero=ft.TextField(label="tu adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar", on_click=lambda e: verificar_adivinanza(e, page))
    texto_resultado=ft.Text("",color="red")
    imagenes=ft.Image(
        src="https://i.ibb.co/Gxgryg9/laser.gif",
        fit=ft.ImageFit.COVER,
        width=350,
        height=200)
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                imagenes
            ],alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        bgcolor="green",
        width=page.window.width,
        height=page.window.height,
        padding=20
            
        
    )
    page.add(contenedor_principal)

ft.app(main)