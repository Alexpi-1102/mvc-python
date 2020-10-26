from model.Alumno import Alumno

class personaController:

    def __init__(self):
        pass


    #*************** CREAR REGISTROS ***********
    def crearRegistro(self,lista):
        self.enlace=Alumno(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setMatricula(lista[4],lista[5])
        self.enlace.insertarAlumno()

    #*************** lEER REGISTROS ************
    def listaRegistros(self):
        pass

    #************** ACTUALIZAR REGISTRO *********
    def actualizarRegistro(self):
        pass

    #************** eLIMINAR REGISTRO **********
    def eliminarRegistro(self):
        pass