from models.controller import controller
from models.LinkedList import LinkedList




def main():

    lista_paises = controller.criar_lista()

    while True:
        controlos = input().split(" ")


        if controlos[0] == "RPI": 
            
            if controller.registar_pais_inicio_lista(lista_paises):
                lista_paises.transverse_list()

        
        if controlos[0] == "RPF":
            pass

        if controlos[0] == "RPDE":
            pass

        if controlos[0] == "RPAE":
            pass

        if controlos[0] == "VNE":
            pass

        if controlos[0] == "VP":
            pass

        if controlos[0] == "EPE":
            pass

        if controlos[0] == "EUE":
            pass
                