def list_to_number(lst):
    return int(''.join(map(str, lst)))

def solution(n):
    lista = []
    for digit in str(n):
        lista.append(digit)
    listsort = sorted(lista, reverse = True)
    return list_to_number(listsort)
