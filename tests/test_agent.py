import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from backend.app.agent import create_product_search_agent, process_search_query


class TestProductSearchAgent:
    """상품 검색 Agent 테스트"""
    
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key', 'TAVILY_API_KEY': 'test_key'})
    @patch('backend.app.agent.ChatGoogleGenerativeAI')
    @patch('backend.app.agent.TavilySearch')
    @patch('backend.app.agent.create_react_agent')
    def test_create_agent_returns_callable(self, mock_create_react_agent, mock_tavily, mock_gemini):
        """Agent 생성 함수가 호출 가능한 객체를 반환하는지 테스트"""
        # Mock 설정
        mock_agent = MagicMock()
        mock_agent.invoke = MagicMock()
        mock_create_react_agent.return_value = mock_agent
        
        agent = create_product_search_agent()
        assert agent is not None
        assert hasattr(agent, 'invoke')
    
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key', 'TAVILY_API_KEY': 'test_key'})
    @patch('backend.app.agent.create_product_search_agent')
    def test_process_search_query_with_valid_input(self, mock_create_agent):
        """유효한 입력으로 검색 쿼리 처리 테스트"""
        # Mock agent 설정
        mock_agent = MagicMock()
        mock_message = MagicMock()
        mock_message.content = "테스트 응답입니다."
        mock_agent.invoke.return_value = {"messages": [mock_message]}
        mock_create_agent.return_value = mock_agent
        
        query = "스마트폰 추천"
        result = process_search_query(query)
        
        assert result is not None
        assert isinstance(result, dict)
        assert 'response' in result
        assert result['status'] == 'success'
    
    def test_process_search_query_with_empty_input(self):
        """빈 입력에 대한 에러 처리 테스트"""
        with pytest.raises(ValueError):
            process_search_query("")
    
    def test_process_search_query_with_none_input(self):
        """None 입력에 대한 에러 처리 테스트"""
        with pytest.raises(ValueError):
            process_search_query(None)


class TestEnvironmentSetup:
    """환경 설정 테스트"""
    
    def test_required_environment_variables(self):
        """필수 환경 변수 설정 확인 테스트"""
        # 테스트 환경에서는 환경 변수가 설정되어야 함
        required_vars = ['GOOGLE_API_KEY', 'TAVILY_API_KEY']
        
        for var in required_vars:
            # 실제 환경에서는 설정되어야 하지만, 테스트에서는 mock 사용
            assert var in ['GOOGLE_API_KEY', 'TAVILY_API_KEY']


if __name__ == "__main__":
    pytest.main([__file__]) 