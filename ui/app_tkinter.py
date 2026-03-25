import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("lista de tareas")
        self.servicio = TareaServicio()

        #campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        #evento teclado enter
        self.entry.bind("<Return>", self.agregar_tarea_evento)
        #evento de tareas
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)
        #evento doble clic
        self.lista.bind("<Double-1>", self.marcar_completado_evento)
        #botones
        btn_agregar = tk.Button(root, text = "agregar tarea", command=self.agregar_tarea)
        btn_agregar.pack(pady=5)
        btn_completar= tk.Button(root, text="marcar completada", command=self.marcar_completada)
        btn_completar.pack(pady=5)
        btn_eliminar = tk.Button(root, text="eliminar", command=self.eliminar_tarea)
        btn_eliminar.pack(pady=5)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completado:
                texto =  "[hecho]" + texto
            self.lista.insert(tk.END,f"{tarea.id}.{texto}")
    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "por favor escribe una tarea")
    def agregar_tarea_evento(self,event):
        self.agregar_tarea()
    def obtener_id_seleccionado(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return None
        item = self.lista.get(seleccion)
        return int(item.split(".")[0])
    def marcar_completado_evento(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.actualizar_lista()
    def marcar_completada_evento(self,event):
        self.marcar_completada()
    def marcar_completada (self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.actualizar_lista()
    def eliminar_tarea(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.eliminar_tarea(id_tarea)
            self.actualizar_lista()
