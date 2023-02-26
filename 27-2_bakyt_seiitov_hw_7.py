from random import randint

random_set = set(randint(0, 100) for i in range(10))
random_list = list(random_set)
print(f'Random list\n{random_list}')


def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                swapped = True
        if not swapped:
            break


bubble_sort(random_list)
print('\nSorted list')
print(random_list)


def binary_search(element, sorted_list):
    pos = -1
    elements_amount = len(sorted_list)
    result = False
    first_element = 0
    last_element = elements_amount - 1
    while (first_element <= last_element) and (pos == -1):
        middle = (first_element + last_element) // 2
        if element == sorted_list[middle]:
            first_element = middle
            last_element = first_element
            result = True
            pos = middle
        else:
            if element > sorted_list[middle]:
                first_element = middle + 1
            else:
                last_element = middle - 1
    if result:
        return f'Element {element} has been found at index {pos}'
    else:
        return f'Element {element} has not been found in the list'


number_input = int(input('\nEnter a number: '))
print(binary_search(number_input, random_list))
