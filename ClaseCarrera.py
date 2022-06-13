class Carrera:
    def __init__(self,codigoFacultad,codigoCarrera,nombre,titulo,duracion,tipogrado):
        self.__Codigo_Facultad = codigoFacultad
        self.__Codigo_Carrera = codigoCarrera
        self.__Nombre = nombre
        self.__Titulo = titulo
        self.__Duracion = duracion
        self.__TipoGrado = tipogrado
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.__Codigo_Facultad,self.__Codigo_Carrera,self.__Nombre,self.__Titulo,self.__Duracion,self.__TipoGrado)
    def Mostrar(self):
        print("   {} Duracion: {}".format(self.__Nombre,self.__Duracion))
    def GetNom(self):
        return self.__Nombre
    def GetCod(self):
        return "{} {}".format(self.__Codigo_Facultad,self.__Codigo_Carrera)
