import tkinter as tk
from tkinter import ttk

def bombeamento():
    codigo = codigo_text.get("1.0", tk.END)
    n_bloco1 = 0
    n_bloco2 = 0
    pilha = []

    for i in codigo:
        if i == '0':
            n_bloco2 += 1
            if n_bloco2 == 10:
                pilha.append([0]*10)
                n_bloco2 = 0
        elif i == '1':
            n_bloco2 += 1
            if n_bloco2 == 10:
                pilha.append([1]*10)
                n_bloco2 = 0
                n_bloco1 += 1
        elif i == '*':
            n_bloco1 += 1
            n_bloco2 = 0

    resposta.delete("1.0", tk.END)
    resposta.insert(tk.END, "Resultados do bombeamento:\n")

    for row in pilha:
        for elem in row:
            resposta.insert(tk.END, str(elem) + " ")
        resposta.insert(tk.END, "\n")

    resposta.insert(tk.END, "\nNíveis:\n")
    for row in pilha:
        resposta.insert(tk.END, str(row.count(0)) + " - " + str(row.count(1)) + "\n")

    resposta.insert(tk.END, "\nTotal de 0s e 1s:\n")
    for row in pilha:
        resposta.insert(tk.END, str(row.count(0)) + " - " + str(row.count(1)) + "\n")

root = tk.Tk()
root.title("Lema do Bombeamento")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

codigo_text = tk.Text(mainframe, wrap=tk.WORD)
codigo_text.grid(column=0, row=0, sticky=(tk.W, tk.E))

botao = ttk.Button(mainframe, text="Bombeamento", command=bombeamento)
botao.grid(column=0, row=1, sticky=tk.W)

resposta = tk.Text(mainframe, wrap=tk.WORD)
resposta.grid(column=0, row=2, sticky=(tk.W, tk.E))

root.mainloop()