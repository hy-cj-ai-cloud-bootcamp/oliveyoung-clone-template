"""
올리브영 클론 - FastAPI 메인 애플리케이션
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, items, chat

# FastAPI 앱 생성
app = FastAPI(
    title="올리브영 클론 API",
    description="CJ AI 클라우드 엔지니어 부트캠프 - 올리브영 클론 백엔드 API",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

# CORS 설정 (프론트엔드에서 API 호출 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth.router, prefix="/api/auth", tags=["인증"])
app.include_router(items.router, prefix="/api", tags=["상품/장바구니/주문"])
app.include_router(chat.router, prefix="/api", tags=["AI 챗봇"])


@app.get("/")
def root():
    """헬스 체크 엔드포인트"""
    return {
        "message": "올리브영 클론 API 서버가 실행 중입니다!",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """헬스 체크 (로드밸런서/모니터링용)"""
    return {"status": "healthy"}
