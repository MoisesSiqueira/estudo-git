import tkinter as tk
from tkinter import messagebox

class PadariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pedidos - Padaria")
        
        # Variáveis de controle
        self.pedido = tk.StringVar()
        self.pedido.set("")  # Inicializando o pedido vazio

        # Rótulo e caixa de entrada para o pedido
        lbl_pedido = tk.Label(root, text="Pedido:")
        lbl_pedido.pack()

        entry_pedido = tk.Entry(root, textvariable=self.pedido, width=30)
        entry_pedido.pack()

        # Botão para fazer o pedido
        btn_fazer_pedido = tk.Button(root, text="Fazer Pedido", command=self.fazer_pedido)
        btn_fazer_pedido.pack()

    def fazer_pedido(self):
        pedido_atual = self.pedido.get()
        if pedido_atual:
            messagebox.showinfo("Pedido Feito", f"Pedido realizado: {pedido_atual}")
            self.pedido.set("")  # Limpar a caixa de entrada após fazer o pedido
        else:
            messagebox.showwarning("Pedido Vazio", "Por favor, insira um pedido antes de fazer o pedido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PadariaApp(root)
    root.mainloop()
