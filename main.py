
import json
import tkinter as tk
from pathlib import Path
from tkinter import font as tkfont
from tkinter import ttk, messagebox
from datetime import datetime

from configuracao import render_settings
from perfil import render_profile

# EvoLink — interface desktop em Tkinter, sem dependências externas.
# Paleta inspirada na referência: fundo claro, laranja/coral, azul-marinho e verde.
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
    "coral": "#F05272",
    "green": "#168B68",
    "green_dark": "#087B59",
    "blue": "#4C8FD9",
    "red": "#E45B66",
}
FONT = "Segoe UI"


class EvoLinkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EvoLink | Suporte e Diagnóstico")
        self.geometry("1180x760")
        self.minsize(900, 620)
        self.configure(bg=COLORS["background"])

        self.current_page = "Início"
        self.tickets = [
            {"id": "CH-1042", "assunto": "Computador não inicia", "setor": "Financeiro", "status": "Aberto", "prioridade": "Alta", "data": "Hoje, 09:42"},
            {"id": "CH-1041", "assunto": "Acesso ao sistema ERP", "setor": "Comercial", "status": "Em atendimento", "prioridade": "Média", "data": "Hoje, 08:17"},
            {"id": "CH-1039", "assunto": "Instalação de impressora", "setor": "Recepção", "status": "Resolvido", "prioridade": "Baixa", "data": "Ontem, 16:30"},
        ]
        self.sectors = ["Financeiro", "Comercial", "Recepção", "Tecnologia"]
        self.computers = [
            {"nome": "PC-FIN-014", "setor": "Financeiro", "status": "Online"},
            {"nome": "NOTE-COM-008", "setor": "Comercial", "status": "Online"},
            {"nome": "PC-REC-003", "setor": "Recepção", "status": "Manutenção"},
        ]
        self.users = [
            {"nome": "Ana Oliveira", "perfil": "Administradora", "setor": "Tecnologia"},
            {"nome": "Marcos Lima", "perfil": "Técnico", "setor": "Tecnologia"},
            {"nome": "Julia Santos", "perfil": "Solicitante", "setor": "Financeiro"},
        ]
        self.preferences_path = Path.home() / ".evolink" / "preferences.json"
        self.text_scale_factor = self._load_text_scale()
        self._configure_styles()
        self._build_login_screen()

    def _draw_brand_icon(self, parent):
        """Desenha um monitor com sinal de diagnóstico para a identidade EvoLink."""
        icon = tk.Canvas(
            parent, width=38, height=38, bg=COLORS["surface"],
            highlightthickness=0,
        )
        icon.create_rectangle(
            4, 4, 34, 26, outline=COLORS["navy"], width=2, fill="#FCFBFD"
        )
        icon.create_line(
            8, 16, 13, 16, 16, 10, 20, 21, 24, 14, 27, 16, 30, 16,
            fill=COLORS["orange"], width=2.2, capstyle="round", joinstyle="round",
        )
        icon.create_line(19, 26, 19, 31, 12, 31, 26, 31,
                         fill=COLORS["navy"], width=2, capstyle="round")
        return icon

    def _build_login_screen(self):
        """Exibe o formulário demonstrativo de entrada no sistema."""
        for child in self.winfo_children():
            child.destroy()

        self.title("EvoLink | Entrar")
        self.configure(bg=COLORS["background"])
        panel = tk.Frame(self, bg=COLORS["background"], padx=24, pady=24)
        panel.pack(fill="both", expand=True)

        card = tk.Frame(
            panel, bg=COLORS["surface"], padx=34, pady=30,
            highlightthickness=1, highlightbackground=COLORS["line"],
        )
        card.place(relx=0.5, rely=0.5, anchor="center", width=420)

        brand = tk.Frame(card, bg=COLORS["surface"])
        brand.pack(anchor="center", pady=(0, 20))
        mark = self._draw_brand_icon(brand)
        mark.pack(side="left", padx=(0, 9))
        brand_name = tk.Frame(brand, bg=COLORS["surface"])
        brand_name.pack(side="left", anchor="w")
        tk.Label(
            brand_name, text="EvoLink", bg=COLORS["surface"], fg=COLORS["navy"],
            font=(FONT, 16, "bold"),
        ).pack(anchor="w")
        tk.Label(
            brand_name, text="SUPORTE & DIAGNÓSTICO", bg=COLORS["surface"],
            fg=COLORS["muted"], font=(FONT, 7, "bold"),
        ).pack(anchor="w")

        tk.Label(
            card, text="Acesse sua conta", bg=COLORS["surface"],
            fg=COLORS["navy"], font=(FONT, 18, "bold"),
        ).pack(anchor="w")
        tk.Label(
            card, text="Entre para continuar no sistema de suporte.",
            bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9),
        ).pack(anchor="w", pady=(4, 18))

        tk.Label(
            card, text="Usuário", bg=COLORS["surface"], fg=COLORS["text"],
            font=(FONT, 9, "bold"),
        ).pack(anchor="w", pady=(0, 6))
        self.login_user_entry = tk.Entry(
            card, bg="#FCFBFD", fg=COLORS["text"], insertbackground=COLORS["text"],
            relief="flat", highlightthickness=1, highlightbackground=COLORS["line"],
            highlightcolor=COLORS["orange"], font=(FONT, 10),
        )
        self.login_user_entry.pack(fill="x", ipady=9, pady=(0, 14))
        self.login_user_entry.bind("<KeyRelease>", self._update_login_preview)

        tk.Label(
            card, text="Senha", bg=COLORS["surface"], fg=COLORS["text"],
            font=(FONT, 9, "bold"),
        ).pack(anchor="w", pady=(0, 6))
        self.login_password_entry = tk.Entry(
            card, show="•", bg="#FCFBFD", fg=COLORS["text"],
            insertbackground=COLORS["text"], relief="flat",
            highlightthickness=1, highlightbackground=COLORS["line"],
            highlightcolor=COLORS["orange"], font=(FONT, 10),
        )
        self.login_password_entry.pack(fill="x", ipady=9, pady=(0, 18))

        self._button(card, "Entrar no sistema", self._submit_login).pack(fill="x")
        self.login_user_preview = tk.StringVar(master=self, value="Usuário: —")
        tk.Label(
            card, textvariable=self.login_user_preview, bg=COLORS["surface"],
            fg=COLORS["orange_dark"], font=(FONT, 9, "bold"),
        ).pack(anchor="w", pady=(11, 0))
        tk.Label(
            card,
            text="Modo demonstrativo: o formulário exige campos preenchidos,\nmas não verifica credenciais reais.",
            bg=COLORS["surface"], fg=COLORS["muted"], justify="left",
            font=(FONT, 8),
        ).pack(anchor="w", pady=(14, 0))

        self.login_user_entry.focus_set()
        self.bind("<Return>", lambda _event: self._submit_login())
        self._apply_text_scale_to_tree()

    def _update_login_preview(self, _event=None):
        """Mostra abaixo do formulário o nome que está sendo digitado."""
        username = self.login_user_entry.get().strip()
        self.login_user_preview.set(f"Usuário: {username}" if username else "Usuário: —")

    def _submit_login(self):
        """Abre o aplicativo após o preenchimento dos campos demonstrativos."""
        if not self.login_user_entry.get().strip():
            messagebox.showwarning(
                "Campo obrigatório", "Informe o usuário para continuar.", parent=self
            )
            self.login_user_entry.focus_set()
            return
        if not self.login_password_entry.get():
            messagebox.showwarning(
                "Campo obrigatório", "Informe a senha para continuar.", parent=self
            )
            self.login_password_entry.focus_set()
            return

        self.active_username = self.login_user_entry.get().strip()
        if not isinstance(getattr(self, "profile_data", None), dict):
            self.profile_data = {
                "nome": self.active_username,
                "email": "",
                "telefone": "",
                "setor": "Tecnologia",
                "perfil": "Administradora",
            }
        else:
            self.profile_data["nome"] = self.active_username

        self.unbind("<Return>")
        for child in self.winfo_children():
            child.destroy()
        self.title("EvoLink | Suporte e Diagnóstico")
        self._build_shell()
        self.show_page("Início")

    def _logout(self):
        """Encerra a sessão demonstrativa e retorna à tela de login."""
        self._build_login_screen()

    def _configure_styles(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure(
            "Evo.TCombobox", fieldbackground=COLORS["surface"],
            background=COLORS["surface"], foreground=COLORS["text"],
            arrowcolor=COLORS["muted"], padding=8,
        )
        style.map("Evo.TCombobox", fieldbackground=[("readonly", COLORS["surface"])])

    def _load_text_scale(self):
        """Carrega a escala salva; usa 100% se o arquivo não existir ou for inválido."""
        try:
            preferences = json.loads(self.preferences_path.read_text(encoding="utf-8"))
            factor = float(preferences.get("text_scale_factor", 1.0))
            if 0.8 <= factor <= 2.0:
                return factor
        except (OSError, ValueError, TypeError, AttributeError):
            pass
        return 1.0

    def _save_text_scale(self):
        """Grava a escala escolhida no arquivo local de preferências do usuário."""
        preferences = {}
        try:
            loaded = json.loads(self.preferences_path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                preferences.update(loaded)
        except (OSError, ValueError, TypeError):
            pass

        preferences["text_scale_factor"] = self.text_scale_factor
        try:
            self.preferences_path.parent.mkdir(parents=True, exist_ok=True)
            temporary_path = self.preferences_path.with_suffix(".tmp")
            temporary_path.write_text(
                json.dumps(preferences, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            temporary_path.replace(self.preferences_path)
            return True
        except OSError:
            return False

    def set_text_scale(self, factor):
        """Aplica um fator de escala aos tamanhos tipográficos do aplicativo."""
        factor = float(factor)
        if not 0.8 <= factor <= 2.0:
            raise ValueError("O tamanho do texto deve ficar entre 80% e 200%.")
        self.text_scale_factor = factor
        self._apply_text_scale_to_tree()
        self.update_idletasks()
        return self._save_text_scale()

    def _apply_text_scale_to_tree(self, parent=None):
        """Redimensiona as fontes atuais e guarda o tamanho-base de cada widget."""
        parent = parent or self
        try:
            font_description = parent.cget("font")
        except (tk.TclError, AttributeError):
            font_description = ""

        if font_description:
            try:
                base_font = getattr(parent, "_evolink_base_font", None)
                if base_font is None:
                    parsed_font = tkfont.Font(root=self, font=font_description)
                    base_font = parsed_font.actual()
                    parent._evolink_base_font = base_font

                base_size = int(base_font["size"])
                new_size = max(1, round(abs(base_size) * self.text_scale_factor))
                if base_size < 0:
                    new_size = -new_size
                font_options = [base_font["family"], new_size]
                if base_font["weight"] == "bold":
                    font_options.append("bold")
                if base_font["slant"] == "italic":
                    font_options.append("italic")
                if base_font["underline"]:
                    font_options.append("underline")
                if base_font["overstrike"]:
                    font_options.append("overstrike")
                parent.configure(font=tuple(font_options))
            except (tk.TclError, TypeError, ValueError, KeyError):
                pass

        try:
            children = parent.winfo_children()
        except (tk.TclError, AttributeError):
            children = ()
        for child in children:
            self._apply_text_scale_to_tree(child)

    def _build_shell(self):
        self.grid_columnconfigure(0, minsize=230, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.topbar = tk.Frame(self, bg=COLORS["surface"], height=74,
                               highlightthickness=1, highlightbackground=COLORS["line"])
        self.topbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.topbar.grid_propagate(False)
        self._build_topbar()

        self.sidebar = tk.Frame(self, bg=COLORS["surface"], width=230,
                                 highlightthickness=1, highlightbackground=COLORS["line"])
        self.sidebar.grid(row=1, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self._build_sidebar()

        self.content = tk.Frame(self, bg=COLORS["background"], padx=30, pady=26)
        self.content.grid(row=1, column=1, sticky="nsew")
        self._apply_text_scale_to_tree()

    def _build_topbar(self):
        brand = tk.Frame(self.topbar, bg=COLORS["surface"])
        brand.pack(side="left", padx=(25, 0), pady=13)

        mark = self._draw_brand_icon(brand)
        mark.pack(side="left", padx=(0, 9))

        name = tk.Frame(brand, bg=COLORS["surface"])
        name.pack(side="left", anchor="w")
        tk.Label(name, text="EvoLink", bg=COLORS["surface"], fg=COLORS["navy"],
                 font=(FONT, 15, "bold")).pack(anchor="w")
        tk.Label(name, text="SUPORTE & DIAGNÓSTICO", bg=COLORS["surface"],
                 fg=COLORS["muted"], font=(FONT, 7, "bold")).pack(anchor="w")

        tk.Label(self.topbar, text="Central de suporte", bg=COLORS["surface"],
                 fg=COLORS["muted"], font=(FONT, 10)).pack(side="left", padx=48)

        actions = tk.Frame(self.topbar, bg=COLORS["surface"])
        actions.pack(side="right", padx=24, pady=15)
        bell = tk.Button(actions, text="♧  7", command=self._show_notifications,
                         bg=COLORS["surface"], fg=COLORS["text"],
                         activebackground=COLORS["surface_soft"],
                         activeforeground=COLORS["orange_dark"], relief="flat",
                         font=(FONT, 10), cursor="hand2", padx=10, pady=8)
        bell.pack(side="left", padx=(0, 10))
        self._button(actions, "+  Nova chamada", lambda: self.show_page("Nova Chamada"),
                     kind="primary").pack(side="left")

    def _build_sidebar(self):
        tk.Label(self.sidebar, text="MENU PRINCIPAL", bg=COLORS["surface"],
                 fg="#A19EAA", font=(FONT, 8, "bold")).pack(anchor="w", padx=22, pady=(25, 12))

        self.nav_buttons = {}
        items = [
            ("Início", "⌂"),
            ("Nova Chamada", "+"),
            ("Novo Setor", "▦"),
            ("Consultar Chamadas", "⌕"),
            ("Computadores", "▣"),
            ("Usuários", "♙"),
            ("Relatórios", "▤"),
            ("Meu Perfil", "♙"),
            ("Configurações", "⚙"),
        ]
        for label, icon in items:
            button = tk.Button(
                self.sidebar, text=f"  {icon}     {label}", anchor="w",
                command=lambda page=label: self.show_page(page),
                relief="flat", borderwidth=0, cursor="hand2",
                font=(FONT, 10), padx=12, pady=10,
                bg=COLORS["surface"], fg=COLORS["muted"],
                activebackground=COLORS["surface_soft"],
                activeforeground=COLORS["orange_dark"],
            )
            button.pack(fill="x", padx=12, pady=2)
            self.nav_buttons[label] = button

        divider = tk.Frame(self.sidebar, bg=COLORS["line"], height=1)
        divider.pack(fill="x", padx=20, pady=(19, 17))

        tk.Label(self.sidebar, text="ESPAÇO DE TRABALHO", bg=COLORS["surface"],
                 fg="#A19EAA", font=(FONT, 8, "bold")).pack(anchor="w", padx=22, pady=(0, 12))
        workspace = tk.Frame(self.sidebar, bg=COLORS["surface_soft"], padx=11, pady=10)
        workspace.pack(fill="x", padx=17)
        tk.Label(workspace, text="●", fg=COLORS["green"], bg=COLORS["surface_soft"],
                 font=(FONT, 10)).pack(side="left", padx=(0, 7))
        tk.Label(workspace, text="EvoLink Tecnologia", fg=COLORS["text"],
                 bg=COLORS["surface_soft"], font=(FONT, 9, "bold")).pack(side="left")

        footer = tk.Frame(self.sidebar, bg=COLORS["surface"])
        footer.pack(side="bottom", fill="x", padx=18, pady=18)
        tk.Frame(footer, bg=COLORS["line"], height=1).pack(fill="x", pady=(0, 12))
        avatar = tk.Canvas(footer, width=34, height=34, bg=COLORS["surface"],
                           highlightthickness=0)
        avatar.pack(side="left", padx=(0, 9))
        avatar.create_oval(1, 1, 33, 33, fill="#FFE3D4", outline="")
        display_name = getattr(self, "active_username", "Mariana Silva")
        initials = "".join(part[0] for part in display_name.split()[:2]).upper() or "MS"
        avatar.create_text(17, 17, text=initials, fill=COLORS["orange_dark"],
                           font=(FONT, 9, "bold"))
        info = tk.Frame(footer, bg=COLORS["surface"])
        info.pack(side="left", anchor="w")
        tk.Label(info, text=display_name, bg=COLORS["surface"], fg=COLORS["text"],
                 font=(FONT, 9, "bold")).pack(anchor="w")
        tk.Label(info, text="Administradora", bg=COLORS["surface"], fg=COLORS["muted"],
                 font=(FONT, 8)).pack(anchor="w")
        self._button(footer, "↩  Sair da conta", self._logout, kind="soft").pack(
            fill="x", pady=(11, 0)
        )

    def _button(self, parent, text, command, kind="primary"):
        if kind == "primary":
            bg, fg, active_bg, active_fg = COLORS["orange"], "white", COLORS["orange_dark"], "white"
        elif kind == "soft":
            bg, fg, active_bg, active_fg = COLORS["surface"], COLORS["text"], COLORS["surface_soft"], COLORS["orange_dark"]
        elif kind == "green":
            bg, fg, active_bg, active_fg = COLORS["green"], "white", COLORS["green_dark"], "white"
        else:
            bg, fg, active_bg, active_fg = COLORS["navy"], "white", COLORS["text"], "white"
        return tk.Button(parent, text=text, command=command, bg=bg, fg=fg,
                         activebackground=active_bg, activeforeground=active_fg,
                         relief="flat", borderwidth=0, cursor="hand2",
                         font=(FONT, 9, "bold"), padx=15, pady=9)

    def _heading(self, title, subtitle):
        header = tk.Frame(self.content, bg=COLORS["background"])
        header.pack(fill="x", pady=(0, 21))
        tk.Label(header, text=title, bg=COLORS["background"], fg=COLORS["navy"],
                 font=(FONT, 22, "bold")).pack(anchor="w")
        tk.Label(header, text=subtitle, bg=COLORS["background"], fg=COLORS["muted"],
                 font=(FONT, 10)).pack(anchor="w", pady=(4, 0))

    def _card(self, parent, padx=17, pady=15):
        frame = tk.Frame(parent, bg=COLORS["surface"], padx=padx, pady=pady,
                         highlightthickness=1, highlightbackground=COLORS["line"])
        return frame

    def _clear_content(self):
        for child in self.content.winfo_children():
            child.destroy()

    def show_page(self, page):
        self.current_page = page
        for label, button in self.nav_buttons.items():
            active = label == page
            button.configure(
                bg=COLORS["surface_soft"] if active else COLORS["surface"],
                fg=COLORS["orange_dark"] if active else COLORS["muted"],
                font=(FONT, 10, "bold" if active else "normal"),
            )
        self._clear_content()
        routes = {
            "Início": self._page_home,
            "Nova Chamada": self._page_new_ticket,
            "Novo Setor": self._page_new_sector,
            "Consultar Chamadas": self._page_tickets,
            "Computadores": self._page_computers,
            "Usuários": self._page_users,
            "Relatórios": self._page_reports,
            "Meu Perfil": lambda: render_profile(self),
            "Configurações": lambda: render_settings(self),
        }
        routes.get(page, self._page_home)()
        self._apply_text_scale_to_tree(self.content)

    def _page_home(self):
        self._heading("Bom dia, Mariana 👋", "Aqui está um resumo do suporte técnico da sua equipe.")

        hero = tk.Frame(self.content, bg=COLORS["surface_soft"], padx=24, pady=21,
                        highlightthickness=1, highlightbackground="#F9E1D6")
        hero.pack(fill="x", pady=(0, 18))
        tk.Label(hero, text="SOLUÇÃO  ·  SUPORTE TÉCNICO", bg="#DDF5EB",
                 fg=COLORS["green_dark"], font=(FONT, 8, "bold"), padx=10, pady=5).pack(anchor="w")
        tk.Label(hero, text="Seu suporte técnico,\nmais simples e conectado.",
                 bg=COLORS["surface_soft"], fg=COLORS["navy"],
                 justify="left", font=(FONT, 20, "bold")).pack(anchor="w", pady=(12, 5))
        tk.Label(hero, text="Acompanhe chamados, equipamentos e sua equipe em um só lugar.",
                 bg=COLORS["surface_soft"], fg=COLORS["muted"],
                 font=(FONT, 9)).pack(anchor="w", pady=(0, 13))
        actions = tk.Frame(hero, bg=COLORS["surface_soft"])
        actions.pack(anchor="w")
        self._button(actions, "+  Abrir uma chamada", lambda: self.show_page("Nova Chamada")).pack(side="left", padx=(0, 9))
        self._button(actions, "Consultar chamados", lambda: self.show_page("Consultar Chamadas"), "soft").pack(side="left")

        stats = tk.Frame(self.content, bg=COLORS["background"])
        stats.pack(fill="x", pady=(0, 18))
        for column in range(3):
            stats.grid_columnconfigure(column, weight=1, uniform="stats")
        open_count = sum(t["status"] == "Aberto" for t in self.tickets)
        progress_count = sum(t["status"] == "Em atendimento" for t in self.tickets)
        for col, (title, value, note, accent) in enumerate([
            ("Chamados abertos", str(open_count), "Precisam de atenção", COLORS["orange"]),
            ("Em atendimento", str(progress_count), "Com a equipe técnica", COLORS["blue"]),
            ("Equipamentos", str(len(self.computers)), "Cadastrados no sistema", COLORS["green"]),
        ]):
            card = self._card(stats, padx=15, pady=13)
            card.grid(row=0, column=col, sticky="ew", padx=(0 if col == 0 else 9, 0 if col == 2 else 9))
            tk.Label(card, text=title, bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 9)).pack(anchor="w")
            tk.Label(card, text=value, bg=COLORS["surface"], fg=accent,
                     font=(FONT, 23, "bold")).pack(anchor="w", pady=(5, 0))
            tk.Label(card, text=note, bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 8)).pack(anchor="w", pady=(1, 0))

        section = tk.Frame(self.content, bg=COLORS["background"])
        section.pack(fill="x", pady=(1, 9))
        tk.Label(section, text="Chamados recentes", bg=COLORS["background"], fg=COLORS["navy"],
                 font=(FONT, 13, "bold")).pack(side="left")
        tk.Button(section, text="Ver todos →", command=lambda: self.show_page("Consultar Chamadas"),
                  bg=COLORS["background"], fg=COLORS["orange_dark"], relief="flat",
                  cursor="hand2", font=(FONT, 9, "bold")).pack(side="right")
        recent = self._card(self.content, padx=15, pady=5)
        recent.pack(fill="x")
        if not self.tickets:
            tk.Label(recent, text="Ainda não há chamados cadastrados.", bg=COLORS["surface"],
                     fg=COLORS["muted"], font=(FONT, 9), pady=15).pack(anchor="w")
        else:
            for ticket in self.tickets[:3]:
                self._ticket_row(recent, ticket)

    def _ticket_row(self, parent, ticket):
        row = tk.Frame(parent, bg=COLORS["surface"], pady=10)
        row.pack(fill="x")
        left = tk.Frame(row, bg=COLORS["surface"])
        left.pack(side="left", fill="x", expand=True)
        tk.Label(left, text=f"{ticket['id']}  ·  {ticket['assunto']}",
                 bg=COLORS["surface"], fg=COLORS["text"], font=(FONT, 9, "bold")).pack(anchor="w")
        tk.Label(left, text=f"{ticket['setor']}  ·  {ticket['data']}",
                 bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 8)).pack(anchor="w", pady=(3, 0))
        status_color = COLORS["green"] if ticket["status"] == "Resolvido" else COLORS["orange_dark"]
        tk.Label(row, text=ticket["status"], bg=COLORS["surface_green"] if ticket["status"] == "Resolvido" else COLORS["surface_soft"],
                 fg=status_color, font=(FONT, 8, "bold"), padx=9, pady=5).pack(side="right")
        tk.Frame(parent, bg=COLORS["line"], height=1).pack(fill="x")

    def _page_new_ticket(self):
        self._heading("Nova chamada", "Descreva a solicitação para encaminhá-la à equipe de suporte.")
        card = self._card(self.content, padx=22, pady=20)
        card.pack(fill="x", anchor="n")
        self._form_label(card, "Assunto")
        subject = tk.Entry(card, bg="#FCFBFD", fg=COLORS["text"], insertbackground=COLORS["text"],
                           relief="flat", highlightthickness=1, highlightbackground=COLORS["line"],
                           highlightcolor=COLORS["orange"], font=(FONT, 10))
        subject.pack(fill="x", ipady=9, pady=(0, 14))

        row = tk.Frame(card, bg=COLORS["surface"])
        row.pack(fill="x")
        col1 = tk.Frame(row, bg=COLORS["surface"])
        col1.pack(side="left", fill="x", expand=True, padx=(0, 10))
        col2 = tk.Frame(row, bg=COLORS["surface"])
        col2.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self._form_label(col1, "Setor")
        sector = ttk.Combobox(col1, values=self.sectors, state="readonly", style="Evo.TCombobox")
        sector.pack(fill="x", pady=(0, 14))
        if self.sectors:
            sector.current(0)
        self._form_label(col2, "Prioridade")
        priority = ttk.Combobox(col2, values=["Baixa", "Média", "Alta"], state="readonly", style="Evo.TCombobox")
        priority.pack(fill="x", pady=(0, 14))
        priority.current(1)

        self._form_label(card, "Descrição")
        description = tk.Text(card, height=5, bg="#FCFBFD", fg=COLORS["text"],
                              insertbackground=COLORS["text"], relief="flat", wrap="word",
                              highlightthickness=1, highlightbackground=COLORS["line"],
                              highlightcolor=COLORS["orange"], font=(FONT, 9), padx=10, pady=9)
        description.pack(fill="x", pady=(0, 16))
        actions = tk.Frame(card, bg=COLORS["surface"])
        actions.pack(fill="x")
        self._button(actions, "Criar chamada", lambda: self._create_ticket(
            subject.get(), sector.get(), priority.get(), description.get("1.0", "end-1c"))).pack(side="right")
        self._button(actions, "Cancelar", lambda: self.show_page("Início"), "soft").pack(side="right", padx=(0, 9))

    def _create_ticket(self, subject, sector, priority, description):
        if not subject.strip():
            messagebox.showwarning("Campo obrigatório", "Informe o assunto da chamada.", parent=self)
            return
        now = datetime.now()
        self.tickets.insert(0, {
            "id": f"CH-{1043 + len(self.tickets)}", "assunto": subject.strip(),
            "setor": sector or "Geral", "status": "Aberto", "prioridade": priority or "Média",
            "data": now.strftime("Hoje, %H:%M"), "descricao": description.strip(),
        })
        messagebox.showinfo("Chamada criada", "A chamada foi registrada com sucesso.", parent=self)
        self.show_page("Consultar Chamadas")

    def _page_new_sector(self):
        self._heading("Novo setor", "Organize os setores atendidos pelo suporte técnico.")
        card = self._card(self.content, padx=22, pady=20)
        card.pack(fill="x", anchor="n")
        self._form_label(card, "Nome do setor")
        name = tk.Entry(card, bg="#FCFBFD", fg=COLORS["text"], insertbackground=COLORS["text"],
                        relief="flat", highlightthickness=1, highlightbackground=COLORS["line"],
                        highlightcolor=COLORS["orange"], font=(FONT, 10))
        name.pack(fill="x", ipady=9, pady=(0, 15))
        self._button(card, "Adicionar setor", lambda: self._create_sector(name.get())).pack(anchor="e")

        list_card = self._card(self.content, padx=18, pady=14)
        list_card.pack(fill="x", pady=(18, 0))
        tk.Label(list_card, text="Setores cadastrados", bg=COLORS["surface"], fg=COLORS["navy"],
                 font=(FONT, 11, "bold")).pack(anchor="w", pady=(0, 8))
        for item in self.sectors:
            tk.Label(list_card, text=f"●   {item}", bg=COLORS["surface"], fg=COLORS["text"],
                     font=(FONT, 9), pady=5).pack(anchor="w")

    def _create_sector(self, name):
        name = name.strip()
        if not name:
            messagebox.showwarning("Campo obrigatório", "Digite o nome do setor.", parent=self)
        elif any(existing.casefold() == name.casefold() for existing in self.sectors):
            messagebox.showwarning("Setor existente", "Esse setor já está cadastrado.", parent=self)
        else:
            self.sectors.append(name)
            messagebox.showinfo("Setor criado", f"O setor {name} foi adicionado.", parent=self)
            self.show_page("Novo Setor")

    def _page_tickets(self):
        self._heading("Consultar chamadas", "Pesquise e acompanhe as solicitações registradas.")
        toolbar = tk.Frame(self.content, bg=COLORS["background"])
        toolbar.pack(fill="x", pady=(0, 13))
        search = tk.Entry(toolbar, bg=COLORS["surface"], fg=COLORS["text"],
                          insertbackground=COLORS["text"], relief="flat",
                          highlightthickness=1, highlightbackground=COLORS["line"],
                          highlightcolor=COLORS["orange"], font=(FONT, 9))
        search.pack(side="left", fill="x", expand=True, ipady=9, padx=(0, 10))
        search.insert(0, "Buscar por chamado, assunto ou setor...")
        search.bind("<FocusIn>", lambda _e: search.delete(0, "end") if search.get().startswith("Buscar por") else None)
        search.bind("<KeyRelease>", lambda _e: self._render_ticket_table(list_frame, search.get()))
        self._button(toolbar, "+  Nova chamada", lambda: self.show_page("Nova Chamada")).pack(side="right")
        list_frame = self._card(self.content, padx=16, pady=12)
        list_frame.pack(fill="both", expand=True)
        self._render_ticket_table(list_frame, "")

    def _render_ticket_table(self, parent, query):
        for child in parent.winfo_children():
            child.destroy()
        headers = tk.Frame(parent, bg=COLORS["surface"])
        headers.pack(fill="x", pady=(0, 6))
        for col, title, width in [("ID", 12), ("Assunto", 30), ("Setor", 16), ("Status", 17), ("Prioridade", 14)]:
            tk.Label(headers, text=title.upper(), bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 8, "bold"), width=width, anchor="w").pack(side="left")
        q = query.casefold()
        matches = [t for t in self.tickets if q in " ".join(str(v) for v in t.values()).casefold()]
        if not matches:
            tk.Label(parent, text="Nenhuma chamada corresponde à busca.", bg=COLORS["surface"],
                     fg=COLORS["muted"], font=(FONT, 9), pady=18).pack(anchor="w")
            return
        for ticket in matches:
            row = tk.Frame(parent, bg=COLORS["surface"])
            row.pack(fill="x", pady=8)
            values = [ticket["id"], ticket["assunto"], ticket["setor"], ticket["status"], ticket["prioridade"]]
            widths = [12, 30, 16, 17, 14]
            for index, (value, width) in enumerate(zip(values, widths)):
                tk.Label(row, text=value, bg=COLORS["surface"],
                         fg=COLORS["orange_dark"] if index == 0 else COLORS["text"],
                         font=(FONT, 8, "bold" if index == 0 else "normal"),
                         width=width, anchor="w").pack(side="left")
            tk.Frame(parent, bg=COLORS["line"], height=1).pack(fill="x")

    def _page_computers(self):
        self._heading("Computadores", "Visão geral dos equipamentos cadastrados e seu estado atual.")
        toolbar = tk.Frame(self.content, bg=COLORS["background"])
        toolbar.pack(fill="x", pady=(0, 13))
        tk.Label(toolbar, text=f"{len(self.computers)} equipamentos", bg=COLORS["background"],
                 fg=COLORS["muted"], font=(FONT, 9)).pack(side="left")
        self._button(toolbar, "+  Adicionar computador", lambda: self._add_computer()).pack(side="right")
        card = self._card(self.content, padx=16, pady=13)
        card.pack(fill="x")
        for comp in self.computers:
            row = tk.Frame(card, bg=COLORS["surface"], pady=11)
            row.pack(fill="x")
            tk.Label(row, text="▣", bg=COLORS["surface"], fg=COLORS["orange"],
                     font=(FONT, 15)).pack(side="left", padx=(0, 11))
            info = tk.Frame(row, bg=COLORS["surface"])
            info.pack(side="left", fill="x", expand=True)
            tk.Label(info, text=comp["nome"], bg=COLORS["surface"], fg=COLORS["text"],
                     font=(FONT, 9, "bold")).pack(anchor="w")
            tk.Label(info, text=comp["setor"], bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 8)).pack(anchor="w")
            color = COLORS["green"] if comp["status"] == "Online" else COLORS["orange_dark"]
            tk.Label(row, text=f"●  {comp['status']}", bg=COLORS["surface"], fg=color,
                     font=(FONT, 8, "bold")).pack(side="right")
            tk.Frame(card, bg=COLORS["line"], height=1).pack(fill="x")

    def _add_computer(self):
        dialog = tk.Toplevel(self)
        dialog.title("Adicionar computador")
        dialog.configure(bg=COLORS["surface"])
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        body = tk.Frame(dialog, bg=COLORS["surface"], padx=22, pady=18)
        body.pack(fill="both", expand=True)
        self._form_label(body, "Nome ou identificador")
        name = tk.Entry(body, font=(FONT, 10), relief="flat", bg="#FCFBFD",
                        highlightthickness=1, highlightbackground=COLORS["line"])
        name.pack(fill="x", ipady=8, pady=(0, 12))
        self._form_label(body, "Setor")
        sector = ttk.Combobox(body, values=self.sectors, state="readonly", style="Evo.TCombobox")
        sector.pack(fill="x", pady=(0, 16))
        if self.sectors:
            sector.current(0)
        def save():
            if not name.get().strip():
                messagebox.showwarning("Campo obrigatório", "Informe o nome do equipamento.", parent=dialog)
                return
            self.computers.append({"nome": name.get().strip(), "setor": sector.get() or "Geral", "status": "Online"})
            dialog.destroy()
            self.show_page("Computadores")
        self._button(body, "Salvar equipamento", save).pack(anchor="e")

    def _page_users(self):
        self._heading("Usuários", "Consulte os membros e perfis da equipe de suporte.")
        card = self._card(self.content, padx=16, pady=12)
        card.pack(fill="x")
        for person in self.users:
            row = tk.Frame(card, bg=COLORS["surface"], pady=10)
            row.pack(fill="x")
            avatar = tk.Canvas(row, width=36, height=36, bg=COLORS["surface"], highlightthickness=0)
            avatar.pack(side="left", padx=(0, 10))
            avatar.create_oval(1, 1, 35, 35, fill="#FFE8DD", outline="")
            initials = "".join(part[0] for part in person["nome"].split()[:2]).upper()
            avatar.create_text(18, 18, text=initials, fill=COLORS["orange_dark"], font=(FONT, 8, "bold"))
            info = tk.Frame(row, bg=COLORS["surface"])
            info.pack(side="left", fill="x", expand=True)
            tk.Label(info, text=person["nome"], bg=COLORS["surface"], fg=COLORS["text"],
                     font=(FONT, 9, "bold")).pack(anchor="w")
            tk.Label(info, text=person["setor"], bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 8)).pack(anchor="w")
            tk.Label(row, text=person["perfil"], bg=COLORS["surface_soft"], fg=COLORS["orange_dark"],
                     font=(FONT, 8, "bold"), padx=9, pady=5).pack(side="right")
            tk.Frame(card, bg=COLORS["line"], height=1).pack(fill="x")

    def _page_reports(self):
        self._heading("Relatórios", "Indicadores rápidos para acompanhar a operação de suporte.")
        total = len(self.tickets)
        resolved = sum(t["status"] == "Resolvido" for t in self.tickets)
        opened = sum(t["status"] == "Aberto" for t in self.tickets)
        active = sum(t["status"] == "Em atendimento" for t in self.tickets)
        cards = tk.Frame(self.content, bg=COLORS["background"])
        cards.pack(fill="x")
        for column in range(2):
            cards.grid_columnconfigure(column, weight=1, uniform="reports")
        for index, (label, value, color) in enumerate([
            ("Total de chamados", total, COLORS["navy"]),
            ("Abertos", opened, COLORS["orange"]),
            ("Em atendimento", active, COLORS["blue"]),
            ("Resolvidos", resolved, COLORS["green"]),
        ]):
            card = self._card(cards, padx=18, pady=17)
            card.grid(row=index // 2, column=index % 2, sticky="ew", padx=7, pady=7)
            tk.Label(card, text=label, bg=COLORS["surface"], fg=COLORS["muted"],
                     font=(FONT, 9)).pack(anchor="w")
            tk.Label(card, text=str(value), bg=COLORS["surface"], fg=color,
                     font=(FONT, 25, "bold")).pack(anchor="w", pady=(7, 0))
        note = self._card(self.content, padx=18, pady=16)
        note.pack(fill="x", pady=(12, 0))
        tk.Label(note, text="Resumo da operação", bg=COLORS["surface"], fg=COLORS["navy"],
                 font=(FONT, 11, "bold")).pack(anchor="w")
        tk.Label(note, text=f"Há {opened} chamado(s) aberto(s), {active} em atendimento e {resolved} resolvido(s).",
                 bg=COLORS["surface"], fg=COLORS["muted"], font=(FONT, 9)).pack(anchor="w", pady=(7, 0))

    def _form_label(self, parent, text):
        tk.Label(parent, text=text, bg=COLORS["surface"], fg=COLORS["text"],
                 font=(FONT, 9, "bold")).pack(anchor="w", pady=(0, 7))

    def _show_notifications(self):
        messagebox.showinfo("Notificações", "Você tem 7 notificações pendentes.", parent=self)


if __name__ == "__main__":
    app = EvoLinkApp()
    app.mainloop()
