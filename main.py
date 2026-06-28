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

    vis = Visualizador(versiculos, textos_tokenizados)
    vis.graficar_estadisticas_basicas()
    vis.graficar_heatmap_similitud(tfidf)

    while True:
        consulta = input("\nIngresa tu busqueda (o 'salir' para terminar): ")
        if consulta.lower() == 'salir':
            break
            
        tokens_consulta = preprocesador.preprocesar(consulta)
        if not tokens_consulta:
            print("Consulta no valida o solo contiene palabras vacias.")
            continue
            
        vector_consulta = tfidf.transformar_uno(tokens_consulta)
        puntajes = SimilitudCoseno.similitud_contra_matriz(vector_consulta, matriz_vectores)
        mejores_resultados = SimilitudCoseno.top_k(puntajes, 5)

        hay_resultados = False
        for indice, puntaje in mejores_resultados:
            if puntaje > 0:
                hay_resultados = True
                v = versiculos[indice]
                print(f"[{puntaje:.4f}] {v.nombre_libro} {v.capitulo}:{v.numero_versiculo} -> {v.texto}")
        
        if not hay_resultados:
            print("No se encontraron coincidencias para tu busqueda.")