from.Persona import persona
from.Conexion import conexion

class Alumno(persona):
    codigo=""
    ciclo=""

    def __init__(self,nombre,apellido,dni,sexo):
        persona.__init__(self,nombre,apellido,dni,sexo)

    def setMatricula(self,codigo,ciclo):
        self.codigo=codigo
        self.ciclo=ciclo

    def setCodigo(self,codigo):
        self.codigo=codigo

    def setCiclo(self,ciclo):
        self.ciclo=ciclo

    def getCodigo(self):
        return self.codigo

    def getCiclo(self):
        return self.ciclo

    def insertarAlumno(self):
        conecta=conexion()
        conecta.conectar()
        SQL="INSERT INTO alumno(codigo,nombres,apellidos,dni,sexo,ciclo) VALUES('"+self.codigo+"','"+self.nombre+"','"+self.apellido+"','"+self.dni+"','"+self.sexo+"',"+str(self.ciclo)+")"
        print(SQL)
        resp=conecta.setEjecutarQuery(SQL)
        if (resp):
            print("registro correcto")
        else:
            print("registro incorrecto")

    def mostrarAlumnos(self):
        pass

    def actualizarAlumno(self,codigo):
        pass

    def eliminarAlumno(self,codigo):
        pass

