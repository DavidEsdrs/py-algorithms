# List comprehension
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
odd_numbers = lambda n: [x for x in n if x % 2 != 0]
square = lambda n: [x ** 2 for x in n]
half = lambda n: [x // 2 for x in n]

# List sort
def selection_sort(list_to_sort):
    copy_list = list_to_sort[:]
    for i in range(len(copy_list)):
        min_value_idx = i
        for j in range(i, len(copy_list)):
            if copy_list[j] < copy_list[min_value_idx]:
                min_value_idx = j
        if i != min_value_idx:
            aux = copy_list[i]
            copy_list[i] = copy_list[min_value_idx]
            copy_list[min_value_idx] = aux
    return copy_list


if __name__ == '__main__':
    list = selection_sort(lista_repetida_50)
    print(half(lista_ordenada_50))
