import tkinter as tk
from catalogo_gui import CatalogoPeliculasApp

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CatalogoPeliculasApp(ventana)
    ventana.mainloop()
