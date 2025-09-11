from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if not name:
        return "Hello, world ahdhee is here!"
    return f"Hello, {name}!"
