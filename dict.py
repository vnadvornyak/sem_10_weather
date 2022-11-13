import openpyxl


def create_list():
    book = openpyxl.open('country_dict.xlsx')
    sheet = book.active
    country_list = []
    for i in range(1, sheet.max_row+1):
        country_list.append(sheet[i][0].value)
    return country_list


def create_dict():
    book = openpyxl.open('country_dict.xlsx')
    sheet = book.active
    country_dict = {}
    for row in range(1, sheet.max_row + 1):
        country_dict[f'{sheet[row][0].value}'] = f'{sheet[row][1].value}'
    return country_dict


def find_country_name(name: str, d: dict):
    eng_name = d[name]
    return eng_name
