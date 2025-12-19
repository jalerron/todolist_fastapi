import uuid

from sqlalchemy import Boolean, DateTime, String, Enum, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from todolist_fastapi.core.role import UserRole
from .base import Base

class User(Base):
    
    id: Mapped[UUID] = mapped_column(as_uuid=True, primary_key=True, default=uuid.uuid4)
    
    # Базовые поля FastAPI Users
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # Дополнительные поля
    username = mapped_column(String(50), unique=True, index=True)
    first_name = mapped_column(String(100))
    last_name = mapped_column(String(100))
    
    # Роль пользователя
    role = mapped_column(Enum(UserRole), default=UserRole.USER)
    
    # Дополнительные данные
    bio = mapped_column(String(1000))
    
    # Таймстампы
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    last_login = mapped_column(DateTime(timezone=True))
    
    # Связи (опционально)
    # posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
    
    @property
    def full_name(self) -> str:
        """Полное имя пользователя"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username or self.email.split('@')[0]
    
    @property
    def is_admin(self) -> bool:
        """Проверка, является ли пользователь администратором"""
        return self.role == UserRole.ADMIN
    
    @property
    def is_moderator(self) -> bool:
        """Проверка, является ли пользователь модератором"""
        return self.role in [UserRole.ADMIN, UserRole.MODERATOR]