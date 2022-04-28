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



def registar_pais_depois_elemento(lista_paises, pais_anterior, pais_novo):

    
    lista_paises.insert_after_item(pais_anterior, pais_novo)
    return lista_paises


def registar_pais_antes_elemento(lista_paises,pais_adiante, pais_novo):

    lista_paises.insert_before_item(pais_adiante, pais_novo)
    return lista_paises


def registar_pais_indice(lista_paises, pais, indice):

    lista_paises.insert_at_index(pais, indice)
    return lista_paises

def verificar_numero_elementos(lista_paises): 

    lista_paises.get_count
    return lista_paises

def verificar_pais(lista_paises, pais):

    if lista_paises.search_item(pais) ==  True:
        return True
    else:
        return False
    
    


def eliminar_primeiro_pais(lista_paises, pais):

    lista_paises.delete_at_start(pais)
    return pais


def eliminar_ultimo_pais(lista_paises, pais):

    lista_paises.delete_at_end(pais)
    return lista_paises


def eliminar_pais(lista_paises, pais):

    lista_paises.delete_element_by_value(pais)
    return lista_paises










