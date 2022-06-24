import tkinter as tk
from tkinter import ttk
from turtle import window_height
from PIL import Image, ImageTk
from tkinter import messagebox as mb

class Menu:
    def __init__(self, frame_1, frame_2, frame_3, frame_4, frame_5):
        self.menu_frame = frame_1
        self.student_frame = frame_2
        self.list_frame = frame_3
        self.grades_frame = frame_4
        self.subject_frame = frame_5
        
        self.students = []
        
        # Botón 1
        self.image_student = Image.open(r'icons\add.ico')
        self.image_student = self.image_student.resize((30,30), Image.ANTIALIAS)
        self.logo_student = ImageTk.PhotoImage(self.image_student)

        self.new_student_btn = tk.Button(
            self.menu_frame, 
            image = self.logo_student,
            text = "Registro",
            compound = "left",
            command = self.add_new_student_frame, 
            bg='#53736A',
            font=("Helvetica", 10, "bold"),
            fg="#F2E3D5"
        )

        # Botón 2
        self.image_grades = Image.open(r'icons\grades.ico')
        self.image_grades = self.image_grades.resize((30,30), Image.ANTIALIAS)
        self.logo_grades = ImageTk.PhotoImage(self.image_grades)

        self.subjects_btn = tk.Button(
            self.menu_frame,
            image = self.logo_grades, 
            text = "Notas",
            compound = "left", 
            command = self.add_grades, 
            bg='#53736A',
            font=("Helvetica", 10, "bold"),
            fg="#F2E3D5"
        )

        # Botón 3
        self.image_list = Image.open(r'icons\list.ico')
        self.image_list = self.image_list.resize((30,30), Image.ANTIALIAS)
        self.logo_list = ImageTk.PhotoImage(self.image_list)

        self.list_btn = tk.Button(
            self.menu_frame,
            image = self.logo_list, 
            text = "Listado", 
            compound = "left",
            command = self.show_student_list, 
            bg='#53736A',
            font=("Helvetica", 10, "bold"),
            fg="#F2E3D5"
        )

        self.new_student_btn.grid(row=1,column=0, padx=(10,10), pady=(20,10), sticky="EW")
        self.subjects_btn.grid(row=2,column=0, padx=(10,10), pady=(10,10), sticky="EW")
        self.list_btn.grid(row=3,column=0, padx=(10,10), pady=(10,10), sticky="EW")
        
        self.grades_frame.pack_forget()
        self.list_frame.pack_forget()
        self.menu_frame.pack(fill="y", side="left")

    def add_new_student_frame(self):
        # Título
        self.title_label = tk.Label(self.student_frame,text="DATOS", font=("Verdana",16), bg='#379392')
        # Id
        self.id_label = tk.Label(self.student_frame,text="Cédula",bg='#379392')
        self.id_input = tk.Entry(self.student_frame, bg='#F2E3D5') 
        # Nombre
        self.name_label = tk.Label(self.student_frame,text="Nombre",bg='#379392')
        self.name_input = tk.Entry(self.student_frame, bg='#F2E3D5') 
        # Apellido
        self.last_name_label = tk.Label(self.student_frame,text="Apellido",bg='#379392')
        self.last_name_input = tk.Entry(self.student_frame, bg='#F2E3D5')
        # Botón
        self.add_btn = tk.Button(self.student_frame, text="Listo", 
                    command=self.add_new_student, 
                    bg='#53736A', 
                    font=("Helvetica", 10, "bold"),
                    fg="#F2E3D5"
        )
        # Título Materias
        self.tsub_label = tk.Label(self.student_frame,text="MATERIAS", font=("Verdana",16), bg= '#379392')
        # Checkbutton
        self.checkbtn_1 = tk.IntVar()
        self.checkbtn_2 = tk.IntVar()   
        self.checkbtn_3 = tk.IntVar()
        self.checkbtn_4 = tk.IntVar()
        self.checkbtn_5 = tk.IntVar()
        self.checkbtn_6 = tk.IntVar()  

        self.spanish_checkbtn = tk.Checkbutton(self.student_frame, text = "Español", 
                      variable = self.checkbtn_1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )
        
        self.math_checkbtn = tk.Checkbutton(self.student_frame, text = "Matemáticas", 
                      variable = self.checkbtn_2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )

        self.science_checkbtn = tk.Checkbutton(self.student_frame, text = "Ciencias", 
                      variable = self.checkbtn_3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )

        self.history_checkbtn = tk.Checkbutton(self.student_frame, text = "Historia", 
                      variable = self.checkbtn_4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )

        self.english_checkbtn = tk.Checkbutton(self.student_frame, text = "Inglés", 
                      variable = self.checkbtn_5,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )

        self.arts_checkbtn = tk.Checkbutton(self.student_frame, text = "Artes", 
                      variable = self.checkbtn_6,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      bg= '#379392'
        )
        
        # Visualización
        self.title_label.grid(row=0, columnspan=3, pady=(20,10))

        self.id_label.grid(row=1, column=1, padx=(80,0), pady=(10,10), sticky="w")
        self.id_input.grid(row=1,column=2, padx=(40,100), pady=(10,10))

        self.name_label.grid(row=2, column=1, padx=(80,0), pady=(10,10), sticky="w")
        self.name_input.grid(row=3,column=1, padx=(80,0))

        self.last_name_label.grid(row=2, column=2, padx=(40,100), pady=(10,10), sticky="w")
        self.last_name_input.grid(row=3,column=2, padx=(40,100))

        self.tsub_label.grid(row=4, columnspan=3, pady=(20,10))

        self.spanish_checkbtn.grid(row=5, column=1, padx=(80,0), sticky = "we")
        self.math_checkbtn.grid(row=6, column=1, padx=(80,0), sticky = "we")
        self.science_checkbtn.grid(row=7, column=1, padx=(80,0), sticky = "we")
        self.history_checkbtn.grid(row=5, column=2, padx=(40,100), sticky = "we")
        self.english_checkbtn.grid(row=6, column=2, padx=(40,100), sticky = "we")
        self.arts_checkbtn.grid(row=7, column=2, padx=(40,100), sticky = "we")

        self.add_btn.grid(row=8, column=2, padx=(40,100), pady=(10,10), ipadx=20, sticky="we")
        
        self.grades_frame.pack_forget()
        self.subject_frame.pack_forget()
        self.list_frame.pack_forget()
        self.student_frame.pack(fill="both", side="left", expand=True)

    def add_new_student(self):
        if self.checkbtn_1.get() or self.checkbtn_2.get() or self.checkbtn_3.get() or self.checkbtn_4.get() or self.checkbtn_5.get() or self.checkbtn_6.get():
            self.subjects = {}
            if self.checkbtn_1.get() == 1: self.subjects['español'] = None
            if self.checkbtn_2.get() == 1: self.subjects['matemáticas'] = None
            if self.checkbtn_3.get() == 1: self.subjects['ciencias'] = None
            if self.checkbtn_4.get() == 1: self.subjects['historia'] = None
            if self.checkbtn_5.get() == 1: self.subjects['inglés'] = None
            if self.checkbtn_6.get() == 1: self.subjects['artes'] = None
            if self.id_input.get() != "" and self.name_input.get() != "" and self.last_name_input.get() != "":
                self.students.append({'id': self.id_input.get(),
                                    'name': self.name_input.get(), 
                                    'lname': self.last_name_input.get(),
                                    'subject': self.subjects
                })
            else:
                mb.showwarning("Atención", "Se deben llenar todos los campos")
        else:
                mb.showwarning("Atención", "Se escoger al menos 1 materia")

    def show_student_list(self):
        # Encabezado de la tabla
        self.table_lable = tk.Label(self.list_frame, text= "Cédula", bd=2, relief=tk.SOLID)
        self.table_lable.grid(row=0, column=0, ipadx = 28)
        self.table_lable = tk.Label(self.list_frame, text= "Nombre", bd=2, relief=tk.SOLID)
        self.table_lable.grid(row=0, column=1, ipadx = 28)
        self.table_lable = tk.Label(self.list_frame, text= "Apellido", bd=2, relief=tk.SOLID)
        self.table_lable.grid(row=0, column=2, ipadx = 28)
        self.table_lable = tk.Label(self.list_frame, text= "Materias", bd=2, relief=tk.SOLID)
        self.table_lable.grid(row=0, column=3, ipadx = 49)
        #self.table_lable = tk.Label(self.list_frame, text= "Grado", bd=2, relief=tk.SOLID)
        #self.table_lable.grid(row=0, column=4, ipadx = 28)
        # Imprimir tabla
        i = 0
        j = 0
        for dict in self.students:      # Ciclo para acceder a los diccionarios de la lista
            j = 0
            for element in dict.values():        # Ciclo para acceder a los valores de dentro del diccionario en questión
                if j < 3:
                    self.table_lable = tk.Label(self.list_frame, text= element, bd=2, relief=tk.SOLID)
                else:
                    aux = ""
                    for k, v in element.items():
                        aux = aux + k+":"+str(v)+"\n"
                    self.table_lable = tk.Label(self.list_frame, text= aux, bd=2, relief=tk.SOLID)
                    print(element)    
                       
                self.table_lable.grid(row=i+1, column=j, sticky="NSEW")    
                j = j + 1
            i = i + 1
          
        self.student_frame.pack_forget() # ocultar frame
        self.grades_frame.pack_forget()
        self.subject_frame.pack_forget()
        self.list_frame.pack(fill="both", side="left", expand=True)
    
    def add_grades(self):       
        # Título
        self.title_label = tk.Label(self.grades_frame, text="ESTUDIANTE", font=("Verdana",16), bg='#379392')
        # Icono
        self.image_user = Image.open(r'icons\user.ico')
        self.image_user = self.image_user.resize((100,100))

        self.image = ImageTk.PhotoImage(self.image_user)
        self.image_label = tk.Label(self.grades_frame, image=self.image, bg='#379392')
        # Id
        self.search_id_label = tk.Label(self.grades_frame,text="Cédula",bg='#379392')
        self.search_id_input = tk.Entry(self.grades_frame, bg='#F2E3D5') 
        # Botón
        self.search_btn = tk.Button(self.grades_frame, text="Buscar", 
                    command=lambda: self.search_student(self.search_id_input.get()), 
                    bg='#53736A', 
                    font=("Helvetica", 10, "bold"),
                    fg="#F2E3D5"
        )
        # Visualización
        self.title_label.grid(row=0, column=0, padx=(40,20), pady=(20,10), sticky="we")

        self.image_label.grid(row=2, column=0, padx=(20,20), pady=(20,10), sticky="we")
        self.search_id_label.grid(row=4, column=0, padx=(20,20), pady=(40,0), sticky="w")
        self.search_id_input.grid(row=5,column=0, padx=(20,20), pady=(10,10), sticky="w")
        self.search_btn.grid(row=6, column=0, padx=(20,20), pady=(10,10))

        self.student_frame.pack_forget()
        self.list_frame.pack_forget()
        self.grades_frame.pack(fill="y", side="left")

    def show_final_grade(self, grade_1, grade_2, grade_3, id):
        self.grade_1 = grade_1
        self.grade_2 = grade_2
        self.grade_3 = grade_3
        promedio = 0
        self.combo_subject = self.combo.get()
        for dict in self.student:
            for k, v in dict.items():
                if (k == 'subject'):
                    for key in v.keys():
                        if self.combo_subject == key:
                            promedio = (float(grade_1) + float(grade_2) + float(grade_3))/3
                            promedio = round(promedio,1)
                            v[key] = promedio
                            if promedio >= 3:
                                mb.showinfo("Calificación","El estudiante aprobó la materia con una calificación de: " + str(promedio))
                            else:
                                mb.showinfo("Calificación","El estudiante reprobó la materia con una calificación de: "+ str(promedio))
        print(self.students)                   

    def search_student(self, id):
        # Título
        self.title_label = tk.Label(self.subject_frame, text="CALIFICACIONES", font=("Verdana",16), bg='#C2C0A6')
        self.student = list(filter(lambda item: item['id'] == id, self.students))
        self.complete_name_lable = tk.Label(self.grades_frame,text="Nombre: " + self.student[0]['name']+ " "+ self.student[0]['lname'],bg='#379392')
        self.subject_lable = tk.Label(self.subject_frame, text="Materias Cursadas", bg="#C2C0A6")
        self.combo = ttk.Combobox(self.subject_frame, state="readonly",
                        values=list(self.student[0]['subject'])
        )
        self.button = ttk.Button(self.subject_frame, text="Calcular Nota Final", 
                        command=lambda: self.show_final_grade(self.grade_1_input.get(),self.grade_3_input.get(), self.grade_3_input.get(), id)
        )
        self.grade_1_label = tk.Label(self.subject_frame, text="Parcial 1:", bg='#C2C0A6')
        self.grade_2_label = tk.Label(self.subject_frame, text="Parcial 2:", bg='#C2C0A6')
        self.grade_3_label = tk.Label(self.subject_frame, text="Parcial 3:", bg='#C2C0A6')
        self.grade_1_input = tk.Entry(self.subject_frame,bg='#F2E3D5')
        self.grade_2_input = tk.Entry(self.subject_frame,bg='#F2E3D5')
        self.grade_3_input = tk.Entry(self.subject_frame,bg='#F2E3D5')


        self.complete_name_lable.grid(row=3, column=0, padx=(40,0), pady=(0,0), sticky="w")
        self.title_label.grid(row=0, column=0, padx=(20,40), pady=(20,10), sticky="we")
        self.subject_lable.grid(row=1, column=0, padx=(20,20), pady=(10,0), sticky="w")
        self.combo.grid(row=2, column=0, padx=(20,0), pady=(10,10), ipadx=5, sticky="we")
        self.grade_1_label.grid(row=3, column=0, padx=(20,40), pady=(10,10), sticky="w")
        self.grade_1_input.grid(row=4, column=0, padx=(20,40), pady=(0,10), sticky="w")
        self.grade_2_label.grid(row=5, column=0, padx=(20,40), pady=(10,10), sticky="w")
        self.grade_2_input.grid(row=6, column=0, padx=(20,40), pady=(0,10), sticky="w")
        self.grade_3_label.grid(row=7, column=0, padx=(20,40), pady=(10,10), sticky="w")        
        self.grade_3_input.grid(row=8, column=0, padx=(20,40), pady=(0,10), sticky="w")
        self.button.grid(row=9,column=0, padx=(20,40), pady=(0,10), sticky="we")

        self.student_frame.pack_forget()
        self.list_frame.pack_forget()
        self.subject_frame.pack(fill="both", side="left", expand=True)
        
        #Cargar un combobox con las materias
        
