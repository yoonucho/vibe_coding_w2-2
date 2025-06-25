from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import chat
from .config import get_settings

# 설정 로드
settings = get_settings()

# FastAPI 앱 생성
app = FastAPI(
    title="AI Chat Backend",
    description="AI 채팅 인터페이스를 위한 FastAPI 백엔드",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    루트 엔드포인트 - API 상태 확인
    """
    return {
        "message": "AI Chat Backend API",
        "version": "1.0.0",
        "status": "healthy",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """
    헬스 체크 엔드포인트
    """
    return {
        "status": "healthy",
        "service": "ai-chat-backend",
        "timestamp": "2024-01-01T00:00:00Z"
    }

@app.get("/api/v1/test")
async def test_endpoint():
    """
    테스트용 새 엔드포인트 - PR 테스트를 위해 추가
    """
    return {
        "message": "PR 테스트용 엔드포인트",
        "feature": "새로운 기능 테스트",
        "status": "success"
    }

# 애플리케이션 시작 시 실행
@app.on_event("startup")
async def startup_event():
    """
    애플리케이션 시작 시 초기화 작업
    """
    print("🚀 AI Chat Backend 서버가 시작되었습니다!")
    print(f"📝 API 문서: http://localhost:8000/docs")

# 애플리케이션 종료 시 실행
@app.on_event("shutdown")
async def shutdown_event():
    """
    애플리케이션 종료 시 정리 작업
    """
    print("🛑 AI Chat Backend 서버가 종료됩니다.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 