# TODO Напишите функцию для поиска индекса товара

def search_in_list(item_list, item):
    for i, elem in enumerate(item_list):
        if elem == item:
            return i
    return None

    # Можно сделать и так, но функция будет два раза проходиться по массиву, если элемент существует
    # if item not in item_list:
    #     return None
    # return item_list.index(item)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_in_list(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
