from typing import Any as _Any, Literal as _Literal

def anything(fish: _Any) -> _Literal[True]:
    'the universal set. the set of all things. every thing is in it. returns True. useful when a function wants to receive/return any thing'
    return True

def nothing(fish: _Any) -> _Literal[False]:
    'the null set. the set of no things. not any thing is in it. returns False. useful when a function wants to receive/return no thing'
    return False
