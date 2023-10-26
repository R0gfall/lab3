# TODO Напишите функцию find_common_participants
def find_common_participants(string_1, string_2, separator=","):
    string_1 = string_1 + separator + string_2
    string_1 = string_1.split(separator)
    new_list = []
    # print(string_1)
    for i in range(len(string_1)):
        for j in range(i, len(string_1) - 1):
            if string_1[i] == string_1[j + 1]:
                new_list.append(string_1[i])
                # print(string_1[i])
    new_list.sort()
    # print(new_list)
    return new_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

# find_common_participants(participants_first_group, participants_second_group, "|")
print(find_common_participants(participants_first_group, participants_second_group, "|"))
