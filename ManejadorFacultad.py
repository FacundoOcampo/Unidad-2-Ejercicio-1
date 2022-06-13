from ClaseCarrera import Carrera
from ClaseFacultad import Facultad
import csv

class ManF:
    __ListF=[]
    def __init__(self):
        self.__ListF=[]
    def Carga(self):
        archivo = open('Facultades.csv',"r",encoding="utf-8")
        reader = csv.reader(archivo,delimiter=',')
        fila=next(reader)
        bandera = True
        while bandera:
            FilaC=next(reader)
            listaaux = []
            while bandera and fila[0]==FilaC[0]:
                Carre = Carrera(int(FilaC[0]),int(FilaC[1]),FilaC[2],FilaC[3],FilaC[4],FilaC[5])
                listaaux.append(Carre)
                try:
                    FilaC=next(reader)
                except StopIteration:
                    bandera=False
            Facu = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4],listaaux)
            fila=FilaC
            self.__ListF.append(Facu)
        archivo.close()

    def BuscarF(self,Num):
        Band=False
        for Facu in self.__ListF:
            if Facu.GetCod()==Num:
                Facu.Mostrar()
                Band=True
        if Band==False:
            print("No se encontro la facultad")
    def BuscarFNom(self,Nom):
        Band=False
        for i in range(len(self.__ListF)):
            for j in range(len(self.__ListF[i].GetList())):
                if Nom==self.__ListF[i].GetList()[j].GetNom():
                    print("{} {}".format(self.__ListF[i].GetList()[j].GetCod(),self.__ListF[i].GetInfo()))
                    Band=True
        if Band==False:
            print("No se encontro la carrera")
