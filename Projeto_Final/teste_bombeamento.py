import tkinter as tk
import itertools

def gerar_palavras(n):
   # Cria uma lista vazia para armazenar as palavras
   lista_palavras = []

   # aux = 1 - l1
   if aux == 1:
   # Adiciona 'a' e 'b' à palavra n vezes
    for i in range(n):
         lista_palavras.append('a' * (i + 1) + 'b' * (i + 1))
   #aux = 2 - l2
   if aux == 2:
    for i in range(100):
     for j in range(n):
        lista_palavras.append('a' * (i + 1) + 'b' * (j + 1))
   return lista_palavras

def lema_bombeamento(palavra):
 # Obtém o comprimento da palavra.
 comprimento = len(palavra)
 k=0
  # Verifica se todos os caracteres pertencem ao alfabeto {a, b}.
 if not all(c in 'ab' for c in palavra):
  raise ValueError("Caracter nao pertence ao alfabeto")

 lista_palavras = gerar_palavras(comprimento)

 #for p in lista_palavras:
   #print(p)

 # Define o valor de p como o menor divisor de comprimento que é maior ou igual a 2.

 #pega o valor de i do usuario 
 i = int(input_i.get())
 # Obtém as sequências u, v e z.
 u = palavra[0]
 v = palavra[1]
 z = palavra[2:] 

 # Verifica se a palavra montada pertence a linguagem
 palavra_montada = u + v + z
 palavra_formada = ""
 palavra_formada += u
 for k in range(0, i):
  palavra_formada += v
  i-=1
 palavra_formada += z

 if palavra_formada in lista_palavras:
  return True
 else:
  return False

def main():
 # Obtém a palavra digitada pelo usuário.
 palavra = input_palavra.get()

 # Aplica o lema do bombeamento.
 if lema_bombeamento(palavra):
  result_label.config(text="A LINGUAGEM PODE SER REGULAR")
 else:
  result_label.config(text="A LINGUAGEM NAO E REGULAR")

root = tk.Tk()
root.title("Lema do Bombeamento")
root.geometry('300x150') # Define o tamanho inicial da janela

# Cria um menu de opções para escolher a linguagem
def escolha_linguagem(*args):
  global linguagem
  linguagem = linguagem_var.get()
   # Atribui o valor de aux com base na escolha do usuário
  global aux
  if linguagem == "L={ a^n b^n | n ≥ 0}":
     aux = 1
  elif linguagem == "L={ a^m b^n | n ≥ 0 e m ≥ 0}":
     aux = 2

# Cria uma variável para armazenar a linguagem selecionada
linguagem_var = tk.StringVar(root)
linguagem_var.set("L={ a^n b^n | n ≥ 0}") # valor padrão
linguagem_var.trace("w", escolha_linguagem)

# Adiciona o menu de opções à janela
optionmenu = tk.OptionMenu(root, linguagem_var, "L={ a^n b^n | n ≥ 0}", "L={ a^m b^n | n ≥ 0 e m ≥ 0}")
optionmenu.pack()

palavra_label = tk.Label(root, text="Palavra: ")
palavra_label.pack()

input_palavra = tk.Entry(root)
input_palavra.pack()

i_label = tk.Label(root, text="Valor de i: ")
i_label.pack()

input_i = tk.Entry(root)
input_i.pack()

result_label = tk.Label(root, text="")
result_label.pack()

button = tk.Button(root, text="Verificar", command=main)
button.pack()


root.mainloop()
