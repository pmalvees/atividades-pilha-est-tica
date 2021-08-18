class Pilha1:
    def __init__(self):
        self.elementos = []
        self.tamanho = 0

    def empilha(self, valor):
        self.elementos.append(valor)
        self.tamanho += 1
        return valor

    def desempilha(self):
        if self.esta_vazia():
            raise Exception('Pilha Vazia, operação não pode ser realizada')
        else:
            topo = self.topo()
            self.elementos = self.elementos[:-1]
            self.tamanho -= 1
            return topo

    def topo(self):
        return self.elementos[-1]

    def retorna_todos_elementos(self):
        for elemento in self.elementos:
            yield elemento

    def esta_vazia(self):
        return self.tamanho == 0

    def menor_elemento(self):
        if self.esta_vazia():
            raise Exception('Pilha Vazia, operação não pode ser realizada')
        else:
            elementos_copia = list(self.retorna_todos_elementos())
            elementos_copia.sort()
            return elementos_copia[0]

    def maior_elemento(self):
        if self.esta_vazia():
            raise Exception('Pilha Vazia, operação não pode ser realizada')
        else:
            elementos_copia = list(self.retorna_todos_elementos())
            print(elementos_copia)
            elementos_copia.sort(reverse=True)
            return elementos_copia[0]

    def media_elementos(self):
        if self.esta_vazia():
            raise Exception('Pilha Vazia, operação não pode ser realizada')
        else:
            soma = 0
            for elemento in self.elementos:
                soma += elemento
            return soma / self.tamanho

    def comparar(self, pilha12):
        if self.tamanho != pilha12.tamanho:
            return False
        else:
            iguais = True
            elementos_2 = list(pilha12.retorna_todos_elementos())
            for i in range(self.tamanho):
                if not self.elementos[i] == elementos_2[i]:
                    iguais = False
                    break

            return iguais
