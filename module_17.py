sequence_of_numbers = [int(x) for x in input("Введите любое количество числел от 1 до 100 в любом порядке, через пробел: ").split()]
def merge_sort(sequence_of_numbers):
    # если массив меньше 2
    if len(sequence_of_numbers) < 2:
        # осуществляется выход из рекурсии
        return sequence_of_numbers[:]
    else:
        # поиск среднего значения
        middle = len(sequence_of_numbers) // 2
        left_part = merge_sort(sequence_of_numbers[:middle])
        right_part = merge_sort(sequence_of_numbers[middle:])
        return merge(left_part, right_part)


def merge(left_part, right_part):
    result = []
    i, j = 0, 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1

    while i < len(left_part):
        result.append(left_part[i])
        i += 1

    while j < len(right_part):
        result.append(right_part[j])
        j += 1
    return result

print(merge_sort(sequence_of_numbers))

# функция алгоритма двоичнго поиска
def binary_search_algorithm(sequence_of_numbers, part, left_part, right_part):
    # если левая граница больше правой
    if left_part > right_part:
        # значит элемент отсутствует
        return False
    # поиск среднего значения
    middle = (right_part + left_part) // 2
    # если элемент в середине
    if sequence_of_numbers[middle] == part:
        # возвращаем индекс
        return middle
    # если элемент меньше элемента в середине    
    elif part < sequence_of_numbers[middle]:
        # рекурсивно ищем в левой половине
        return binary_search_algorithm(sequence_of_numbers, part, left_part, middle - 1)
    else:  # иначе в правой
        return binary_search_algorithm(sequence_of_numbers, part, middle + 1, right_part)

while True:
    try:
        part = int(input("Введите любое одно число из списка, указанного выше: "))
        if part < 0 or part > 100:
            raise Exception
        break
    except ValueError:
        print("Неверно, здесь нужно ввести число. Вернитесь к заданию! ")
    except Exception:
        print("Неправильный диапазон!")

print(binary_search_algorithm(sequence_of_numbers, part, 0,  len(sequence_of_numbers)))