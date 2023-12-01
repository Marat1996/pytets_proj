def get(array, index, default=None):
    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    length = len(coll)

    if length == 0:
        return []

    normalized_start = start if start is not None else 0
    normalized_end = end if end is not None and end <= length else length

    return coll[normalized_start:normalized_end]
