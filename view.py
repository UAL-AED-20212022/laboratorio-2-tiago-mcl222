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
            
            controller.registar_pais_depois_elemento(lista_paises, controlos[2], controlos[1])
            lista_paises.traverse_list()

        if controlos[0] == "RPAE":
            
            controller.registar_pais_antes_elemento(lista_paises, controlos[2], controlos[1])
            lista_paises.traverse_list()

        if controlos[0] == "RPII":

            controller.registar_pais_indice(lista_paises, int(controlos[2]),controlos[1])
            lista_paises.traverse_list()
            




        if controlos[0] == "VNE":
            
            controller.verificar_numero_elementos(lista_paises)
            lista_paises.traverse_list()
            print(f"O número de elementos são {lista_paises.get_count()}.")

        if controlos[0] == "VP":

            pais = lista_paises.search_item

            controller.verificar_pais(lista_paises, controlos[1])
            lista_paises.traverse_list()

            if True:
                print(f"O país {controlos[1]} encontra-se na lista.")
            
            else:
                print(f"O país {controlos[1]} não se encontra na lista.")
            
            
            

        if controlos[0] == "EPE":

            primeiro_elemento = lista_paises.start_node.item
            
            controller.eliminar_primeiro_pais(lista_paises)
            lista_paises.traverse_list()
            print(f"O país {primeiro_elemento} foi eliminado da lista.")
            
            
            

        if controlos[0] == "EUE":

            ultimo_elemento = lista_paises.get_last_node()

            controller.eliminar_ultimo_pais(lista_paises)
            lista_paises.traverse_list()
            print(f"O país {ultimo_elemento} foi eliminado da lista")

        if controlos[0] == "EP":
            
            controller.eliminar_pais(lista_paises, controlos[1])
            print(f"O país {(controlos[1])} foi eliminado da lista.")
                