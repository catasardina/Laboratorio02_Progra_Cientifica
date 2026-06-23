import pandas as pd
import re
import string
from collections import Counter

class BiblicalCorpus:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.datos = pd.DataFrame()
        self.vocabulario = set()
        self.frecuencia_palabras = Counter()
        self.palabras_vacias = {
            "el", "la", "los", "las", "un", "una", "unos", "unas",
            "y", "o", "de", "en", "a", "que", "por", "para", "con",
            "su", "sus", "al", "del", "se", "no", "como", "más", "pero",
            "le", "les", "me", "te", "lo", "ya", "ha", "han"
        }

    def cargar_datos(self):
        self.datos = pd.read_csv(self.ruta_archivo, header=0, names=['id', 'b', 'c', 'v', 't'])
        return self.datos

    def preprocesar_texto(self, texto):
        if not isinstance(texto, str):
            return []
        
        texto = texto.lower()
        texto = re.sub(f'[{re.escape(string.punctuation)}0-9]', ' ', texto)
        tokens = texto.split()
        
        return [palabra for palabra in tokens if palabra not in self.palabras_vacias]

    def aplicar_preprocesamiento(self):
        self.datos['Tokens'] = self.datos['t'].apply(self.preprocesar_texto)
        
        for tokens in self.datos['Tokens']:
            self.vocabulario.update(tokens)
            self.frecuencia_palabras.update(tokens)
            
        self.vocabulario = sorted(list(self.vocabulario))
        return self.datos