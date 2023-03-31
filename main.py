import random

# List comprehension
any_numbers = random.sample(range(1, 1000), 50)
ordered_list_5 = [1, 2, 3, 4, 5]
ordered_list_50 = list(range(1, 51))
reversed_list_5 = [5, 4, 3, 2, 1]
reversed_list_50 = list(reversed(range(1, 51)))
repeated_items_5 = [1, 1, 1, 1, 1]
repeated_items_50 = [1] * 50
double_repeated_items_5 = [1, 2, 2, 3, 3]
double_repeated_items_50 = [i // 2 for i in range(1, 101)]
diff_repeated_5 = [1, 2, 1, 2, 1]
diff_repeated_50 = [i % 5 for i in range(1, 51)]
odd_numbers = lambda n: [x for x in n if x % 2 != 0]
square = lambda n: [x ** 2 for x in n]
half = lambda n: [x // 2 for x in n]

# Selection sort
# O(n^2)
def selection_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        min_value_idx = i
        for j in range(i + 1, len(list_to_sort)):
            if(list_to_sort[j] < list_to_sort[min_value_idx]):
                min_value_idx = j
        if i != min_value_idx:
            aux = list_to_sort[min_value_idx]
            list_to_sort[min_value_idx] = list_to_sort[i]
            list_to_sort[i] = aux

# Bubble sort
# O(n^2)
def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for j in range(n - 1):
        for i in range(n - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

if __name__ == '__main__':
    list = any_numbers
    print(f"random: {list}")
    bubble_sort(list)
    print(F"sorted: {list}")