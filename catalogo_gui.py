import tkinter as tk
from pelicula import Pelicula

class CatalogoPeliculasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Películas")

        self.peliculas = [
            Pelicula("Bichos", "Animación divertida y emotiva. Inspirada en 'Los siete samuráis'."),
            Pelicula("El Dorado", "Aventura animada con humor y música en una ciudad mítica."),
            Pelicula("Camino hacia el Terror", "Terror clásico en bosques con mutantes. Tensión pura."),
            Pelicula("Freddy vs Jason", "Choque de dos leyendas del terror. Más acción que miedo."),
            Pelicula("12 Horas para Sobrevivir", "Thriller con crítica social. Crímenes permitidos una noche.")
        ]

        self.lista = tk.Listbox(self.root, width=40)
        for peli in self.peliculas:
            self.lista.insert(tk.END, peli.titulo)
        self.lista.pack(pady=10)

        self.texto_resena = tk.Text(self.root, height=6, width=50, wrap=tk.WORD)
        self.texto_resena.pack(pady=10)

        self.lista.bind("<<ListboxSelect>>", self.mostrar_resena)

    def mostrar_resena(self, event):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            pelicula = self.peliculas[index]
            self.texto_resena.delete("1.0", tk.END)
            self.texto_resena.insert(tk.END, pelicula.resena)
