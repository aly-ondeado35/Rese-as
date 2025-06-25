class Pelicula:
    def __init__(self, titulo, resena):
        self.titulo = titulo
        self.resena = resena

    def __str__(self):
        return self.titulo
