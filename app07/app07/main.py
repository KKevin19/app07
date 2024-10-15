import flet as ft
import random

def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario==numero_secreto:
        texto_resultado.value="¡felicidades! adivinaste el numero secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="Victoria.mp3",autoplay=True))
        imagen.src="Feliz.png"
    
    elif adivinanza_usuario < numero_secreto:
        texto_resultado.value="¡fallaste! el numero secreto es mayor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
        imagen.src="triste.png"
    else:
        texto_resultado.value="¡fallaste! el numero secreto es menor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
        imagen.src="triste.png"
    entrada_numero.value=""
    page.update()    


#funcion principal
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar,imagen
    
    page.title="adivina el numero"
    
    #generar un numero aleatorio
    numero_secreto=random.randint(1,100)
    
    #crear elementos de la interfaz
    titulo=ft.Text("adivina el numero entre 1 y 100",size=20,color="red")
    entrada_numero=ft.TextField(label="tu adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar", on_click=lambda e: verificar_adivinanza(e, page))
    texto_resultado=ft.Text("",color="red")
    imagen=ft.Image(
        src="https://i.ibb.co/Gxgryg9/laser.gif",
        fit=ft.ImageFit.COVER,
        width=350,
        height=300)

    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                imagen
            ],alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        bgcolor="blue",
        width=page.window.width,
        height=page.window.height,
        padding=20
            
        
    )
    page.add(contenedor_principal)


ft.app(main)
