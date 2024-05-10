# Модуль widget с функцией для обработки входных данных и применения маскировки
from src.masks import mask_account_number
from src.masks import mask_card_number


# Модуль widget с функцией для обработки входных данных и применения маскировки

def universal_masking(input_data: str) -> str:
    """
    Маскирует номер кредитной карты или счета в зависимости от входных данных.

    Args:
    input_data (str): Строка, содержащая тип и номер, например, "Visa 1234567890123456".

    Returns:
    str: Исходная строка с маскированным номером.
    """
    # Разбиваем входные данные, чтобы определить тип и номер
    parts = input_data.split()
    account_type = parts[0]  # Тип, например "Visa", "MasterCard", "Счет" (для счетов)

    # Определяем, входные данные относятся к карте или счету, основываясь на наличии "Счет"
    if account_type == "Счет":
        account_number = parts[1]
        masked_number = mask_account_number(account_number)
        result = f"{account_type} {masked_number}"
    else:
        # Считаем, что остальные части - это номер карты, разделенный пробелами
        card_number = "".join(parts[1:])
        masked_number = mask_card_number(card_number)
        result = f"{parts[0]} {masked_number[:4]} {masked_number[5:7]}{masked_number[7:9]} {masked_number[10:14]} {masked_number[15:]}"

    return result


# Модуль widget с функцией для преобразования даты и времени в дату

def format_datetime_to_date(datetime_str: str) -> str:
    """
    Преобразует строку с датой и временем в формате ISO в строку даты в формате DD.MM.YYYY.

    Args:
    datetime_str (str): Строка даты и времени в формате ISO, например, "2018-07-11T02:26:18.671407".

    Returns:
    str: Строка даты в формате DD.MM.YYYY.
    """
    # Извлекаем часть с датой из строки даты и времени
    date_part = datetime_str.split("T")[0]
    # Разделяем дату на год, месяц и день
    year, month, day = date_part.split("-")
    # Форматируем дату в формат DD.MM.YYYY
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date

# Примеры функций оставлены в комментариях для проверки формата
# universal_masking("Visa Platinum 7000 7922 8960 6361")
# universal_masking("Счет 73654108430135874305")
# format_datetime_to_date("2018-07-11T02:26:18.671407")

