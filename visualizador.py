import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizador:
    def __init__(self, corpus, matriz_tfidf):
        self.corpus = corpus
        self.matriz_tfidf = matriz_tfidf
        self.datos = self.corpus.datos

    def graficar_estadisticas_basicas(self):
        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        longitudes = self.datos['Tokens'].apply(len)
        sns.histplot(longitudes, bins=50, kde=True, ax=axes[0], color='coral') # <-- CAMBIAR COLOR
        axes[0].set_title('Distribución de Longitud de Versículos')
        axes[0].set_xlabel('Cantidad de Palabras (Tokens)')
        axes[0].set_ylabel('Frecuencia')

        conteo_libros = self.datos['b'].value_counts().head(20)
        ids_libros_str = conteo_libros.index.astype(str)
        sns.barplot(x=conteo_libros.values, y=ids_libros_str, ax=axes[1], palette='magma', hue=ids_libros_str, legend=False) # <-- CAMBIAR PALETA
        axes[1].set_title('Top 20 Libros con Más Versículos')
        axes[1].set_xlabel('Cantidad de Versículos')
        axes[1].set_ylabel('ID del Libro')

        plt.tight_layout()
        plt.show()

    def graficar_heatmap_similitud(self, vectorizador):
        print("Calculando similitud entre libros para el heatmap...")
        
        libros = self.datos['b'].unique()
        tokens_por_libro = []
        nombres_libros = []

        for libro in libros:
            tokens_libro = []
            for tokens in self.datos[self.datos['b'] == libro]['Tokens']:
                tokens_libro.extend(tokens)
            tokens_por_libro.append(tokens_libro)
            nombres_libros.append(libro)

        matriz_tfidf_libros = vectorizador.transformar_tfidf(tokens_por_libro)
        num_libros = len(libros)
        
        matriz_similitud = np.zeros((num_libros, num_libros))
        for i in range(num_libros):
            vec_i = matriz_tfidf_libros[i]
            similitudes = vectorizador.similitud_coseno(vec_i, matriz_tfidf_libros)
            matriz_similitud[i] = similitudes

        plt.figure(figsize=(12, 10))
        sns.heatmap(matriz_similitud, xticklabels=nombres_libros, yticklabels=nombres_libros, cmap='plasma')
        plt.title('Matriz de Similitud del Coseno entre Libros de la Biblia')
        plt.xlabel('Libros')
        plt.ylabel('Libros')
        plt.tight_layout()
        plt.show()