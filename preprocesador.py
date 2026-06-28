import re
import string

PALABRAS_VACIAS = {
    'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'shall', 'can', 'that', 'this',
    'it', 'its', 'he', 'she', 'they', 'we', 'i', 'you', 'his', 'her',
    'their', 'our', 'my', 'your', 'not', 'no', 'nor', 'so', 'yet', 'both',
    'either', 'neither', 'as', 'if', 'then', 'than', 'because', 'while',
    'although', 'though', 'unto', 'upon', 'thee', 'thou', 'thy', 'ye',
    'hath', 'doth', 'shalt', 'thereof', 'therein', 'whereby', 'wherein',
    'him', 'them', 'us', 'me', 'who', 'which', 'what', 'when', 'where',
    'how', 'all', 'any', 'every', 'each', 'one', 'also', 'into', 'up',
    'out', 'about', 'after', 'before', 'over', 'under', 'again', 'there',
    'here', 'through', 'during', 'same', 'own', 'more', 'most', 'other',
    'such', 'only', 'just', 'even', 'now', 'very'
}

class PreprocesadorTexto:
    def __init__(self):
        self.palabras_vacias = PALABRAS_VACIAS
        self.vocabulario = {}
        self.frecuencia_palabras = {}

    def preprocesar(self, texto):
        texto = texto.lower()
        texto = texto.translate(str.maketrans('', '', string.punctuation))
        texto = re.sub(r'[^a-z\s]', '', texto)
        tokens = texto.split()
        return [t for t in tokens if t not in self.palabras_vacias]

    def preprocesar_varios(self, textos):
        return [self.preprocesar(t) for t in textos]

    def construir_vocabulario(self, textos_tokenizados):
        frecuencia = {}
        for tokens in textos_tokenizados:
            for token in tokens:
                frecuencia[token] = frecuencia.get(token, 0) + 1
        self.frecuencia_palabras = frecuencia
        palabras_ordenadas = sorted(frecuencia.keys())
        self.vocabulario = {palabra: idx for idx, palabra in enumerate(palabras_ordenadas)}