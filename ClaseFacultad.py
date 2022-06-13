class Facultad:
     __ListaCarreras = []
     def __init__(self,codigo=None,Nombre=None,Direccion=None,Localidad= None,telefono=None,listaAuxCarreras=None):
        self.__Codigo = codigo
        self.__Nombre = Nombre
        self.__Direccion = Direccion
        self.__Localidad = Localidad
        self.__telefono = telefono
        self.__ListaCarreras = []
        for i in range(len(listaAuxCarreras)):
            self.__ListaCarreras.append(listaAuxCarreras[i])
     def __str__(self):
         return "{} {} {} {} {}".format(self.__Codigo,self.__Nombre,self.__Direccion,self.__Localidad,self.__telefono)
     def GetCod(self):
         return self.__Codigo
     def Mostrar(self):
         print(self.__Nombre)
         print("Carreras:")
         for Carr in self.__ListaCarreras:
             Carr.Mostrar()
     def GetList(self):
         return self.__ListaCarreras
     def GetInfo(self):
         return "{} {}".format(self.__Nombre,self.__Localidad)
