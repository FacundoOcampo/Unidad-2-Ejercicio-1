from ClassMenu import Menu
from ManejadorFacultad import ManF

if __name__=='__main__':
    NuevoM=ManF()
    NuevoM.Carga()
    NuevoMenu=Menu()
    Num=int(input("-----------Seleccione una opcion:-----------\n1_Mostrar nombre de la facultad, nombre  y duración de cada una de las carreras.\n2_Mostrar código, nombre y localidad de la facultad donde esta se dicta.\n"))
    while Num!=0:
        NuevoMenu.Opciones(Num,NuevoM)
        Num=int(input("-----------Seleccione una opcion:-----------\n1_Mostrar nombre de la facultad, nombre  y duración de cada una de las carreras.\n2_Mostrar código, nombre y localidad de la facultad donde esta se dicta.\n"))
