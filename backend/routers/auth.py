"""
인증 라우터 - 회원가입/로그인 (JWT)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError

from database import get_db
from schemas import UserRegister, UserLogin, Token
from crud import get_user_by_email, get_user_by_username, create_user, verify_password
from config import JWT_SECRET, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

# JWT 토큰 인증 스킴
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    """
    현재 로그인한 사용자의 ID를 반환하는 의존성 함수
    JWT 토큰을 검증하고 사용자 ID를 추출합니다.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
        return user_id
    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")


def create_access_token(data: dict) -> str:
    """JWT 액세스 토큰 생성"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


@router.post("/register", response_model=dict)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """
    회원가입 API
    - username, email, password를 받아 새 사용자를 생성합니다.
    - 이메일 또는 사용자명이 중복되면 400 에러를 반환합니다.
    """
    # 이메일 중복 확인
    if get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    
    # 사용자명 중복 확인
    if get_user_by_username(db, user_data.username):
        raise HTTPException(status_code=400, detail="이미 사용 중인 사용자명입니다.")
    
    # 사용자 생성
    user = create_user(db, user_data.username, user_data.email, user_data.password)
    return {"message": "회원가입 성공", "user_id": user.id}


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    로그인 API
    - 이메일과 비밀번호를 검증하고 JWT 토큰을 발급합니다.
    """
    # 사용자 조회
    user = get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    
    # 비밀번호 검증
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    
    # JWT 토큰 생성
    access_token = create_access_token({"sub": str(user.id), "email": user.email})
    
    return Token(access_token=access_token, username=user.username)
