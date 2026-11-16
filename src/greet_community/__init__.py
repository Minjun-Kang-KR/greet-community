"""A friendly greeting package."""


def greet(name: str) -> str:
    """Return a greeting for name."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
