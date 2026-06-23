import numpy as np
from collections import Counter

class TextVectorizer:
    def __init__(self, vocabulario):
        self.vocabulario = vocabulario
        self.indice_vocabulario = {palabra: idx for idx, palabra in enumerate(self.vocabulario)}
        self.idf = {}

    def calcular_tf(self, tokens):
        diccionario_tf = Counter(tokens)
        longitud_doc = len(tokens)
        if longitud_doc == 0:
            return {}
        return {palabra: conteo / longitud_doc for palabra, conteo in diccionario_tf.items()}

    def ajustar_idf(self, documentos_tokens):
        N = len(documentos_tokens)
        diccionario_df = {}
        
        for tokens in documentos_tokens:
            palabras_unicas = set(tokens)
            for palabra in palabras_unicas:
                if palabra in diccionario_df:
                    diccionario_df[palabra] += 1
                else:
                    diccionario_df[palabra] = 1

        for palabra, df in diccionario_df.items():
            self.idf[palabra] = np.log((1 + N) / (1 + df)) + 1

    def transformar_tfidf(self, documentos_tokens):
        num_docs = len(documentos_tokens)
        tamano_vocabulario = len(self.vocabulario)
        
        matriz_tfidf = np.zeros((num_docs, tamano_vocabulario), dtype=np.float32)

        for i, tokens in enumerate(documentos_tokens):
            tf = self.calcular_tf(tokens)
            for palabra, valor_tf in tf.items():
                if palabra in self.indice_vocabulario:
                    col_idx = self.indice_vocabulario[palabra]
                    matriz_tfidf[i, col_idx] = valor_tf * self.idf.get(palabra, 0)

        return matriz_tfidf

    def similitud_coseno(self, vector_a, matriz_b):
        producto_punto = np.dot(matriz_b, vector_a)
        norma_a = np.linalg.norm(vector_a)
        norma_b = np.linalg.norm(matriz_b, axis=1)
        similitud = np.divide(producto_punto, (norma_a * norma_b), out=np.zeros_like(producto_punto), where=(norma_a * norma_b) != 0)
        return similitud