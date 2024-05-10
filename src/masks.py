# маскировки номеров карт и счетов


def mask_card_number(card_number: str) -> str:
    """
    Masks a credit card number, showing only the first 6 and the last 4 digits.

    Args:
    card_number (str): The credit card number to be masked.

    Returns:
    str: The masked credit card number in the format 'XXXX XX** **** XXXX'.
    """
    # номер карты состоит только из цифр и имеет правильную длину  (16 цифр)
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        raise ValueError(
            "Invalid card number. Card number must have exactly 16 digits."
        )


def mask_account_number(account_number: str) -> str:
    """
    Masks an account number, showing only the last 4 digits.

    Args:
    account_number (str): The account number to be masked.

    Returns:
    str: The masked account number in the format '**XXXX'.
    """
    # номер счета состоит только из цифр и имеет длину не менее 4 цифр
    if len(account_number) >= 4 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        raise ValueError(
            "Invalid account number. Account number must have at least 4 digits."
        )


print(mask_card_number("7000792289606361"))
print(mask_account_number("73654108430135874305"))
