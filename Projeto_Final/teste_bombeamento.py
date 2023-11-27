import tkinter as tk

def lema_bombeamento(palavra):
 # Obtém o comprimento da palavra.
 k=0
 comprimento = len(palavra)

 # Define o valor de p como o menor divisor de comprimento que é maior ou igual a 2.
 i = int(input_i.get())
 # Obtém as sequências u, v e z.
 u = palavra[0]
 v = palavra[1]
 z = palavra[2:] 

 # Verifica se a palavra montada é igual à palavra formada.
 palavra_montada = u + v + z
 palavra_formada = ""
 palavra_formada += u
 for k in range(0, i):
  palavra_formada += v
  i-=1
 palavra_formada += z

 if palavra_montada == palavra_formada:
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

#implementar um loop para formar as palavras da linguagem atravéz do p da palavra inserida
# pesquisar no vetor de palavras se ela pertence a linguagem.
