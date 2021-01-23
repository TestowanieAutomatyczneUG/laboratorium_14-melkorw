def check_isbn(value):
    splited_value = value.split("-")
    joined_value = "".join(splited_value)
    if len(joined_value) != 13:
        return 'Wrong length of values'
    suma = 0
    for i in range(0, len(joined_value)):
        if joined_value[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 'Provide only numbers please'
        if i % 2 == 0:
            suma += int(joined_value[i]) * 1
        else:
            suma += int(joined_value[i]) * 3
    modulo = suma % 10
    if modulo == 0:
        modulo = 10
    if 10 - modulo == 0:
        return True
    else:
        return False
