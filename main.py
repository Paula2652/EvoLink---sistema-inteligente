import customtkinter as ctk
from tkinter import messagebox

from login import mostrar_login

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("EvoLink - Suporte Técnico")
janela.geometry("750x550")
janela.minsize(650, 450)


# Funções de navegação
def abrir_login():
    mostrar_login(janela, abrir_menu)


def abrir_menu():
    # Próxima etapa do trabalho: aqui vai a tela do menu principal.
    # Por enquanto, só confirma que o login funcionou.
    messagebox.showinfo(
        "EvoLink",
        "Login realizado com sucesso!\n\nO menu principal será a próxima tela."
    )


# Abrir a tela inicial
abrir_login()

janela.mainloop()
