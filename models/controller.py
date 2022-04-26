from models.LinkedList import LinkedList

class controller:
    def criar_lista():
        lista = LinkedList()
        return lista


    def registar_pais_inicio_lista(lista_paises, pais):

    
        lista_paises.insert_at_end(pais)
        return lista_paises





