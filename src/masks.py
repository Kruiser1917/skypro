def format_datetime_to_date(datetime_str: str) -> str:
    """
    Преобразует строку с датой и временем в формате ISO в строку даты в формате DD.MM.YYYY.

    Args:
    datetime_str (str): Строка даты и времени в формате ISO, например, "2018-07-11T02:26:18.671407".

    Returns:
    str: Строка даты в формате DD.MM.YYYY.
    :param datetime_str:
    :return:
    """
    date_part = datetime_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


def universal_masking(input_data: str) -> str:
    """
    Маскирует номер кредитной карты или счета в зависимости от входных данных.

    Args:
        input_data (str): Входная строка с типом и номером (например, "Visa 1234567890123456").

    Returns:
        str: Исходная строка с маскированным номером.
    """
    parts = input_data.split()
    if parts[0] == "Счет":
        account_number = parts[-1]
        masked_number = mask_account_number(account_number)
        return f"{' '.join(parts[:-1])} {masked_number}"
    else:
        card_number = ''.join(parts[-4:])
        if len(card_number) == 16:
            masked_number = mask_card_number(card_number)
            return f"{' '.join(parts[:-4])} {masked_number[:4]} {masked_number[5:7]}{masked_number[7:9]} {masked_number[10:14]} {masked_number[15:]}"
        else:
            return f"{' '.join(parts[:-4])} Card number must be exactly 16 digits long"


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, показывая только первые 6 и последние 4 цифры.

    Args:
    card_number (str): Номер кредитной карты, который будет замаскирован.

    Returns:
    str: Замаскированный номер кредитной карты в формате 'XXXX XX** **** XXXX'.
    """
    if 13 <= len(card_number) <= 19 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        raise ValueError("Неверный номер карты. Номер карты должен содержать от 13 до 19 цифр.")


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Args:
    account_number (str): Номер счета, который будет замаскирован.

    Returns:
    str: Замаскированный номер счета в формате '**XXXX'.
    """
    if len(account_number) >= 4 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        raise ValueError("Неверный номер счета. Номер счета должен содержать минимум 4 цифры.")
