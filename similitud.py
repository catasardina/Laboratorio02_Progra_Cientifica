import math

class SimilitudCoseno:
    @staticmethod
    def similitud(vec_a, vec_b):
        punto = sum(a * b for a, b in zip(vec_a, vec_b))
        norma_a = math.sqrt(sum(x ** 2 for x in vec_a))
        norma_b = math.sqrt(sum(x ** 2 for x in vec_b))
        if norma_a == 0.0 or norma_b == 0.0:
            return 0.0
        return punto / (norma_a * norma_b)

    @staticmethod
    def similitud_contra_matriz(vector_consulta, matriz):
        return [SimilitudCoseno.similitud(vector_consulta, vector_doc) for vector_doc in matriz]

    @staticmethod
    def top_k(puntajes, k):
        indexado = [(i, s) for i, s in enumerate(puntajes)]
        indexado.sort(key=lambda x: x[1], reverse=True)
        return indexado[:k]
    
    @staticmethod
    def matriz_similitud(vectores):
        n = len(vectores)
        matriz = [[0.0] * n for _ in range(n)]
        for i in range(n):
            matriz[i][i] = 1.0
            for j in range(i + 1, n):
                sim = SimilitudCoseno.similitud(vectores[i], vectores[j])
                matriz[i][j] = sim
                matriz[j][i] = sim
        return matriz