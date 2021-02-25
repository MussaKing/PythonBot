def parser():
    # Файл для парсинга
    f = open('Answer&Question.txt', encoding='utf-8')

    string = f.read()
    # Разделение по переносу строки
    string = string.split('\n')
    # Удаление лишнего
    string = string[:-1]
    for i in range(len(string)):
        list(string[i])
        string[i] = string[i].split(';')
    return string


def serch(searchstr):
    for i in range(len(parser())):
        # print(i)
        # print(parser()[i][0] == searchstr)
        if parser()[i][0] == searchstr:
            if parser()[i][1] == "'имя бота'":
                res = 'name'
                break
            else:
                res = parser()[i][1]
                break
        else:
            res = 'Пока такого не знаю'
    return res

# Для теста модуля локально
# searchstr = 'Hi'
# print(parser()[0][0] == searchstr)
# print(serch(searchstr))