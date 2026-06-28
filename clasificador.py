from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

class ClasificadorBiblico:
    def __init__(self, matriz, labels):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(matriz, labels, test_size=0.2)
        self.modelo = MultinomialNB()

    def entrenar(self):
        self.modelo.fit(self.X_train, self.y_train)

    def evaluar(self):
        predicciones = self.modelo.predict(self.X_test)
        print(f"Accuracy: {accuracy_score(self.y_test, predicciones):.4f}")
        return confusion_matrix(self.y_test, predicciones)