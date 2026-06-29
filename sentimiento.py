from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

class AnalizadorSentimiento:
    @staticmethod
    def analizar(texto):
        return TextBlob(texto).sentiment.polarity

    @staticmethod
    def graficar_evolucion_por_libro(versiculos):
        print("Calculando sentimiento por libro (esto puede tardar unos segundos)...")
        datos = []
        for v in versiculos:
            polaridad = AnalizadorSentimiento.analizar(v.texto)
            datos.append({'Libro': v.nombre_libro, 'Polaridad': polaridad})
        
        df = pd.DataFrame(datos)
        sentimiento_promedio = df.groupby('Libro')['Polaridad'].mean().reindex(df['Libro'].unique())

        plt.figure(figsize=(14, 6))
        sentimiento_promedio.plot(kind='bar', color='skyblue')
        plt.title('Evolución del Sentimiento Promedio por Libro Bíblico')
        plt.xlabel('Libro')
        plt.ylabel('Polaridad Promedio (TextBlob)')
        plt.xticks(rotation=90, fontsize=8)
        plt.axhline(0, color='red', linestyle='--')
        plt.tight_layout()
        plt.show()