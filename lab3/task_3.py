# TODO  Напишите функцию count_letters

def count_letters(letter):
    new_dictionary = dict()
    for i in range(len(letter)):
        if letter[i].isalpha():
            a_lower_letter = letter[i].lower()
            if a_lower_letter not in new_dictionary:
                new_dictionary[a_lower_letter] = 1
            else:
                new_dictionary[a_lower_letter] += 1

    return new_dictionary

# TODO Напишите функцию calculate_frequency

def calculate_frequency(new_dictionary):
    cnt_letters = sum(new_dictionary.values())
    b = new_dictionary.items()
    last_dictionary = dict()
    for i in new_dictionary:
        last_dictionary[i] = new_dictionary[i] / cnt_letters

    return last_dictionary

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

# print(count_letters(main_str))
c = calculate_frequency(count_letters(main_str))
for i in c:
    print(i + ": " + "{:.2f}".format(c[i]))
