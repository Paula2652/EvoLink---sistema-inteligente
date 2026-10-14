import customtkinter as ctk
from tkinter import messagebox

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"


def mostrar_login(janela, abrir_menu):

    # Remove os componentes da tela anterior
    for componente in janela.winfo_children():
        componente.destroy()

    janela.title("Login - EvoLink")

    # Cartão central
    cartao = ctk.CTkFrame(janela, corner_radius=16)
    cartao.place(relx=0.5, rely=0.5, anchor="center")

    # Logo
    ctk.CTkLabel(
        cartao,
        text="EL",
        font=("Arial", 22, "bold"),
        text_color="white",
        fg_color="#3b6fe0",
        corner_radius=14,
        width=56,
        height=56
    ).pack(padx=50, pady=(35, 10))

    # Título
    ctk.CTkLabel(
        cartao,
        text="EvoLink",
        font=("Arial", 28, "bold")
    ).pack()

    ctk.CTkLabel(
        cartao,
        text="Suporte Técnico e Diagnóstico",
        text_color="gray"
    ).pack(pady=(0, 22))

    # Campo de usuário
    usuario = ctk.CTkEntry(
        cartao,
        width=280,
        height=38,
        placeholder_text="Digite seu usuário"
    )
    usuario.pack(pady=8)

    # Campo de senha
    senha = ctk.CTkEntry(
        cartao,
        width=280,
        height=38,
        placeholder_text="Digite sua senha",
        show="*"
    )
    senha.pack(pady=8)

    # Mostrar / ocultar a senha
    def alternar_senha():
        senha.configure(show="" if ver_senha.get() else "*")

    ver_senha = ctk.CTkCheckBox(
        cartao,
        text="Mostrar senha",
        command=alternar_senha
    )
    ver_senha.pack(pady=(4, 0))

    # Função para validar o login
    def validar_login(evento=None):
        nome_usuario = usuario.get().strip()
        senha_digitada = senha.get()

        if nome_usuario == "" or senha_digitada == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha o usuário e a senha."
            )
            return

        if nome_usuario == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
            abrir_menu()
        else:
            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos!"
            )
            senha.delete(0, "end")

    # Apertar Enter também faz o login
    usuario.bind("<Return>", validar_login)
    senha.bind("<Return>", validar_login)

    # Botão de entrar
    ctk.CTkButton(
        cartao,
        text="Entrar",
        width=280,
        height=40,
        font=("Arial", 14, "bold"),
        command=validar_login
    ).pack(pady=(20, 10))

    # Informações de acesso
    ctk.CTkLabel(
        cartao,
        text="Usuário: admin | Senha: 1234",
        text_color="gray"
    ).pack(pady=(5, 30))

    usuario.focus()
