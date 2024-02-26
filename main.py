import re

if __name__ == "__main__":
    from pprint import pprint
    # читаем адресную книгу в формате CSV в список contacts_list
    import csv

    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    contact_dict = {}
    for contact in contacts_list:
        if contact[0] != 'lastname':
            contact[5] = re.sub(r"(8|\+7)?\s?\(?(\d+)\)?-?\s?(\d{3})(-|\s?)(\d{2})(-|\s?)(\d{2})(\s)?\(?((доб.)?)(\s?)(\d*)(\)?)",
                             r"+7(\2)\3-\5-\7\8\10\12", contact[5])
            FIO = ' '.join(list([contact[0], contact[1], contact[2]])).strip().split()
            if len(FIO) > 0: contact[0] = FIO[0]
            if len(FIO) > 1: contact[1] = FIO[1]
            if len(FIO) > 2: contact[2] = FIO[2]

            key = ' '.join(list([FIO[0], FIO[1]]))

            if key not in contact_dict:
                contact_dict[key] = contact
            else:
                if contact_dict[key][2] == '': contact_dict[key][2] = contact[2]
                if contact_dict[key][3] == '': contact_dict[key][3] = contact[3]
                if contact_dict[key][4] == '': contact_dict[key][4] = contact[4]
                if contact_dict[key][5] == '': contact_dict[key][5] = contact[5]
                if contact_dict[key][6] == '': contact_dict[key][6] = contact[6]

    finish_contact_list = list(contact_dict.values())

    pprint(finish_contact_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')

        datawriter.writerows(finish_contact_list)