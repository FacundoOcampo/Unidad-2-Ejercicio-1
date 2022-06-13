class Menu:
    __Switch=None
    def __init__(self):
        self.__Switch={
            1:self.Opcion1,
            2:self.Opcion2
        }
    def Opciones(self,Num,Man):
        Fun=self.__Switch.get(Num,lambda : print("Opcion incorrecta"))
        if Num==1 or Num==2:
            Fun(Man)
        else:
            Fun()
    def Opcion1(self,Man):
        Num=int(input("Ingrese el codigo de una facultad\n"))
        Man.BuscarF(Num)
    def Opcion2(self,Man):
        Nom=input("ingrese el nombre de una carrera\n")
        Man.BuscarFNom(Nom)
