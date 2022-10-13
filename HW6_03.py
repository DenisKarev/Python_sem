# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
#    значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in        "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out        {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'],
#             'П': ['Петр', 'Петр']}


invoice_list = 'Иван', 'Мария', 'Петр', 'Илья', 'Марина', 'Петр', 'Алина', 'Бибочка', 'Алевтина', 'Борис', 'Павел'

# invoice_list = 'Иван, Мария, Петр, Илья, Марина, Петр, Алина, Бибочка, Алевтина, Борис, Павел' # input('Enter the names of eployes: ')
# invoice_list = 'Иван Мария Петр Илья Марина Петр' # input('Enter the names of eployes: ')
# for manual input      Иван, Мария, Петр, Илья, Марина, Петр, Алина, Бибочка, Алевтина, Борис, Павел
# print(type(invoice_list))

def split_to_dict_by_1st_letter(li: list):
    res = {}
    for i in li:
        if i[0] not in res:
            res[i[0]] = []
        res[i[0]].append(i)
    return res

# does not work
# out_dict = {i[0]: [] if i[0] not in out_dict else out_dict[i[0]].append(i) for i in invoice_list}

print(invoice_list)
out_dict = split_to_dict_by_1st_letter(list(invoice_list)) if not isinstance(invoice_list, str)\
      else split_to_dict_by_1st_letter(invoice_list.replace(',', '').split())
print(out_dict)
