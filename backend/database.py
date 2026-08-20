"""
데이터베이스 연결 모듈
SQLAlchemy를 사용하여 PostgreSQL에 연결합니다.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 베이스 클래스
Base = declarative_base()


def get_db():
    """
    DB 세션을 생성하고 요청이 끝나면 닫는 의존성 함수
    FastAPI의 Depends()와 함께 사용합니다.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
