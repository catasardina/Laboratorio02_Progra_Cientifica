import random
from collections import defaultdict, Counter

class GeneradorTexto:
    def __init__(self, textos_tokenizados):
        self.modelo = defaultdict(Counter)
        for tokens in textos_tokenizados:
            for i in range(len(tokens) - 2):
                grama = (tokens[i], tokens[i+1])
                self.modelo[grama][tokens[i+2]] += 1

    def generar(self, inicio, largo=15):
        resultado = [inicio[0], inicio[1]]
        for _ in range(largo):
            siguiente = self.modelo[tuple(resultado[-2:])].most_common(1)
            if not siguiente: break
            resultado.append(siguiente[0][0])
        return " ".join(resultado)