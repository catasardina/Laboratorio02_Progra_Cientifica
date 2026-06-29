from corpus_biblico import CorpusBiblico
from preprocesador import PreprocesadorTexto
from tfidf import TfIdf
from similitud import SimilitudCoseno
from visualizador import Visualizador
from pca_viz import VisualizadorPCA
from clasificador import ClasificadorBiblico
from sentimiento import AnalizadorSentimiento
from generador_texto import GeneradorTexto
import random

if __name__ == "__main__":
    corpus = CorpusBiblico('t_kjv.csv', 'key_english.csv')
    textos_crudos = corpus.obtener_textos()
    versiculos = corpus.obtener_todos_versiculos()

    preprocesador = PreprocesadorTexto()
    textos_tokenizados = preprocesador.preprocesar_varios(textos_crudos)
    preprocesador.construir_vocabulario(textos_tokenizados)

    tfidf = TfIdf()
    tfidf.ajustar(textos_tokenizados)
    df_tfidf = tfidf.transformar(textos_tokenizados)
    matriz_vectores = df_tfidf.values.tolist()

    print("Generando visualizaciones...")
    vis = Visualizador(versiculos, textos_tokenizados)
    vis.graficar_estadisticas_basicas()
    vis.graficar_heatmap_similitud(tfidf)
    
    pca = VisualizadorPCA(matriz_vectores, versiculos)
    pca.graficar()

    print("\nConstruyendo modelos de generación de texto...")
    generador = GeneradorTexto(textos_tokenizados)
    print("\n--- Ejemplos de Texto Generado ---")
    print("Unigrama:", generador.generar_unigrama())
    print("Bigrama:", generador.generar_bigrama())
    print("Trigrama:", generador.generar_trigrama(palabra1='in'))
    print("----------------------------------\n")

    print("Generando gráfico de evolución de sentimiento...")
    AnalizadorSentimiento.graficar_evolucion_por_libro(versiculos)

    print("\nEntrenando clasificador...")
    nombres_libros = [v.nombre_libro for v in versiculos]
    clasificador = ClasificadorBiblico(matriz_vectores, nombres_libros)
    clasificador.entrenar()
    print("Matriz de confusion:\n", clasificador.evaluar())

    print("\nEjemplo de sentimiento en primer versiculo:", 
          AnalizadorSentimiento.analizar(textos_crudos[0]))
    while True:
        consulta = input("\nIngresa tu busqueda (o 'salir'): ")
        if consulta.lower() == 'salir': break
        
        tokens_consulta = preprocesador.preprocesar(consulta)
        vector_consulta = tfidf.transformar_uno(tokens_consulta)
        puntajes = SimilitudCoseno.similitud_contra_matriz(vector_consulta, matriz_vectores)
        
        for indice, puntaje in SimilitudCoseno.top_k(puntajes, 3):
            if puntaje > 0:
                v = versiculos[indice]
                print(f"[{puntaje:.4f}] {v.nombre_libro} {v.capitulo}:{v.numero_versiculo} -> {v.texto}")