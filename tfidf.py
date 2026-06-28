import math
import pandas as pd

class TfIdf:
    def __init__(self):
        self.vocabulario = {}
        self.idf = {}
        self.n_docs = 0
        self.ajustado = False

    def ajustar(self, documentos_tokenizados):
        self.n_docs = len(documentos_tokenizados)
        df = {}
        for tokens in documentos_tokenizados:
            tokens_unicos = set(tokens)
            for token in tokens_unicos:
                df[token] = df.get(token, 0) + 1

        vocabulario_ordenado = sorted(df.keys())
        self.vocabulario = {palabra: idx for idx, palabra in enumerate(vocabulario_ordenado)}

        N = self.n_docs
        self.idf = {palabra: math.log((N + 1) / (df[palabra] + 1)) + 1 for palabra in df}
        self.ajustado = True

    def transformar(self, documentos_tokenizados):
        if not self.ajustado:
            raise RuntimeError("Debes llamar a ajustar() antes de transformar()")
        palabras = list(self.vocabulario.keys())
        filas = [self._calcular_vector_tfidf(tokens) for tokens in documentos_tokenizados]
        return pd.DataFrame(filas, columns=palabras)

    def transformar_uno(self, tokens):
        if not self.ajustado:
            raise RuntimeError("Debes llamar a ajustar() antes de transformar_uno()")
        vector = self._calcular_vector_tfidf(tokens)
        return vector

    def _calcular_tf(self, tokens):
        tf = {}
        total = len(tokens)
        if total == 0:
            return tf
        for token in tokens:
            tf[token] = tf.get(token, 0) + 1
        for token in tf:
            tf[token] /= total
        return tf

    def _calcular_vector_tfidf(self, tokens):
        tf = self._calcular_tf(tokens)
        vector = [0.0] * len(self.vocabulario)
        for token, valor_tf in tf.items():
            if token in self.vocabulario:
                idx = self.vocabulario[token]
                vector[idx] = valor_tf * self.idf.get(token, 0.0)
        return vector