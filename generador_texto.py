import random
from collections import defaultdict

class GeneradorTexto:
    def __init__(self, textos_tokenizados):
        self.textos = textos_tokenizados
        self.unigramas = []
        self.bigramas = defaultdict(list)
        self.trigramas = defaultdict(list)
        self._construir_modelos()

    def _construir_modelos(self):
        for tokens in self.textos:
            secuencia = ['<START>'] + tokens + ['<END>']
            for i in range(len(secuencia)):
                self.unigramas.append(secuencia[i])
                if i < len(secuencia) - 1:
                    self.bigramas[secuencia[i]].append(secuencia[i+1])
                if i < len(secuencia) - 2:
                    self.trigramas[(secuencia[i], secuencia[i+1])].append(secuencia[i+2])

    def generar_unigrama(self, longitud_max=15):
        resultado = []
        for _ in range(longitud_max):
            palabra = random.choice(self.unigramas)
            if palabra == '<END>': break
            if palabra != '<START>': resultado.append(palabra)
        return " ".join(resultado)

    def generar_bigrama(self, palabra_inicial='<START>', longitud_max=15):
        resultado = []
        palabra_actual = palabra_inicial
        for _ in range(longitud_max):
            if palabra_actual not in self.bigramas: break
            siguiente = random.choice(self.bigramas[palabra_actual])
            if siguiente == '<END>': break
            if siguiente != '<START>': resultado.append(siguiente)
            palabra_actual = siguiente
        return " ".join(resultado)

    def generar_trigrama(self, palabra1='<START>', palabra2=None, longitud_max=15):
        resultado = []
        if palabra2 is None:
            if palabra1 not in self.bigramas: return ""
            palabra2 = random.choice(self.bigramas[palabra1])
        
        if palabra1 != '<START>': resultado.append(palabra1)
        if palabra2 != '<START>' and palabra2 != '<END>': resultado.append(palabra2)
        
        p1, p2 = palabra1, palabra2
        for _ in range(longitud_max - len(resultado)):
            if (p1, p2) not in self.trigramas: break
            siguiente = random.choice(self.trigramas[(p1, p2)])
            if siguiente == '<END>': break
            resultado.append(siguiente)
            p1, p2 = p2, siguiente
        return " ".join(resultado)