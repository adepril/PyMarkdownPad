"""
Visionneuse Markdown simple utilisant tkinter et tkhtmlview.

Fonctionnement :
1. Lancez l'application.
2. Utilisez le menu "Fichier" > "Ouvrir" pour sélectionner un fichier Markdown (.md).
3. Le contenu Markdown sera converti en HTML et affiché dans la fenêtre.

Pour afficher du texte :
- Créez un fichier .md avec du contenu Markdown.
- Ouvrez un fichier .md via l'application.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import markdown2
from tkhtmlview import HTMLLabel

class MarkdownViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Visionneuse Markdown")
        self.master.geometry("800x600")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.master.quit)

    def create_widgets(self):
        self.html_view = HTMLLabel(self.master, html="<h1>Bienvenue dans la visionneuse Markdown</h1>")
        self.html_view.pack(expand=True, fill="both", padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers Markdown", "*.md")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    md_content = file.read()
                    html_content = markdown2.markdown(md_content)
                    self.html_view.set_html(html_content)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier : {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownViewer(root)
    root.mainloop()