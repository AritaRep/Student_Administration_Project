import tkinter as tk
from PIL import Image
from tkinter import messagebox as mb

from login import Login
from menu import Menu

class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.create_login_window()

    def exit(self):
        self.master.destroy()
        self.master.quit()

    def create_menu_window(self):
        self.master.withdraw() # Cerrar la ventana anterior
        self.menu_window = self.create_menu_window
        self.menu_window = tk.Toplevel()
        self.menu_window.title('Menú')
        self.menu_window.geometry("575x400+400+150")
        self.menu_window.rowconfigure(0, weight=1)
        self.menu_window.columnconfigure(1, weight=1)
        self.menu_window.protocol("WM_DELETE_WINDOW", self.exit) # Finalizar la ejecución al presionar la X
        self.menu_window.configure(bg='#379392')

        self.menu_frame = tk.Frame(self.menu_window, bg='#024554', relief=tk.RAISED, bd=2, width='250', height='400')
        self.student_frame = tk.Frame(self.menu_window, bg='#379392', width='430')
        self.list_frame = tk.Frame(self.menu_window, bg='#379392', width='430')
        self.grades_frame = tk.Frame(self.menu_window, bg='#379392', width='250')
        self.subject_frame = tk.Frame(self.menu_window, bg='#C2C0A6', width='180')
        self.menu_window = Menu(self.menu_frame, self.student_frame, self.list_frame, self.grades_frame, self.subject_frame)
    
    def create_login_window(self):
        # Frames
        self.image_frame = tk.Frame(self.master, bg='#379392', relief=tk.GROOVE, bd=3) # pack
        self.form_frame = tk.Frame(self.master,  bg='#024554', relief=tk.GROOVE, bd=3, height='300') # grid
        
        self.login_window = Login(self.image_frame, self.form_frame, self.sign_up)

        # Icono
        self.image_user = Image.open(r'icons\user.ico')
        self.master.iconbitmap(r'icons\user.ico')

        
    def sign_up(self, user, password):
        if user == "ADMIN" and password == "12345":
            self.create_menu_window()
        else:
           mb.showwarning("Atención", "Usuario o Contraseña no válidos")
    
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Login")
    window.geometry("300x300+500+150")
    window.configure(bg='#C2C0A6')

    main = Main(window)
    main.mainloop()