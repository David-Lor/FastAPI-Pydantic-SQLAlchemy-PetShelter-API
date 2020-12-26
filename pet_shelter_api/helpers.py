from uuid import uuid4

__all__ = ("get_uuid", "snakecase_to_camelcase")


def get_uuid() -> str:
    """Get an unique identifier as a UUID4"""
    return str(uuid4())


def snakecase_to_camelcase(s: str) -> str:
    """Convert a snake_case string to camelCase format"""
    return ''.join(
        word.capitalize() if i != 0 else word
        for i, word in enumerate(s.split('_'))
    )
