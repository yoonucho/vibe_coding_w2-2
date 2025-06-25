"""
새로운 기능 테스트를 위한 테스트 코드
PR 테스트용으로 추가된 엔드포인트들을 테스트합니다.
🎉 ZeroDivisionError 버그 수정 반영
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_test_endpoint_default():
    """
    새로 수정된 /api/v1/test 엔드포인트 기본 테스트 (divisor=2)
    """
    response = client.get("/api/v1/test")
    assert response.status_code == 200
    
    data = response.json()
    assert data["message"] == "PR 테스트용 엔드포인트"
    assert data["feature"] == "새로운 기능 테스트"
    assert data["status"] == "success"
    assert data["calculation"] == 50.0  # 100 / 2 = 50
    assert "formula" in data
    assert "note" in data


def test_test_endpoint_with_custom_divisor():
    """
    커스텀 divisor 파라미터로 테스트
    """
    response = client.get("/api/v1/test?divisor=5")
    assert response.status_code == 200
    
    data = response.json()
    assert data["calculation"] == 20.0  # 100 / 5 = 20
    assert data["formula"] == "100 ÷ 5 = 20.0"


def test_test_endpoint_zero_divisor_error():
    """
    🐛 버그 수정 검증: 0으로 나누기 시 적절한 에러 응답
    """
    response = client.get("/api/v1/test?divisor=0")
    assert response.status_code == 400
    
    data = response.json()
    assert "나누는 수는 0이 될 수 없습니다" in data["detail"]


def test_test_endpoint_negative_divisor():
    """
    음수 divisor로 테스트
    """
    response = client.get("/api/v1/test?divisor=-4")
    assert response.status_code == 200
    
    data = response.json()
    assert data["calculation"] == -25.0  # 100 / -4 = -25


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


@pytest.mark.parametrize("endpoint,expected_status", [
    ("/", 200),
    ("/health", 200), 
    ("/api/v1/test", 200),
    ("/api/v1/test?divisor=10", 200)
])
def test_all_endpoints_return_success(endpoint, expected_status):
    """
    모든 엔드포인트가 성공 상태코드를 반환하는지 테스트
    """
    response = client.get(endpoint)
    assert response.status_code == expected_status


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


class TestBugFixValidation:
    """
    🐛 버그 수정 검증을 위한 테스트 클래스
    """
    
    def test_zero_division_bug_fixed(self):
        """
        ZeroDivisionError 버그가 수정되었는지 검증
        """
        # 이전에는 ZeroDivisionError가 발생했지만, 이제는 적절한 HTTP 400 에러 반환
        response = client.get("/api/v1/test?divisor=0")
        assert response.status_code == 400
        assert "나누는 수는 0이 될 수 없습니다" in response.json()["detail"]
    
    def test_error_handling_robustness(self):
        """
        에러 핸들링이 견고하게 구현되었는지 테스트
        """
        # 정상 케이스
        response = client.get("/api/v1/test?divisor=1")
        assert response.status_code == 200
        
        # 에러 케이스
        response = client.get("/api/v1/test?divisor=0")
        assert response.status_code == 400
        
        # 음수 케이스 (정상 처리되어야 함)
        response = client.get("/api/v1/test?divisor=-1")
        assert response.status_code == 200
    
    def test_response_format_consistency(self):
        """
        API 응답 형식의 일관성 테스트
        """
        response = client.get("/api/v1/test?divisor=4")
        data = response.json()
        
        # 필수 필드 확인
        required_fields = ["message", "feature", "status", "calculation", "formula", "note"]
        for field in required_fields:
            assert field in data
        
        # 계산 결과 정확성 확인
        assert data["calculation"] == 25.0  # 100 / 4 = 25


class TestAPIVersioning:
    """
    API 버저닝 테스트
    """
    
    def test_api_versioning_v1(self):
        """
        API v1 버저닝이 올바르게 적용되었는지 테스트
        """
        response = client.get("/api/v1/test")
        assert response.status_code == 200
        assert "v1" in "/api/v1/test"
    
    def test_response_includes_bug_fix_note(self):
        """
        응답에 버그 수정 안내가 포함되어 있는지 확인
        """
        response = client.get("/api/v1/test")
        data = response.json()
        assert "버그가 수정되었습니다" in data["note"]