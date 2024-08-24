#!/usr/bin/env python3
'''
Module defines a coroutine called async_comprehension
that takes no arguments.
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Function for async comprehension
    '''
    return [i async for i in async_generator()]
