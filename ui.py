import tkinter as tk
from tkinter import font
import random
from game import criar_baralho, calcular_pontos, valores  # Importar o dicionário valores

class BlackJackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Jack")
        
        self.cartas_disponiveis = criar_baralho()
        self.mao_jogador = []
        self.pontos_atual = 0
        self.pontos_final = 0
        self.nome_jogador = ""
        self.histórico = []  # Lista para armazenar o histórico dos últimos 5 jogos

        # Configuração da fonte para os botões
        self.font_padrao = font.Font(size=14)

        # Entrada do nome do jogador
        self.nome_label = tk.Label(root, text="Digite seu nome:", font=self.font_padrao)
        self.nome_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.nome_entry = tk.Entry(root, font=self.font_padrao)
        self.nome_entry.grid(row=1, column=0, columnspan=3, pady=10)
        
        self.start_button = tk.Button(root, text="Iniciar Jogo", command=self.iniciar_jogo, font=self.font_padrao, width=20)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Labels
        self.nome_jogador_label = tk.Label(root, text="", font=self.font_padrao)
        self.nome_jogador_label.grid(row=0, column=0, padx=10, sticky="w")
        
        self.pontos_atual_label = tk.Label(root, text=f"Pontos Atuais: {self.pontos_atual}", font=self.font_padrao)
        self.pontos_atual_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.status_label = tk.Label(root, text="", font=self.font_padrao)
        self.status_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Botões
        self.pegar_carta_button = tk.Button(root, text="Pegar Carta", command=self.pegar_carta, font=self.font_padrao, width=20)
        self.parar_button = tk.Button(root, text="Parar", command=self.parar, font=self.font_padrao, width=20)
        self.jogar_novamente_button = tk.Button(root, text="Jogar Novamente", command=self.restart, font=self.font_padrao, width=20)
        self.exit_button = tk.Button(root, text="Sair do Jogo", command=self.sair, font=self.font_padrao, width=20)

        # Configurar layout dos botões
        self.pegar_carta_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        self.parar_button.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
        self.jogar_novamente_button.grid(row=6, column=2, padx=10, pady=10, sticky="ew")
        self.exit_button.grid(row=7, column=0, columnspan=3, pady=10, sticky="ew")

        # Configurar histórico de jogos
        self.histórico_label = tk.Label(root, text="Histórico da Última Jogada", font=self.font_padrao)
        self.histórico_label.grid(row=8, column=0, columnspan=3, pady=10)

        self.histórico_listbox = tk.Listbox(root, height=5, width=50, font=self.font_padrao)
        self.histórico_listbox.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Adicionar barra de rolagem
        self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.histórico_listbox.yview)
        self.scrollbar.grid(row=9, column=3, sticky="ns")
        self.histórico_listbox.config(yscrollcommand=self.scrollbar.set)

        # Ajusta o tamanho da janela
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Ajustar colunas para expandir igualmente
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Desabilitar botões de jogo até que o nome seja inserido e o jogo comece
        self.pegar_carta_button.config(state=tk.DISABLED)
        self.parar_button.config(state=tk.DISABLED)
        self.jogar_novamente_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.NORMAL)

    def iniciar_jogo(self):
        """Inicia o jogo e configura o nome do jogador."""
        self.nome_jogador = self.nome_entry.get()
        if not self.nome_jogador:
            self.status_label.config(text="Por favor, insira seu nome antes de começar o jogo.")
            return
        
        self.cartas_disponiveis = criar_baralho()
        random.shuffle(self.cartas_disponiveis)
        self.mao_jogador = []
        self.pontos_atual = 0
        self.pontos_final = 0
        self.pontos_atual_label.config(text=f"Pontos Atuais: {self.pontos_atual}")
        self.nome_jogador_label.config(text=self.nome_jogador)  # Exibe apenas o nome do jogador
        self.status_label.config(text="Bem-vindo ao Black Jack! Boa sorte!")
        self.nome_label.grid_forget()
        self.nome_entry.grid_forget()
        self.start_button.grid_forget()
        self.pegar_carta_button.config(state=tk.NORMAL)
        self.parar_button.config(state=tk.NORMAL)
        self.jogar_novamente_button.config(state=tk.DISABLED)
        self.exit_button.config(state=tk.NORMAL)

        # Limpar a mão do jogador
        self.mao_jogador = []

    def atualizar_histórico(self):
        """Atualiza o histórico com o nome do jogador e a pontuação final da última jogada."""
        if len(self.histórico) >= 5:
            self.histórico.pop(0)  # Remove o item mais antigo se houver mais de 5 itens

        self.histórico.append(f"{self.nome_jogador}: {self.pontos_final}")
        self.histórico_listbox.delete(0, tk.END)  # Limpa o histórico
        for entrada in reversed(self.histórico):
            self.histórico_listbox.insert(tk.END, entrada)

    def pegar_carta(self):
        if not self.cartas_disponiveis:
            self.status_label.config(text="O baralho acabou. Não há mais cartas para pegar.")
            return
        
        carta = self.cartas_disponiveis.pop()
        self.mao_jogador.append(carta)
        valor = valores[carta.split()[0]]  # Usa o dicionário valores importado
        self.pontos_atual = calcular_pontos(self.mao_jogador)
        
        if self.pontos_atual > 21:
            self.pontos_final = self.pontos_atual
            self.status_label.config(text=f"Você pegou: {carta} - Valor: {valor}. Você ultrapassou 21 pontos. Você perdeu!")
            self.pegar_carta_button.config(state=tk.DISABLED)
            self.parar_button.config(state=tk.DISABLED)
            self.jogar_novamente_button.config(state=tk.NORMAL)
            self.atualizar_histórico()
        else:
            self.status_label.config(text=f"Você pegou: {carta} - Valor: {valor}.")
        self.pontos_atual_label.config(text=f"Pontos Atuais: {self.pontos_atual}")

    def parar(self):
        self.pontos_final = self.pontos_atual
        self.status_label.config(text=f"Você parou. Seu total de pontos finais: {self.pontos_final}.")
        self.pegar_carta_button.config(state=tk.DISABLED)
        self.parar_button.config(state=tk.DISABLED)
        self.jogar_novamente_button.config(state=tk.NORMAL)
        self.atualizar_histórico()

    def restart(self):
        """Reinicia o jogo para um novo jogador."""
        self.nome_label.grid(row=0, column=0, columnspan=3, pady=10)
        self.nome_entry.grid(row=1, column=0, columnspan=3, pady=10)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.pontos_atual_label.config(text=f"Pontos Atuais: {self.pontos_atual}")
        self.nome_jogador_label.config(text="")
        self.status_label.config(text="Bem-vindo ao Black Jack!")
        self.pegar_carta_button.config(state=tk.DISABLED)
        self.parar_button.config(state=tk.DISABLED)
        self.jogar_novamente_button.config(state=tk.DISABLED)
        
        # Limpar a mão do jogador e resetar os pontos
        self.mao_jogador = []
        self.pontos_atual = 0
        self.pontos_atual_label.config(text=f"Pontos Atuais: {self.pontos_atual}")

    def sair(self):
        """Fecha a aplicação."""
        self.root.quit()
