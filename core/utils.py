def expand_map(mapping):
    """Meta-function to allow multiple strings to be mapped to one value.

    The input `mapping` will be expanded like this:

    >>> expand_map({"a": "1", ("b", "c", "d"): "2"})
    {"a": "1", "b": "2", "c": "2", "d": "2"}

    (Note we use a tuple as the key because dictionary keys must be hashable).

    From: https://github.com/lenardos/talon_config-jcaw/blob/master/utils/__init__.py
    """
    result = {}
    for key, value in mapping.items():
        if isinstance(key, tuple):
            # Map each list element individually
            for element in key:
                result[element] = value
        else:
            result[key] = value
    return result
