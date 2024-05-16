from typing import List, Dict

def filter_by_state(records: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
    records (List[Dict]): Список словарей.
    state (str, optional): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
    List[Dict]: Новый список, содержащий только словари с указанным значением 'state'.
    """
    return [record for record in records if record.get('state') == state]

from typing import List, Dict

def sort_by_date(records: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    Args:
    records (List[Dict]): Список словарей.
    descending (bool, optional): Порядок сортировки. True для убывания, False для возрастания. По умолчанию True.

    Returns:
    List[Dict]: Новый список, отсортированный по ключу 'date'.
    """
    return sorted(records, key=lambda x: x['date'], reverse=descending)


records = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по состоянию EXECUTED
filtered_records = filter_by_state(records)
print(filtered_records)

# Фильтрация по состоянию CANCELED
filtered_records_canceled = filter_by_state(records, 'CANCELED')
print(filtered_records_canceled)

# Сортировка по дате по убыванию
sorted_records_desc = sort_by_date(records)
print(sorted_records_desc)

# Сортировка по дате по возрастанию
sorted_records_asc = sort_by_date(records, descending=False)
print(sorted_records_asc)

