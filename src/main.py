import tkinter as tk
from dotenv import load_dotenv
import os

# Cargamos las variables de entorno
load_dotenv()
PASSWORD_CORRECTO = os.getenv("USER_PASSWORD")

# 1. Función de validación (Solo actualiza la etiqueta en pantalla)
def capturar_valor():
    valor_usuario = campo_entrada_usuario.get()
    valor_password = campo_entrada_password.get()
    
    if valor_password == PASSWORD_CORRECTO:
        # Mensaje de éxito dentro de la app
        lbl_info.config(text=f"ACCESO CORRECTO: Bienvenido {valor_usuario}", fg="green")
    else:
        # Mensaje de error dentro de la app
        lbl_info.config(text="ACCESO INCORRECTO: Clave inválida", fg="red")

# 2. Configuración de la ventana
ventana = tk.Tk()
ventana.title(" MI primera app en thinter")
ventana.geometry("500x500")

# 3. Widgets
tk.Label(ventana, text="Usuario:", font=("Arial", 10, "bold")).pack(pady=5)
campo_entrada_usuario = tk.Entry(ventana)
campo_entrada_usuario.pack(pady=5)

tk.Label(ventana, text="Password:", font=("Arial", 10, "bold")).pack(pady=5)
campo_entrada_password = tk.Entry(ventana, show="*") 
campo_entrada_password.pack(pady=5)

# --- Esta es la etiqueta donde aparecerá el mensaje ---
lbl_info = tk.Label(ventana, text="", font=("Arial", 11))
lbl_info.pack(pady=20)

# Botón de acción
boton = tk.Button(ventana, text="Entrar", command=capturar_valor, width=15)
boton.pack(pady=10)

# 4. Loop
ventana.mainloop()
    


