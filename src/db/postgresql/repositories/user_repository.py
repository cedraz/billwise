from sqlalchemy.orm import Session
from db.postgresql.models.user import User
from schemas.user import UserCreate


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self) -> list[User]:
        return self.session.query(User).all()

    def create(self, user_in: UserCreate) -> User:
        user_data = user_in.model_dump()
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
