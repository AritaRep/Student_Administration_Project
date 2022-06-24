import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox as mb

# AGREGAR WIDGETS A LA VENTANA DE LOGIN
class Login:
    def __init__(self, frame_1, frame_2, menu):
        self.image_frame = frame_1
        self.form_frame = frame_2
        
        # Usuario
        self.user_label = tk.Label(self.form_frame,text="Usuario",bg='#024554',fg = "#F2E3D5", font=("Helvetica", 10, "bold"))
        self.user_input = tk.Entry(self.form_frame, bg='#C2C0A6') 

        # Contraseña
        self.password_label = tk.Label(self.form_frame,text="Contraseña",bg='#024554', fg="#F2E3D5", font=("Helvetica", 10, "bold"))
        self.password_input = tk.Entry(self.form_frame, bg='#C2C0A6') 

         # Botón
        self.sign_up_btn = tk.Button(
            self.form_frame, 
            text = "Iniciar Sesión", 
            command = lambda: menu(self.user_input.get(),self.password_input.get()), 
            bg='#53736A',
            font=("Helvetica", 10, "bold"),
            fg= '#F2E3D5'
        )
        self.password_input['show']="*"

        # Icono
        self.image_user = Image.open(r'icons\login.ico')
        self.image_user = self.image_user.resize((100,100))

        self.image = ImageTk.PhotoImage(self.image_user)
        self.image_label = tk.Label(self.image_frame, image=self.image, bg='#379392')

        # Visualización/Posicionamiento
        self.image_label.pack(fill="x", pady=(10,0))

        self.user_label.grid(row=1, column=0, padx=(40,0), pady=(20,0))
        self.user_input.grid(row=1,column=1, padx=(10,15), pady=(20,0))

        self.password_label.grid(row=2,column=0, padx=(40,0), pady=(25,30))
        self.password_input.grid(row=2,column=1, padx=(10,15))
        
        self.sign_up_btn.grid(row=3, columnspan=2, padx=(40,15), pady=(0,40), sticky="we")
        
        self.image_frame.pack(fill="x")
        self.form_frame.pack(fill="both")