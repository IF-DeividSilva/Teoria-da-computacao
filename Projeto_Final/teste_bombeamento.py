import tkinter as tk
from tkinter import filedialog


def verificar_igualdade_substr(s, p, q, r):
    if p == q or q == r:
        return False
    return s[p:q] == s[q:r]

def lema_bombeamento(linguagem, n):
    for s in linguagem:
        if len(s) >= n:
            for i in range(len(s) - n + 1):
                for j in range(i + 1, len(s) + 1):
                    if j - i < n:
                        continue
                    if verificar_igualdade_substr(s, i, i + n, j):
                        return False
    return True

def verificar_linguagens():
    nome_arquivo = entry_nome_arquivo.get()
    n = int(entry_n.get())
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linguagens = arquivo.readlines()

        linguagens = [linha.strip() for linha in linguagens]

        todas_regulares = True

        result_text.delete(1.0, tk.END)

        for i, linguagem in enumerate(linguagens):
            if lema_bombeamento([linguagem], n):
                result_text.insert(tk.END, f"Linguagem {i + 1}: '{linguagem}' pode ser regular.\n")
            else:
                result_text.insert(tk.END, f"Linguagem {i + 1}: '{linguagem}' não é regular.\n")
                todas_regulares = False

        if todas_regulares:
            result_text.insert(tk.END, "Todas as linguagens no arquivo são regulares.")
        else:
            result_text.insert(tk.END, "Pelo menos uma das linguagens no arquivo pode não ser regular.")

    except FileNotFoundError:
        result_text.insert(tk.END, f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        result_text.insert(tk.END, f"Ocorreu um erro: {str(e)}")

def selecionar_arquivo():
    nome_arquivo = filedialog.askopenfilename()
    entry_nome_arquivo.delete(0, tk.END)
    entry_nome_arquivo.insert(0, nome_arquivo)

# Cria a janela principal
root = tk.Tk()
root.title("Verificação de Linguagens Regulares")

# Rótulo e entrada para o nome do arquivo
label_nome_arquivo = tk.Label(root, text="Nome do Arquivo:")
label_nome_arquivo.pack()
entry_nome_arquivo = tk.Entry(root)
entry_nome_arquivo.pack()

# Botão para selecionar o arquivo
button_selecionar = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
button_selecionar.pack()

# Rótulo e entrada para o valor de n
label_n = tk.Label(root, text="Valor de n:")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Botão para verificar as linguagens
button_verificar = tk.Button(root, text="Verificar Linguagens", command=verificar_linguagens)
button_verificar.pack()

# Área de texto para exibir os resultados
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()

#verificar_linguagens_em_arquivo(nome_arquivo, n)
