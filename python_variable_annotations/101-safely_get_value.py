#!/usr/bin/env python3
"""
This module provides a type-annotated function for safely retrieving
values from a dictionary with a default fallback.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """
    Safely retrieves a value from a dictionary. If the key is not found, returns the default value.

    Parameters:
    dct (Mapping[Any, T]): The dictionary to retrieve the value from.
    key (Any): The key whose value needs to be retrieved.
    default (Union[T, None]): The default value to return if the key is not found. Defaults to None.

    Returns:
    Union[T, Any]: The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
