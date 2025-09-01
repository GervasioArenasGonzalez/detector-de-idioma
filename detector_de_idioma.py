from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import tkinter as tk

idiomas = {
    "af": "Afrikáans", "ar": "Árabe", "bg": "Búlgaro", "bn": "Bengalí", "ca": "Catalán",
    "cs": "Checo", "cy": "Galés", "da": "Danés", "de": "Alemán", "el": "Griego",
    "en": "Inglés", "es": "Español", "et": "Estonio", "fa": "Persa", "fi": "Finés",
    "fr": "Francés", "gu": "Guyaratí", "he": "Hebreo", "hi": "Hindi", "hr": "Croata",
    "hu": "Húngaro", "id": "Indonesio", "it": "Italiano", "ja": "Japonés", "kn": "Canarés",
    "ko": "Coreano", "lt": "Lituano", "lv": "Letón", "mk": "Macedonio", "ml": "Malabar",
    "mr": "Maratí", "ne": "Nepalí", "nl": "Neerlandés", "no": "Noruego", "pa": "Panyabí",
    "pl": "Polaco", "pt": "Portugués", "ro": "Rumano", "ru": "Ruso", "sk": "Eslovaco",
    "sl": "Esloveno", "so": "Somalí", "sq": "Albanés", "sv": "Sueco", "sw": "Suajili",
    "ta": "Tamil", "te": "Télugu", "th": "Tailandés", "tl": "Tagalo", "tr": "Turco",
    "uk": "Ucraniano", "ur": "Urdu", "vi": "Vietnamita", "zh-cn": "Chino simplificado",
    "zh-tw": "Chino tradicional"
}

# Función para calcular idioma
def detectar():
    texto = entrada.get()
    try:
        if not texto.strip():
            etiqueta.config(text="⚠️ Ingresa algún texto primero", fg="#ffcc00")
            return
        codigo = detect(texto)
        idioma = idiomas.get(codigo, "Desconocido")
        etiqueta.config(text=f"El idioma es: {idioma} ({codigo})", fg="white")
    except LangDetectException:
        etiqueta.config(text="❌ No se pudo detectar el idioma", fg="red")

# ------------------------------
# Ventana principal
# ------------------------------
root = tk.Tk()
root.geometry('500x300+700+300')
root.title('🌐 Detector de Idioma')
root.config(bg="#2c3e50")  # Fondo oscuro

# ------------------------------
# Widgets
# ------------------------------
titulo = tk.Label(root, text="🌍 Detector de Idiomas", font=("Arial", 18, "bold"),
                  bg="#2c3e50", fg="#ecf0f1")
subtitulo = tk.Label(root, text="Escribe un texto y detecta en qué idioma está.",
                     font=("Arial", 11), bg="#2c3e50", fg="#bdc3c7")

entrada = tk.Entry(root, width=40, font=("Arial", 12))
boton = tk.Button(root, text="Detectar idioma", command=detectar,
                  bg="#3498db", fg="white", font=("Arial", 12, "bold"),
                  activebackground="#2980b9", activeforeground="white",
                  relief="flat", padx=10, pady=5)

etiqueta = tk.Label(root, font=("Arial", 14, "bold"), bg="#2c3e50")

# ------------------------------
# Layout
# ------------------------------
titulo.pack(pady=10)
subtitulo.pack(pady=5)
entrada.pack(pady=15)
boton.pack(pady=10)
etiqueta.pack(pady=20)

# Ejecutar
root.mainloop()
