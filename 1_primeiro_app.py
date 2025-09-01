# Primeiro programa desenvolvido em Python

import flet as ft

def main(page: ft.Page):

    #Configurações básicas
    page.tittle = "Meu primeiro App Flet"
    page.padding = 20

    meu_texto = ft.Text(
        value = "Hello World!",
        size = 24,
        color = ft.Colors.PINK,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER    
    )

    page.add(meu_texto)

    page.add(
        ft.Text("Bem-Vindo(a) ao mundo do desenvolvimento Mobile!😍",
        size=16),
        ft.Text("Com Flet, você pode criar apps incríveis!📱",
        size=16, color=ft.Colors.BLUE)
    )

ft.app(target=main)