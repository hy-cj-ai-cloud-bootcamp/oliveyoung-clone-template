"""
Pydantic 스키마 정의
API 요청/응답 데이터 검증에 사용됩니다.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ===== 인증 스키마 =====

class UserRegister(BaseModel):
    """회원가입 요청"""
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    """로그인 요청"""
    email: str
    password: str


class Token(BaseModel):
    """토큰 응답"""
    access_token: str
    token_type: str = "bearer"
    username: str


# ===== 카테고리 스키마 =====

class CategoryResponse(BaseModel):
    """카테고리 응답"""
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


# ===== 상품 스키마 =====

class ProductResponse(BaseModel):
    """상품 응답"""
    id: int
    name: str
    brand: Optional[str] = None
    price: int
    description: Optional[str] = None
    image_url: Optional[str] = None
    category_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    """상품 목록 응답"""
    products: List[ProductResponse]
    total: int


# ===== 장바구니 스키마 =====

class CartItemAdd(BaseModel):
    """장바구니 추가 요청"""
    product_id: int
    quantity: int = 1


class CartItemUpdate(BaseModel):
    """장바구니 수량 변경 요청"""
    quantity: int


class CartItemResponse(BaseModel):
    """장바구니 아이템 응답"""
    id: int
    product_id: int
    quantity: int
    product: ProductResponse

    class Config:
        from_attributes = True


# ===== 주문 스키마 =====

class OrderItemResponse(BaseModel):
    """주문 아이템 응답"""
    id: int
    product_name: str
    quantity: int
    price: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    """주문 응답"""
    id: int
    total_amount: int
    status: str
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True


# ===== 챗봇 스키마 =====

class ChatRequest(BaseModel):
    """챗봇 요청"""
    message: str


class ChatResponse(BaseModel):
    """챗봇 응답"""
    reply: str
