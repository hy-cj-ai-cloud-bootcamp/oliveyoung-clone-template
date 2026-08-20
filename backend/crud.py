"""
CRUD 함수 모듈
데이터베이스 CRUD(Create, Read, Update, Delete) 작업을 수행합니다.
"""
from sqlalchemy.orm import Session
import bcrypt
from models import User, Category, Product, CartItem, Order, OrderItem

# 비밀번호 해싱


# ===== 사용자 CRUD =====

def get_user_by_email(db: Session, email: str):
    """이메일로 사용자 조회"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    """사용자명으로 사용자 조회"""
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, username: str, email: str, password: str):
    """새 사용자 생성"""
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """비밀번호 검증"""
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


# ===== 카테고리 CRUD =====

def get_categories(db: Session):
    """전체 카테고리 조회"""
    return db.query(Category).all()


# ===== 상품 CRUD =====

def get_products(db: Session, category_id: int = None, limit: int = 50, offset: int = 0):
    """상품 목록 조회 (카테고리 필터링 가능)"""
    query = db.query(Product)
    if category_id:
        query = query.filter(Product.category_id == category_id)
    total = query.count()
    products = query.offset(offset).limit(limit).all()
    return products, total


def get_product(db: Session, product_id: int):
    """상품 상세 조회"""
    return db.query(Product).filter(Product.id == product_id).first()


def search_products(db: Session, keyword: str):
    """상품 검색 (이름 또는 설명에서 키워드 검색)"""
    return db.query(Product).filter(
        (Product.name.ilike(f"%{keyword}%")) |
        (Product.description.ilike(f"%{keyword}%"))
    ).all()


# ===== 장바구니 CRUD =====

def get_cart_items(db: Session, user_id: int):
    """사용자의 장바구니 조회"""
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()


def add_cart_item(db: Session, user_id: int, product_id: int, quantity: int = 1):
    """장바구니에 상품 추가 (이미 있으면 수량 증가)"""
    existing = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == product_id
    ).first()
    
    if existing:
        existing.quantity += quantity
        db.commit()
        db.refresh(existing)
        return existing
    
    item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_cart_item(db: Session, item_id: int, user_id: int, quantity: int):
    """장바구니 수량 변경"""
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == user_id
    ).first()
    if item:
        item.quantity = quantity
        db.commit()
        db.refresh(item)
    return item


def delete_cart_item(db: Session, item_id: int, user_id: int):
    """장바구니에서 삭제"""
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == user_id
    ).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False


def clear_cart(db: Session, user_id: int):
    """장바구니 전체 비우기"""
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()


# ===== 주문 CRUD =====

def create_order(db: Session, user_id: int):
    """장바구니 내용으로 주문 생성"""
    cart_items = get_cart_items(db, user_id)
    if not cart_items:
        return None

    # 총 금액 계산
    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    # 주문 생성
    order = Order(user_id=user_id, total_amount=total_amount)
    db.add(order)
    db.flush()

    # 주문 아이템 생성
    for cart_item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=cart_item.product_id,
            product_name=cart_item.product.name,
            quantity=cart_item.quantity,
            price=cart_item.product.price
        )
        db.add(order_item)

    # 장바구니 비우기
    clear_cart(db, user_id)
    
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session, user_id: int):
    """사용자의 주문 목록 조회"""
    return db.query(Order).filter(
        Order.user_id == user_id
    ).order_by(Order.created_at.desc()).all()


def get_all_products_for_chat(db: Session):
    """챗봇용 - 전체 상품 정보 조회"""
    return db.query(Product).all()
