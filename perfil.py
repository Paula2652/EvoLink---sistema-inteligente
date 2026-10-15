"""Tela de perfil para o aplicativo EvoLink.

Integração com o menu existente:
1. Importe: `from perfil import render_profile`
2. Inclua `("Meu Perfil", "♙")` na lista `items` de `_build_sidebar`.
3. Inclua `"Meu Perfil": lambda: render_profile(self)` no dicionário `routes`
   de `show_page`.

A tela é renderizada dentro de `app.content` e reutiliza os métodos visuais do
EvoLinkApp. As alterações ficam em memória durante a execução do aplicativo.
"""

import tkinter as tk
from tkinter import messagebox


COLORS = {
    "background": "#F8F7FA",
    "surface": "#FFFFFF",
    "surface_soft": "#FFF4EF",
    "surface_green": "#E7F7F1",
    "navy": "#19152D",
    "text": "#29253B",
    "muted": "#777486",
    "line": "#EAE8EE",
    "orange": "#F87535",
    "orange_dark": "#E95E28",
    "green": "#168B68",
    "green_dark": "#087B59",
}
FONT = "Segoe UI"

DEFAULT_PROFILE = {
    "nome": "Mariana Silva",
    "email": "",
    "telefone": "",
    "setor": "Tecnologia",
    "perfil": "Administradora",
}


def render_profile(app):
    """Desenha a página de perfil dentro da área `app.content` do EvoLinkApp."""
    profile = getattr(app, "profile_data", None)
    if not isinstance(profile, dict):
        profile = DEFAULT_PROFILE.copy()
        app.profile_data = profile

    app._heading(
        "Meu perfil",
        "Consulte e atualize suas informações pessoais e de contato.",
    )

    # Cartão de identidade do usuário.
    identity = app._card(app.content, padx=20, pady=18)
    identity.pack(fill="x", pady=(0, 16))

    avatar = tk.Canvas(
        identity, width=66, height=66, bg=COLORS["surface"], highlightthickness=0
    )
    avatar.pack(side="left", padx=(0, 15))
    avatar.create_oval(2, 2, 64, 64, fill="#FFE3D4", outline="")
    initials = "".join(part[0] for part in profile.get("nome", "MS").split()[:2]).upper()
    avatar.create_text(
        33, 33, text=initials or "MS", fill=COLORS["orange_dark"],
        font=(FONT, 15, "bold")
    )

    identity_info = tk.Frame(identity, bg=COLORS["surface"])
    identity_info.pack(side="left", fill="x", expand=True)
    tk.Label(
        identity_info, text=profile.get("nome", ""), bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 15, "bold")
    ).pack(anchor="w")
    tk.Label(
        identity_info, text=profile.get("setor", ""), bg=COLORS["surface"],
        fg=COLORS["muted"], font=(FONT, 9)
    ).pack(anchor="w", pady=(3, 7))
    tk.Label(
        identity, text=profile.get("perfil", "Usuário"),
        bg=COLORS["surface_soft"], fg=COLORS["orange_dark"],
        font=(FONT, 8, "bold"), padx=10, pady=6
    ).pack(side="right", anchor="n")

    # Formulário de edição.
    form = app._card(app.content, padx=20, pady=18)
    form.pack(fill="x")
    tk.Label(
        form, text="Informações da conta", bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 12, "bold")
    ).pack(anchor="w", pady=(0, 15))

    fields = [
        ("Nome completo", "nome"),
        ("E-mail", "email"),
        ("Telefone", "telefone"),
        ("Setor", "setor"),
    ]
    entries = {}
    field_grid = tk.Frame(form, bg=COLORS["surface"])
    field_grid.pack(fill="x")
    field_grid.grid_columnconfigure(0, weight=1, uniform="profile_fields")
    field_grid.grid_columnconfigure(1, weight=1, uniform="profile_fields")

    for index, (label, key) in enumerate(fields):
        row, column = divmod(index, 2)
        cell = tk.Frame(field_grid, bg=COLORS["surface"])
        cell.grid(
            row=row, column=column, sticky="ew",
            padx=(0, 10) if column == 0 else (10, 0),
            pady=(0, 14),
        )
        tk.Label(
            cell, text=label, bg=COLORS["surface"], fg=COLORS["text"],
            font=(FONT, 9, "bold")
        ).pack(anchor="w", pady=(0, 6))
        entry = tk.Entry(
            cell, bg="#FCFBFD", fg=COLORS["text"],
            insertbackground=COLORS["text"], relief="flat",
            highlightthickness=1, highlightbackground=COLORS["line"],
            highlightcolor=COLORS["orange"], font=(FONT, 10),
        )
        entry.pack(fill="x", ipady=9)
        entry.insert(0, profile.get(key, ""))
        entries[key] = entry

    buttons = tk.Frame(form, bg=COLORS["surface"])
    buttons.pack(fill="x", pady=(2, 0))

    def save_profile():
        name = entries["nome"].get().strip()
        if not name:
            messagebox.showwarning(
                "Campo obrigatório", "Informe seu nome completo.", parent=app
            )
            entries["nome"].focus_set()
            return

        for key, entry in entries.items():
            profile[key] = entry.get().strip()

        # Atualiza também a identificação apresentada no topo do cartão.
        for child in identity_info.winfo_children():
            child.destroy()
        tk.Label(
            identity_info, text=profile["nome"], bg=COLORS["surface"],
            fg=COLORS["navy"], font=(FONT, 15, "bold")
        ).pack(anchor="w")
        tk.Label(
            identity_info, text=profile["setor"], bg=COLORS["surface"],
            fg=COLORS["muted"], font=(FONT, 9)
        ).pack(anchor="w", pady=(3, 7))
        avatar.itemconfigure(
            2, text="".join(part[0] for part in profile["nome"].split()[:2]).upper()
        )
        messagebox.showinfo(
            "Perfil atualizado", "Suas informações foram atualizadas nesta sessão.",
            parent=app,
        )

    def reset_fields():
        for key, entry in entries.items():
            entry.delete(0, "end")
            entry.insert(0, profile.get(key, ""))

    app._button(buttons, "Salvar alterações", save_profile, kind="primary").pack(side="right")
    app._button(buttons, "Descartar", reset_fields, kind="soft").pack(
        side="right", padx=(0, 9)
    )

    appearance = app._card(app.content, padx=20, pady=16)
    appearance.pack(fill="x", pady=(16, 0))
    tk.Label(
        appearance, text="Aparência do sistema", bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 12, "bold")
    ).pack(anchor="w")
    tk.Label(
        appearance,
        text="Digite a porcentagem (80 a 200%); o ajuste é aplicado quando o valor é válido.",
        bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9)
    ).pack(anchor="w", pady=(4, 10))

    current_factor = getattr(app, "text_scale_factor", 1.0)
    scale_row = tk.Frame(appearance, bg=COLORS["surface"])
    scale_row.pack(fill="x")
    percentage_var = tk.StringVar(master=app, value=f"{current_factor * 100:g}")
    app._profile_percentage_var = percentage_var
    size_entry = tk.Entry(
        scale_row, width=10, textvariable=percentage_var,
        bg="#FCFBFD", fg=COLORS["text"],
        insertbackground=COLORS["text"], relief="flat",
        highlightthickness=1, highlightbackground=COLORS["line"],
        highlightcolor=COLORS["orange"], font=(FONT, 10),
    )
    size_entry.pack(side="left", ipady=8)
    tk.Label(
        scale_row, text="%", bg=COLORS["surface"], fg=COLORS["text"],
        font=(FONT, 10, "bold"),
    ).pack(side="left", padx=(7, 0))
    scale_status = tk.StringVar(
        master=app, value=f"Tamanho atual: {current_factor * 100:g}%"
    )
    app._profile_scale_status = scale_status

    def apply_text_size(_event=None, show_errors=False):
        value = size_entry.get().strip().replace("%", "").strip().replace(",", ".")
        try:
            percentage = float(value)
        except ValueError:
            if show_errors:
                messagebox.showwarning(
                    "Percentual inválido", "Digite um número, como 125.", parent=app
                )
                size_entry.focus_set()
            return
        if not 80 <= percentage <= 200:
            if show_errors:
                messagebox.showwarning(
                    "Fora do limite", "Use um percentual entre 80 e 200.", parent=app
                )
                size_entry.focus_set()
            return

        saved = app.set_text_scale(percentage / 100)
        save_note = "salvo neste computador" if saved else "aplicado apenas nesta sessão"
        scale_status.set(f"Tamanho atual: {percentage:g}% — {save_note}")

    percentage_var.trace_add("write", lambda *_args: apply_text_size())
    size_entry.bind("<Return>", apply_text_size)
    app._button(
        scale_row, "Aplicar", lambda: apply_text_size(show_errors=True), kind="primary"
    ).pack(side="right")
    tk.Label(
        appearance,
        textvariable=scale_status, bg=COLORS["surface"],
        fg=COLORS["green_dark"], font=(FONT, 8, "bold"),
    ).pack(anchor="w", pady=(8, 0))

    tk.Label(
        app.content,
        text="As alterações são mantidas apenas enquanto o aplicativo estiver aberto.",
        bg=COLORS["background"], fg=COLORS["muted"], font=(FONT, 8),
    ).pack(anchor="w", pady=(10, 0))
