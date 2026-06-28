import pandas as pd

class Versiculo:
    def __init__(self, numero_libro, nombre_libro, capitulo, numero_versiculo, texto):
        self.numero_libro = numero_libro
        self.nombre_libro = nombre_libro
        self.capitulo = capitulo
        self.numero_versiculo = numero_versiculo
        self.texto = texto

class CorpusBiblico:
    ANTIGUO_TESTAMENTO = set(range(1, 40))
    NUEVO_TESTAMENTO = set(range(40, 67))

    def __init__(self, ruta_versiculos, ruta_libros):
        self.df_libros = pd.read_csv(ruta_libros)
        self.df_versiculos = pd.read_csv(ruta_versiculos, header=0, names=['id', 'b', 'c', 'v', 't'])
        self.nombres_libros = dict(zip(self.df_libros['b'], self.df_libros['n']))
        self.versiculos = []
        self.textos_crudos = []
        self._construir()

    def _construir(self):
        for _, fila in self.df_versiculos.iterrows():
            versiculo = Versiculo(
                numero_libro=fila['b'],
                nombre_libro=self.nombres_libros.get(fila['b'], f"Libro {fila['b']}"),
                capitulo=fila['c'],
                numero_versiculo=fila['v'],
                texto=fila['t']
            )
            self.versiculos.append(versiculo)
            self.textos_crudos.append(fila['t'])

    def obtener_todos_versiculos(self):
        return self.versiculos

    def obtener_textos(self):
        return self.textos_crudos