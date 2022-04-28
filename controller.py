from models.LinkedList import LinkedList


def criar_lista():
    lista = LinkedList()
    return lista


def registar_pais_inicio_lista(lista_paises, pais):

    lista_paises.insert_at_start(pais)
    return lista_paises



def registar_pais_fim_lista(lista_paises, pais):

    lista_paises.insert_at_end(pais)
    return lista_paises



def registar_pais_depois_elemento(lista_paises, pais):

    
    lista_paises.insert_after_item(pais)
    return lista_paises


def registar_pais_antes_elemento(lista_paises,pais):

    lista_paises.insert_before_item(pais)
    return lista_paises


def registar_pais_indice(lista_paises, pais):

    lista_paises.insert_at_index(pais)
    return lista_paises

def verificar_numero_elementos(lista_paises): 

    lista_paises.get_count
    return lista_paises

def verificar_pais(lista_paises, pais):

    lista_paises.search_item(pais)
    return lista_paises


def eliminar_primeiro_pais(lista_paises, pais):

    lista_paises.delete_at_start(pais)
    return pais


def eliminar_ultimo_pais(lista_paises, pais):

    lista_paises.delete_at_end(pais)
    return lista_paises


def eliminar_pais(lista_paises, pais):

    lista_paises.delete_element_by_value(pais)
    return lista_paises










