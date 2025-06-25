# AI Chat Backend - vibe_coding_w2-2

AI 채팅 인터페이스를 위한 FastAPI 백엔드 프로젝트입니다.

## 🚀 프로젝트 개요

이 프로젝트는 AI 채팅 기능을 제공하는 백엔드 API 서버와 Streamlit 프론트엔드로 구성되어 있습니다.

### 🛠️ 기술 스택

- **백엔드**: FastAPI, Python 3.11+
- **프론트엔드**: Streamlit
- **테스트**: pytest
- **CI/CD**: GitHub Actions
- **코드 품질**: flake8, pytest-cov

## 📂 프로젝트 구조

```
vibe_coding_w2-2/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI 메인 애플리케이션
│   │   ├── config.py        # 설정 관리
│   │   ├── agent.py         # AI 에이전트 로직
│   │   ├── models/          # 데이터 모델
│   │   └── routers/         # API 라우터
│   ├── tests/               # 테스트 코드
│   └── requirements.txt     # Python 의존성
├── frontend/
│   ├── app.py              # Streamlit 앱
│   └── requirements.txt    # 프론트엔드 의존성
├── .github/
│   ├── workflows/          # GitHub Actions
│   ├── ISSUE_TEMPLATE/     # 이슈 템플릿
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/                   # 문서
```

## 🏃‍♂️ 시작하기

### 1. 저장소 클론

```bash
git clone https://github.com/yoonucho/vibe_coding_w2-2.git
cd vibe_coding_w2-2
```

### 2. 백엔드 실행

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

API 문서: http://localhost:8000/docs

### 3. 프론트엔드 실행

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

웹 앱: http://localhost:8501

## 🧪 테스트 실행

```bash
# 백엔드 테스트
cd backend
pytest tests/ -v

# 커버리지 포함 테스트
pytest tests/ --cov=app --cov-report=html
```

## 📋 새로운 기능 (PR 테스트용)

### 🆕 추가된 엔드포인트

- **GET `/api/v1/test`**: 테스트용 새 엔드포인트
- **개선된 루트 엔드포인트**: 더 자세한 API 정보 제공
- **향상된 헬스체크**: 서비스 정보 및 타임스탬프 포함

### 🔧 개선사항

1. **API 버저닝**: `/api/v1` 프리픽스 추가
2. **설정 관리**: config.py를 통한 중앙화된 설정
3. **문서화**: 상세한 docstring 및 API 문서
4. **이벤트 핸들러**: 시작/종료 이벤트 처리
5. **테스트 확장**: 새로운 기능에 대한 포괄적인 테스트

## 🤖 GitHub Actions

자동화된 워크플로우:

- ✅ **테스트 자동 실행** (push/PR 시)
- 🏷️ **자동 라벨링** (PR/이슈)
- 👥 **자동 할당** (리뷰어/담당자)
- 💬 **자동 댓글** (가이드라인 제공)
- 🔍 **자동 코드 리뷰** (품질 검사)

## 📝 개발 가이드

### 브랜치 전략

- `main`: 메인 브랜치
- `feature/*`: 새로운 기능 개발
- `bugfix/*`: 버그 수정
- `hotfix/*`: 긴급 수정

### 커밋 컨벤션

```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 업데이트
test: 테스트 추가/수정
refactor: 코드 리팩토링
```

### PR 생성 시 체크리스트

- [ ] 테스트 코드 작성 완료
- [ ] 모든 테스트 통과
- [ ] 코드 리뷰 가이드라인 준수
- [ ] 문서 업데이트 (필요한 경우)

## 🔗 링크

- [GitHub Repository](https://github.com/yoonucho/vibe_coding_w2-2)
- [API 문서](http://localhost:8000/docs)
- [이슈 트래커](https://github.com/yoonucho/vibe_coding_w2-2/issues)

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.

---

🤖 **자동화된 개발 환경**으로 효율적인 협업을 경험해보세요!
