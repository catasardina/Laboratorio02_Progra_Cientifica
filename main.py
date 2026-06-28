from corpus_biblico import CorpusBiblico
from preprocesador import PreprocesadorTexto
from tfidf import TfIdf
from similitud import SimilitudCoseno
from visualizador import Visualizador

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

   
    consulta = "in the beginning god created the heaven and the earth"
    tokens_consulta = preprocesador.preprocesar(consulta)
    vector_consulta = tfidf.transformar_uno(tokens_consulta)

    puntajes = SimilitudCoseno.similitud_contra_matriz(vector_consulta, matriz_vectores)
    mejores_resultados = SimilitudCoseno.top_k(puntajes, 5)

    print(f"\nBuscando: '{consulta}'\n")
    for indice, puntaje in mejores_resultados:
        if puntaje > 0:
            v = versiculos[indice]
            print(f"[{puntaje:.4f}] {v.nombre_libro} {v.capitulo}:{v.numero_versiculo} -> {v.texto}")

    print("\nGenerando visualizaciones exploratorias...")
    vis = Visualizador(versiculos, textos_tokenizados)
    
    print("Mostrando estadísticas básicas...")
    vis.graficar_estadisticas_basicas()
    
    print("Mostrando heatmap de similitud...")
    vis.graficar_heatmap_similitud(tfidf)