from uuid import uuid4

__all__ = ("get_uuid",)


def get_uuid() -> str:
    return str(uuid4())
