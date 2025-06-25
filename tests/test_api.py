import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import os
from backend.app.main import app


@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)


class TestChatAPI:
    """Chat API 테스트"""
    
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key', 'TAVILY_API_KEY': 'test_key'})
    @patch('backend.app.agent.create_product_search_agent')
    def test_chat_endpoint_success(self, mock_create_agent, client):
        """채팅 엔드포인트 성공 케이스 테스트"""
        # Mock agent 설정
        mock_agent = MagicMock()
        mock_message = MagicMock()
        mock_message.content = "아이폰 15는 최신 스마트폰입니다."
        mock_agent.invoke.return_value = {"messages": [mock_message]}
        mock_create_agent.return_value = mock_agent
        
        response = client.post(
            "/chat", 
            json={"message": "아이폰 15 추천해줘"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "session_id" in data
        assert data["response"] == "아이폰 15는 최신 스마트폰입니다."
    
    def test_chat_endpoint_empty_message(self, client):
        """빈 메시지에 대한 에러 처리 테스트"""
        response = client.post(
            "/chat", 
            json={"message": ""}
        )
        
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
    
    def test_chat_endpoint_missing_message(self, client):
        """메시지 필드 누락에 대한 에러 처리 테스트"""
        response = client.post("/chat", json={})
        
        assert response.status_code == 422  # Validation error
    
    def test_health_check(self, client):
        """헬스 체크 엔드포인트 테스트"""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


if __name__ == "__main__":
    pytest.main([__file__]) 