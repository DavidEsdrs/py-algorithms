lista_ordenada_5 = [1, 2, 3, 4, 5]
lista_ordenada_50 = list(range(1, 51))
lista_inversa_5 = [5, 4, 3, 2, 1]
lista_inversa_50 = list(reversed(range(1, 51)))
lista_iguais_5 = [1, 1, 1, 1, 1]
lista_iguais_50 = [1] * 50
lista_dupla_5 = [1, 2, 2, 3, 3]
lista_dupla_50 = [i // 2 for i in range(1, 101)]
lista_repetida_5 = [1, 2, 1, 2, 1]
lista_repetida_50 = [i % 5 for i in range(1, 51)]


def selection_sort(list_to_sort):
    copy_list = list_to_sort[:]
    for j in range(len(copy_list) - 1):
        min_index = j
        for i in range(j, len(copy_list)):
            if copy_list[i] < copy_list[min_index]:
                min_index = i
        if copy_list[j] > copy_list[min_index]:
            aux = copy_list[j]
            copy_list[j] = copy_list[min_index]
            copy_list[min_index] = aux
    return copy_list


if __name__ == '__main__':
    list = selection_sort(lista_ordenada_50)
    print(list)
