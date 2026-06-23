from biblical_corpus import BiblicalCorpus
from text_vectorizer import TextVectorizer

if __name__ == "__main__":
    corpus = BiblicalCorpus('t_kjv.csv')
    df = corpus.cargar_datos()
    corpus.aplicar_preprocesamiento()

    vectorizador = TextVectorizer(corpus.vocabulario)
    vectorizador.ajustar_idf(df['Tokens'])
    matriz_tfidf = vectorizador.transformar_tfidf(df['Tokens'])

    print(f"Dimensiones de la matriz: {matriz_tfidf.shape}")