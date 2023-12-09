def lema_do_bombeamento(p: int, u: str, v: str, z: str) -> bool:
  """
  Implementação do lema do bombeamento.

  Args:
    p: O valor de p.
    u: A palavra u.
    v: A palavra v.
    z: A palavra z.

  Returns:
    True se a linguagem é regular, False caso contrário.
  """

  if len(u) + len(v) + len(z) != 2 * p:
    return False

  # Construindo a palavra formada

  palavra_formada = u + v + z

  # Verificando se a palavra formada é igual à palavra original

  if palavra_formada == p * "a" + p * "b":
    return True

  # Construindo a palavra w

  w = palavra_formada[:p] + v

  # Verificando se w é uma subpalavra da palavra original

  if w in palavra_formada:
    return True

  return False
2

if __name__ == "__main__":
  # Pegando os valores de entrada

  p = int(input("Digite o valor de p: "))
  u = input("Digite o valor de U: ")
  v = input("Digite o valor de V: ")
  z = input("Digite o valor de Z: ")

  # Verificando se a linguagem é regular

  if lema_do_bombeamento(p, u, v, z):
    print("A LINGUAGEM PODE SER REGULAR")
  else:
    print("A LINGUAGEM NÃO É REGULAR")
