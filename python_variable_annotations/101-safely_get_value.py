#!/usr/bin/env python3
"""
This module provides a type-annotated function for safely retrieving
values from a dictionary with a default fallback.
"""

from typing import Any, Mapping, TypeVar, Optional, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, 
    key: Any, 
    default: Optional[T] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary. If the key is not found,
    returns the default value.

    Parameters:
    dct (Mapping): The dictionary to retrieve the value from.
    key (Any): The key whose value needs to be retrieved.
    default (Optional[T]): The default value to return if the key is not
    found. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
