import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from similitud import SimilitudCoseno

class Visualizador:
    def __init__(self, versiculos, textos_tokenizados):
        self.versiculos = versiculos
        self.textos_tokenizados = textos_tokenizados

        self.df = pd.DataFrame({
            'Tokens': textos_tokenizados,
            'b': [v.nombre_libro for v in versiculos]
        })

    def graficar_estadisticas_basicas(self):
        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        longitudes = self.df['Tokens'].apply(len)
        sns.histplot(longitudes, bins=50, kde=True, ax=axes[0], color='coral')
        axes[0].set_title('Distribución de Longitud de Versículos')
        axes[0].set_xlabel('Cantidad de Palabras (Tokens)')
        axes[0].set_ylabel('Frecuencia')

        conteo_libros = self.df['b'].value_counts().head(20)
        nombres_libros_str = conteo_libros.index.astype(str)
        
        sns.barplot(x=conteo_libros.values, y=nombres_libros_str, ax=axes[1], palette='magma', hue=nombres_libros_str, legend=False)
        axes[1].set_title('Top 20 Libros con Más Versículos')
        axes[1].set_xlabel('Cantidad de Versículos')
        axes[1].set_ylabel('Libro')

        plt.tight_layout()
        plt.show()

    def graficar_heatmap_similitud(self, tfidf):
        print("Calculando similitud entre libros para el heatmap...")
        
        libros = self.df['b'].unique()
        tokens_por_libro = []
        nombres_libros = []

        for libro in libros:
            tokens_libro = []
            for tokens in self.df[self.df['b'] == libro]['Tokens']:
                tokens_libro.extend(tokens)
            tokens_por_libro.append(tokens_libro)
            nombres_libros.append(libro)

       
        matriz_tfidf_libros = tfidf.transformar(tokens_por_libro).values.tolist()
        
        matriz_similitud = SimilitudCoseno.matriz_similitud(matriz_tfidf_libros)

        plt.figure(figsize=(12, 10))
        sns.heatmap(matriz_similitud, xticklabels=nombres_libros, yticklabels=nombres_libros, cmap='plasma')
        plt.title('Matriz de Similitud del Coseno entre Libros de la Biblia')
        plt.xlabel('Libros')
        plt.ylabel('Libros')
        plt.tight_layout()
        plt.show()