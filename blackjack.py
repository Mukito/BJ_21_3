import tkinter as tk
from tkinter import PhotoImage
from ui import BlackJackUI

def main():
    root = tk.Tk()
    root.title("Black Jack")

    # Definir o ícone da janela
    try:
        # Subistitua pelo caminho para o seu icone.png
        icon = PhotoImage(file='icon/cartas.png')
        root.iconphoto(False, icon)
    except Exception as e:
        print(f"Erro ao carregar o ícone: {e}")

    #root.iconbitmap('icon/cartas.png')  # Substitua pelo caminho para o seu ícone .ico

    app = BlackJackUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
