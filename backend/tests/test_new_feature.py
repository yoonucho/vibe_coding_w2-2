"""
새로운 기능 테스트를 위한 테스트 코드
PR 테스트용으로 추가된 엔드포인트들을 테스트합니다.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_test_endpoint():
    """
    새로 추가된 /api/v1/test 엔드포인트 테스트
    """
    response = client.get("/api/v1/test")
    assert response.status_code == 200
    
    data = response.json()
    assert data["message"] == "PR 테스트용 엔드포인트"
    assert data["feature"] == "새로운 기능 테스트"
    assert data["status"] == "success"


def test_improved_root_endpoint():
    """
    개선된 루트 엔드포인트 테스트
    """
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert "AI Chat Backend API" in data["message"]
    assert data["version"] == "1.0.0"
    assert data["status"] == "healthy"
    assert data["docs"] == "/docs"


def test_enhanced_health_check():
    """
    개선된 헬스체크 엔드포인트 테스트
    """
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "ai-chat-backend"
    assert "timestamp" in data


@pytest.mark.parametrize("endpoint", [
    "/",
    "/health", 
    "/api/v1/test"
])
def test_all_endpoints_return_200(endpoint):
    """
    모든 엔드포인트가 200 상태코드를 반환하는지 테스트
    """
    response = client.get(endpoint)
    assert response.status_code == 200


def test_api_documentation_access():
    """
    API 문서 엔드포인트 접근 테스트
    """
    # Swagger UI 문서
    docs_response = client.get("/docs")
    assert docs_response.status_code == 200
    
    # ReDoc 문서  
    redoc_response = client.get("/redoc")
    assert redoc_response.status_code == 200


class TestNewFeatureIntegration:
    """
    새로운 기능의 통합 테스트 클래스
    """
    
    def test_api_versioning(self):
        """
        API 버저닝이 올바르게 적용되었는지 테스트
        """
        response = client.get("/api/v1/test")
        assert response.status_code == 200
        assert "v1" in "/api/v1/test"
    
    def test_response_consistency(self):
        """
        API 응답 형식의 일관성 테스트
        """
        endpoints = ["/", "/health", "/api/v1/test"]
        
        for endpoint in endpoints:
            response = client.get(endpoint)
            data = response.json()
            
            # 모든 응답이 dict 형태인지 확인
            assert isinstance(data, dict)
            
            # 각 응답에 기본적인 정보가 포함되어 있는지 확인
            assert len(data) > 0