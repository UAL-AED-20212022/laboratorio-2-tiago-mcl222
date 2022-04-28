import controller





def main():

    lista_paises = controller.criar_lista()

    while True:
        print("Menu")
        controlos = input().split(" ")


        if controlos[0] == "RPI": 
            
            controller.registar_pais_inicio_lista(lista_paises, controlos[1])
            lista_paises.traverse_list()

        
        if controlos[0] == "RPF":
            
            controller.registar_pais_fim_lista(lista_paises, controlos[1])
            lista_paises.traverse_list()

        if controlos[0] == "RPDE":
            
            controller.registar_pais_depois_elemento(lista_paises, controlos[1], controlos[2])
            lista_paises.traverse_list()

        if controlos[0] == "RPAE":
            
            controller.registar_pais_antes_elemento(lista_paises, controlos[1], controlos[2])
            lista_paises.traverse_list()

        if controlos[0] == "RPII":

            controller.registar_pais_indice(lista_paises, controlos[1], int(controlos[2]))
            lista_paises.traverse_list()
            




        if controlos[0] == "VNE":
            
            controller.verificar_numero_elementos(lista_paises)
            lista_paises.traverse_list()
            print(f"O numero de elementos são {lista_paises.get_count()}.")

        if controlos[0] == "VP":
            controller.verificar_pais(lista_paises, controlos[1])
            lista_paises.traverse_list()
            
            

        if controlos[0] == "EPE":
            
            controller.eliminar_primeiro_pais(lista_paises)
            lista_paises.traverse_list()
            #print(f"O país {pais} foi eliminado da lista.)
            
            
            

        if controlos[0] == "EUE":
            
            controller.eliminar_ultimo_pais(lista_paises)
            lista_paises.traverse_list()
            print(f"O país {lista_paises.delete_at_start()} foi eliminado da lista")

        if controlos[0] == "EP":
            
            controller.eliminar_pais(lista_paises, controlos[1])
            print(f"O país {(controlos[1])} foi eliminado da lista.")
                