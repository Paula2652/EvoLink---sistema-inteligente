"""Tela de configurações para o aplicativo EvoLink.

Integração com o menu existente:
1. Importe: `from configuracao import render_settings`
2. Inclua `("Configurações", "⚙")` na lista `items` de `_build_sidebar`.
3. Inclua `"Configurações": lambda: render_settings(self)` no dicionário
   `routes` de `show_page`.

A tela é renderizada dentro de `app.content`. Os valores são mantidos no
atributo `app.settings_data` durante a execução atual do aplicativo.
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

DEFAULT_SETTINGS = {
    "nome_workspace": "EvoLink Tecnologia",
    "notificacoes_ativas": True,
    "avisar_novos_chamados": True,
    "avisar_atualizacoes": True,
}


def render_settings(app):
    """Desenha a página de configurações na área `app.content` do EvoLinkApp."""
    settings = getattr(app, "settings_data", None)
    if not isinstance(settings, dict):
        settings = DEFAULT_SETTINGS.copy()
        app.settings_data = settings
    else:
        # Completa configurações existentes sem descartar valores já definidos.
        for key, value in DEFAULT_SETTINGS.items():
            settings.setdefault(key, value)

    app._heading(
        "Configurações",
        "Personalize o espaço de trabalho e as preferências do aplicativo.",
    )

    workspace_card = app._card(app.content, padx=20, pady=18)
    workspace_card.pack(fill="x", pady=(0, 16))
    tk.Label(
        workspace_card, text="Espaço de trabalho", bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 12, "bold")
    ).pack(anchor="w")
    tk.Label(
        workspace_card,
        text="Defina o nome usado para identificar sua equipe no EvoLink.",
        bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9)
    ).pack(anchor="w", pady=(4, 13))

    tk.Label(
        workspace_card, text="Nome do espaço de trabalho",
        bg=COLORS["surface"], fg=COLORS["text"], font=(FONT, 9, "bold")
    ).pack(anchor="w", pady=(0, 6))
    workspace_entry = tk.Entry(
        workspace_card, bg="#FCFBFD", fg=COLORS["text"],
        insertbackground=COLORS["text"], relief="flat",
        highlightthickness=1, highlightbackground=COLORS["line"],
        highlightcolor=COLORS["orange"], font=(FONT, 10),
    )
    workspace_entry.pack(fill="x", ipady=9)
    workspace_entry.insert(0, settings.get("nome_workspace", ""))

    notifications_card = app._card(app.content, padx=20, pady=18)
    notifications_card.pack(fill="x", pady=(0, 16))
    tk.Label(
        notifications_card, text="Notificações", bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 12, "bold")
    ).pack(anchor="w")
    tk.Label(
        notifications_card,
        text="Escolha quais avisos você quer acompanhar nesta interface.",
        bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9)
    ).pack(anchor="w", pady=(4, 12))

    notification_vars = {
        "notificacoes_ativas": tk.BooleanVar(
            master=app, value=bool(settings.get("notificacoes_ativas", True))
        ),
        "avisar_novos_chamados": tk.BooleanVar(
            master=app, value=bool(settings.get("avisar_novos_chamados", True))
        ),
        "avisar_atualizacoes": tk.BooleanVar(
            master=app, value=bool(settings.get("avisar_atualizacoes", True))
        ),
    }

    options = [
        ("notificacoes_ativas", "Ativar notificações do aplicativo"),
        ("avisar_novos_chamados", "Avisar sobre novos chamados"),
        ("avisar_atualizacoes", "Avisar sobre atualizações de chamados"),
    ]
    for key, text in options:
        tk.Checkbutton(
            notifications_card, text=text, variable=notification_vars[key],
            bg=COLORS["surface"], fg=COLORS["text"],
            activebackground=COLORS["surface"], activeforeground=COLORS["orange_dark"],
            selectcolor=COLORS["surface_soft"], relief="flat", bd=0,
            highlightthickness=0, font=(FONT, 9), cursor="hand2",
        ).pack(anchor="w", pady=4)

    info_card = app._card(app.content, padx=20, pady=15)
    info_card.pack(fill="x")
    tk.Label(
        info_card, text="Sobre", bg=COLORS["surface"],
        fg=COLORS["navy"], font=(FONT, 11, "bold")
    ).pack(anchor="w")
    tk.Label(
        info_card, text="EvoLink · Suporte & Diagnóstico · Interface desktop Tkinter",
        bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9)
    ).pack(anchor="w", pady=(5, 0))

    actions = tk.Frame(app.content, bg=COLORS["background"])
    actions.pack(fill="x", pady=(16, 0))

    def save_settings():
        workspace_name = workspace_entry.get().strip()
        if not workspace_name:
            messagebox.showwarning(
                "Campo obrigatório", "Informe o nome do espaço de trabalho.", parent=app
            )
            workspace_entry.focus_set()
            return

        settings["nome_workspace"] = workspace_name
        for key, variable in notification_vars.items():
            settings[key] = bool(variable.get())

        messagebox.showinfo(
            "Configurações salvas",
            "As preferências foram atualizadas nesta sessão.",
            parent=app,
        )

    def restore_defaults():
        workspace_entry.delete(0, "end")
        workspace_entry.insert(0, DEFAULT_SETTINGS["nome_workspace"])
        for key, variable in notification_vars.items():
            variable.set(DEFAULT_SETTINGS[key])
        settings.clear()
        settings.update(DEFAULT_SETTINGS)
        messagebox.showinfo(
            "Padrões restaurados",
            "As configurações padrão foram restauradas nesta sessão.",
            parent=app,
        )

    app._button(actions, "Salvar configurações", save_settings, kind="primary").pack(
        side="right"
    )
    app._button(actions, "Restaurar padrões", restore_defaults, kind="soft").pack(
        side="right", padx=(0, 9)
    )

    tk.Label(
        app.content,
        text="As configurações ficam em memória e não são gravadas em arquivo ou banco de dados.",
        bg=COLORS["background"], fg=COLORS["muted"], font=(FONT, 8),
    ).pack(anchor="w", pady=(10, 0))
