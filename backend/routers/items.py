"""
상품/장바구니/주문 라우터
메인 비즈니스 로직 CRUD API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from schemas import (
    CategoryResponse, ProductResponse, ProductListResponse,
    CartItemAdd, CartItemUpdate, CartItemResponse,
    OrderResponse
)
from crud import (
    get_categories, get_products, get_product,
    get_cart_items, add_cart_item, update_cart_item, delete_cart_item,
    create_order, get_orders
)
from .auth import get_current_user

router = APIRouter()


# ===== 카테고리 API =====

@router.get("/categories", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    """카테고리 목록 조회"""
    return get_categories(db)


# ===== 상품 API =====

@router.get("/products")
def list_products(
    category_id: Optional[int] = None,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    """
    상품 목록 조회
    - category_id: 카테고리 필터링 (선택)
    - limit: 한 페이지에 보여줄 상품 수
    - offset: 시작 위치
    """
    products, total = get_products(db, category_id, limit, offset)
    return {"products": products, "total": total}


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_detail(product_id: int, db: Session = Depends(get_db)):
    """상품 상세 조회"""
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
    return product


# ===== 장바구니 API =====

@router.get("/cart")
def list_cart(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """장바구니 조회 (로그인 필요)"""
    items = get_cart_items(db, user_id)
    return [
        {
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "product": {
                "id": item.product.id,
                "name": item.product.name,
                "price": item.product.price,
                "image_url": item.product.image_url,
                "brand": item.product.brand
            }
        }
        for item in items
    ]


@router.post("/cart")
def add_to_cart(
    item: CartItemAdd,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """장바구니에 상품 추가 (로그인 필요)"""
    # 상품 존재 확인
    product = get_product(db, item.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
    
    cart_item = add_cart_item(db, user_id, item.product_id, item.quantity)
    return {"message": "장바구니에 추가되었습니다.", "id": cart_item.id}


@router.put("/cart/{item_id}")
def update_cart(
    item_id: int,
    item: CartItemUpdate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """장바구니 수량 변경 (로그인 필요)"""
    updated = update_cart_item(db, item_id, user_id, item.quantity)
    if not updated:
        raise HTTPException(status_code=404, detail="장바구니 아이템을 찾을 수 없습니다.")
    return {"message": "수량이 변경되었습니다."}


@router.delete("/cart/{item_id}")
def remove_from_cart(
    item_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """장바구니에서 삭제 (로그인 필요)"""
    success = delete_cart_item(db, item_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="장바구니 아이템을 찾을 수 없습니다.")
    return {"message": "삭제되었습니다."}


# ===== 주문 API =====

@router.post("/orders")
def place_order(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """주문 생성 - 장바구니 내용으로 주문 (로그인 필요)"""
    order = create_order(db, user_id)
    if not order:
        raise HTTPException(status_code=400, detail="장바구니가 비어있습니다.")
    return {"message": "주문이 완료되었습니다.", "order_id": order.id}


@router.get("/orders")
def list_orders(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """주문 내역 조회 (로그인 필요)"""
    orders = get_orders(db, user_id)
    return [
        {
            "id": order.id,
            "total_amount": order.total_amount,
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "items": [
                {
                    "id": item.id,
                    "product_name": item.product_name,
                    "quantity": item.quantity,
                    "price": item.price
                }
                for item in order.items
            ]
        }
        for order in orders
    ]
