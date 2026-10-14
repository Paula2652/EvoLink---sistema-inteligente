# """Tela inicial EvoLink — protótipo em Tkinter, sem dependências externas.

# Execute com: python3 evolink_menu.py
# """

# import tkinter as tk
# from tkinter import messagebox
# from datetime import datetime


# # Paleta inspirada na referência
# NAVY = "#0c1830"
# NAVY_HOVER = "#162442"
# BLUE = "#5b86f7"
# BG = "#f4f4fc"
# WHITE = "#ffffff"
# TEXT = "#111b2d"
# MUTED = "#778094"
# BORDER = "#e4e6ed"


# class EvoLinkApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("EvoLink | Suporte & Diagnóstico")
#         self.geometry("1500x820")
#         self.minsize(1050, 650)
#         self.configure(bg=BG)
#         self.active_item = "Início"
#         self.canvas = tk.Canvas(self, bg=BG, highlightthickness=0)
#         self.canvas.pack(fill="both", expand=True)
#         self.canvas.bind("<Configure>", self.draw)
#         self.canvas.bind("<Button-1>", self.on_click)
#         self.canvas.bind("<Motion>", self.on_motion)
#         self.canvas.bind("<Leave>", lambda _e: self.draw())
#         self.hitboxes = []
#         self.hover_tag = None

#     @staticmethod
#     def rounded_rect(c, x1, y1, x2, y2, radius=12, **kwargs):
#         """Desenha um retângulo arredondado usando polígonos suavizados."""
#         r = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)
#         points = [
#             x1+r, y1, x2-r, y1, x2, y1, x2, y1+r,
#             x2, y2-r, x2, y2, x2-r, y2, x1+r, y2,
#             x1, y2, x1, y2-r, x1, y1+r, x1, y1,
#         ]
#         return c.create_polygon(points, smooth=True, splinesteps=24, **kwargs)

#     def add_hitbox(self, coords, action):
#         self.hitboxes.append((coords, action))

#     def draw_icon(self, x, y, symbol, size=14, color=BLUE):
#         self.canvas.create_text(x, y, text=symbol, fill=color,
#                                 font=("DejaVu Sans", size, "bold"))

#     def draw(self, _event=None):
#         c = self.canvas
#         w, h = c.winfo_width(), c.winfo_height()
#         if w < 10 or h < 10:
#             return
#         c.delete("all")
#         self.hitboxes.clear()

#         sidebar_w = 200
#         c.create_rectangle(0, 0, sidebar_w, h, fill=NAVY, outline=NAVY)
#         # Marca
#         self.rounded_rect(c, 17, 28, 47, 58, 9, fill=BLUE, outline=BLUE)
#         self.draw_icon(32, 43, "▣", 16, WHITE)
#         c.create_text(55, 31, text="EvoLink", anchor="nw", fill=WHITE,
#                       font=("DejaVu Sans", 12, "bold"))
#         c.create_text(55, 48, text="Suporte &", anchor="nw", fill="#9ba8c4",
#                       font=("DejaVu Sans", 9))
#         c.create_text(55, 61, text="Diagnóstico", anchor="nw", fill="#9ba8c4",
#                       font=("DejaVu Sans", 9))
#         # Notificações
#         self.rounded_rect(c, 151, 27, 181, 58, 9, fill="#14213a", outline="#25324a")
#         self.draw_icon(166, 42, "♧", 16, "#bdc9df")
#         self.rounded_rect(c, 170, 20, 184, 34, 7, fill="#ef6267", outline="#ef6267")
#         c.create_text(177, 27, text="7", fill=WHITE, font=("DejaVu Sans", 8, "bold"))
#         c.create_line(15, 80, sidebar_w-15, 80, fill="#1b2942")

#         nav_items = [
#             ("Início", "⌂"), ("Nova Chamada", "+"), ("Novo Setor", "+"),
#             ("Consultar Chamadas", "⌕"), ("Computadores", "▱"),
#             ("Usuários", "♙"), ("Relatórios", "▥"),
#         ]
#         y = 95
#         for label, icon in nav_items:
#             selected = label == self.active_item
#             if selected:
#                 self.rounded_rect(c, 9, y, sidebar_w-12, y+33, 8,
#                                   fill="#14213c", outline="#253653")
#             elif self.hover_tag == f"nav:{label}":
#                 self.rounded_rect(c, 9, y, sidebar_w-12, y+33, 8,
#                                   fill=NAVY_HOVER, outline=NAVY_HOVER)
#             self.draw_icon(27, y+16, icon, 14, BLUE if selected else "#9ba8c4")
#             c.create_text(43, y+16, text=label, anchor="w",
#                           fill=WHITE if selected else "#aab5ca",
#                           font=("DejaVu Sans", 10, "bold" if selected else "normal"))
#             self.add_hitbox((9, y, sidebar_w-12, y+33), ("nav", label))
#             y += 35 if label == "Início" else 35

#         # Perfil no rodapé
#         c.create_line(15, h-50, sidebar_w-15, h-50, fill="#1b2942")
#         self.rounded_rect(c, 9, h-39, 31, h-17, 11, fill="#1b2a45", outline="#30405d")
#         self.draw_icon(20, h-28, "♙", 12, "#aab9d5")
#         c.create_oval(36, h-34, 43, h-27, fill="#31c48d", outline="#31c48d")
#         c.create_text(48, h-34, text="Administrador", anchor="w", fill="#e3e9f3",
#                       font=("DejaVu Sans", 9, "bold"))
#         c.create_text(48, h-21, text="Online · Perfil e Configurações", anchor="w",
#                       fill="#8491aa", font=("DejaVu Sans", 8))
#         self.draw_icon(182, h-28, "⚙", 12, "#8391aa")

#         # Conteúdo principal
#         x0 = sidebar_w + 28
#         available_w = max(500, w - x0 - 28)
#         c.create_text(x0, 27, text="Bem-vindo ao EvoLink", anchor="nw", fill=TEXT,
#                       font=("DejaVu Sans", 17, "bold"))
#         c.create_text(x0, 53,
#                       text="Sistema inteligente de registro, diagnóstico e acompanhamento de chamados de suporte técnico.",
#                       anchor="nw", fill=MUTED, font=("DejaVu Sans", 9))
#         now = datetime.now().strftime("%d/%m/%Y · %H:%M")
#         c.create_text(w-28, 39, text=now, anchor="e", fill="#687083",
#                       font=("DejaVu Sans Mono", 9))

#         stats = [("5", "Total de chamados"), ("2", "Resolvidos"),
#                  ("3", "Pendentes"), ("Computador lento", "Problema mais frequente")]
#         card_w, card_h, gap = 178, 70, 14
#         for i, (value, label) in enumerate(stats):
#             x = x0 + i * (card_w + gap)
#             self.rounded_rect(c, x, 83, x+card_w, 83+card_h, 12,
#                               fill=WHITE, outline=BORDER, width=1)
#             if i < 3:
#                 c.create_text(x+15, 96, text=value, anchor="nw", fill=TEXT,
#                               font=("DejaVu Sans", 20, "bold"))
#                 c.create_text(x+15, 128, text=label, anchor="nw", fill=MUTED,
#                               font=("DejaVu Sans", 9))
#             else:
#                 c.create_text(x+15, 100, text=value, anchor="nw", fill="#4969b9",
#                               font=("DejaVu Sans", 11, "bold"))
#                 c.create_text(x+15, 120, text=label, anchor="nw", fill=MUTED,
#                               font=("DejaVu Sans", 9))

#         actions = [
#             ("+", "Nova Chamada", "Registre um problema relatado por um\nusuário.", "Nova Chamada"),
#             ("⌕", "Consultar Chamadas", "Acompanhe o status e o histórico de todos\nos atendimentos.", "Consultar Chamadas"),
#             ("▱", "Cadastro de Computadores", "Mantenha o inventário das máquinas\natualizado.", "Computadores"),
#             ("♙", "Cadastro de Usuários", "Cadastre quem pode abrir chamados no\nsistema.", "Usuários"),
#             ("▥", "Relatórios", "Estatísticas dos atendimentos e categorias\nmais frequentes.", "Relatórios"),
#         ]
#         action_w, action_h, action_gap = 242, 123, 12
#         start_y = 175
#         for i, (icon, title, desc, destination) in enumerate(actions):
#             col, row = i % 3, i // 3
#             x = x0 + col * (action_w + action_gap)
#             y = start_y + row * (action_h + action_gap)
#             hovered = self.hover_tag == f"card:{title}"
#             self.rounded_rect(c, x, y, x+action_w, y+action_h, 12,
#                               fill="#fbfcff" if hovered else WHITE,
#                               outline="#cbd5ed" if hovered else BORDER, width=1)
#             self.rounded_rect(c, x+16, y+16, x+47, y+47, 9,
#                               fill=NAVY, outline=NAVY)
#             self.draw_icon(x+31.5, y+31.5, icon, 16, BLUE)
#             c.create_text(x+16, y+61, text=title, anchor="nw", fill=TEXT,
#                           font=("DejaVu Sans", 10, "bold"))
#             c.create_text(x+16, y+81, text=desc, anchor="nw", fill=MUTED,
#                           font=("DejaVu Sans", 9), justify="left", spacing1=2)
#             self.add_hitbox((x, y, x+action_w, y+action_h), ("card", destination))

#     def on_motion(self, event):
#         old = self.hover_tag
#         self.hover_tag = None
#         for coords, action in self.hitboxes:
#             x1, y1, x2, y2 = coords
#             if x1 <= event.x <= x2 and y1 <= event.y <= y2:
#                 self.hover_tag = f"{action[0]}:{action[1]}"
#                 break
#         if old != self.hover_tag:
#             self.draw()

#     def on_click(self, event):
#         for coords, action in self.hitboxes:
#             x1, y1, x2, y2 = coords
#             if x1 <= event.x <= x2 and y1 <= event.y <= y2:
#                 kind, destination = action
#                 if kind == "nav":
#                     self.active_item = destination
#                     self.draw()
#                 else:
#                     messagebox.showinfo(
#                         destination,
#                         f"Ação selecionada: {destination}\n\n"
#                         "Conecte este botão à tela ou funcionalidade correspondente do seu sistema.",
#                         parent=self,
#                     )
#                 return


# if __name__ == "__main__":
#     EvoLinkApp().mainloop()

from builtins import super
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

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
        self._configure_styles()
        self._build_shell()
        self.show_page("Início")

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

    def _build_topbar(self):
        brand = tk.Frame(self.topbar, bg=COLORS["surface"])
        brand.pack(side="left", padx=(25, 0), pady=13)

        mark = tk.Canvas(brand, width=38, height=38, bg=COLORS["surface"],
                         highlightthickness=0)
        mark.pack(side="left", padx=(0, 9))
        mark.create_line(5, 30, 5, 8, 12, 19, 19, 8, 19, 30,
                         fill=COLORS["orange"], width=2.6, joinstyle="round")
        mark.create_line(23, 30, 23, 8, 30, 19, 36, 8, 36, 30,
                         fill=COLORS["coral"], width=2.6, joinstyle="round")

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
        avatar.create_text(17, 17, text="MS", fill=COLORS["orange_dark"],
                           font=(FONT, 9, "bold"))
        info = tk.Frame(footer, bg=COLORS["surface"])
        info.pack(side="left", anchor="w")
        tk.Label(info, text="Mariana Silva", bg=COLORS["surface"], fg=COLORS["text"],
                 font=(FONT, 9, "bold")).pack(anchor="w")
        tk.Label(info, text="Administradora", bg=COLORS["surface"], fg=COLORS["muted"],
                 font=(FONT, 8)).pack(anchor="w")

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
        }
        routes.get(page, self._page_home)()

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
