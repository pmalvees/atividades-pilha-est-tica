def checa_parenteses(string):
  pilha = Pilha()
  for char in string:
    if char == '(':
      pilha.empilha(char)
    elif char == ')':
      try:
        pilha.desempilha()
      except Exception:
        return False

  return True if pilha.esta_vazia() else False