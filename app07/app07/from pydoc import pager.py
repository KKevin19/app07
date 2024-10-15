from pydoc import pager
import flet as ft

def main(page: ft.Page):
    page.title="¿me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="blue"
    
    lbl1=ft.Text("¿me perdnas?",
                style=ft.TextStyle(size=40,weight="bold"))
                                    
    img1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("si",
    color="green",
    width=100,
    height=50)
    
    btnNo=ft.ElevatedButton("No",
    color="red",
    width=100,
    height=50)
    
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
        
    def si(e):
        img1.src="feliz.png"
        page.undate()
        
   
    btnSi.on_click=si
    btnNo.on_click=no    
    
    
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.Row([btnSi,btnNo],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


ft.app(main)