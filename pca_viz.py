import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

class VisualizadorPCA:
    def __init__(self, matriz_tfidf, versiculos):
        self.matriz = matriz_tfidf
        self.versiculos = versiculos

    def graficar(self):
        pca = PCA(n_components=2)
        componentes = pca.fit_transform(self.matriz)
        colores = ['#00FF00' if v.numero_libro < 40 else 'magenta' for v in self.versiculos]

        plt.figure(figsize=(10, 7))
        plt.scatter(componentes[:, 0], componentes[:, 1], c=colores, alpha=0.5, s=10)
        plt.title('PCA: Distribución de Versículos (Cian=Antiguo, Magenta=Nuevo)')
        plt.xlabel('Componente Principal 1')
        plt.ylabel('Componente Principal 2')
        plt.show()