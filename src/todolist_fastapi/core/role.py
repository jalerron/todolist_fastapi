import enum


class UserRole(str, enum.Enum):
    """Roles"""
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"