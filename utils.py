from typing import Callable
from typing import TypeVar
import time
import json

import requests

T1 = TypeVar('T1')
def safely_do_request(f: Callable[..., T1], retries: int = 5):
    """
    Useful wrapper around a function that handles many types of randomly reoccurring exceptions

    Usage:

    intead of running `f(x1, x2, x4=y4)` do: `safely_do_request(lambda : f(x1, x2, x4=y4))`

    Catches specific hardcoded set of exceptions.
    """
    for i in range(retries):
        try:
            ret = f()
            break
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.RequestException,
            json.JSONDecodeError,
            requests.exceptions.JSONDecodeError,
            requests.exceptions.InvalidJSONError,
        ) as e:
            time.sleep(0.5 + (2**i)/4) # in seconds: 0.5, 1.0, 1.5, 2.5, 4.5, 8.5, 16.5, ...
            if i == retries - 1:
                raise e
            continue
    assert ret, "the exception raise after an unsuccessful last iteration in the except handler SHOULD ensure ret is set"
    return ret
