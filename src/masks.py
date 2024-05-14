# маскировки номеров карт и счетов


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, показывая только первые "
    "6 и последние 4 цифры. "

    Аргументы:
    card_number (str): Номер кредитной карты, который будет замаскирован.

    Возвращает:
    str: Замаскированный номер кредитной карты "
    "в формате 'XXXX XX** **** XXXX'.
    """
    # Проверяем, что номер карты состоит только из цифр и имеет допустимую длин
    if 13 <= len(card_number) <= 19 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        raise ValueError("Неверный номер карты. Номер карты должен содержать от 13 до 19 цифр.")


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
    account_number (str): Номер счета, который будет замаскирован.

    Возвращает:
    str: Замаскированный номер счета в формате '**XXXX'.
    """
    # номер счета состоит только из цифр и имеет длину не менее 4 цифр
    if len(account_number) >= 4 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        raise ValueError(
            "Неверный номер счета. Номер счета должен содержать минимум 4 цифры."
        )
