from textblob import TextBlob

class AnalizadorSentimiento:
    @staticmethod
    def analizar(texto):
        return TextBlob(texto).sentiment.polarity