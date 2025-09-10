# FastAPI & Motor(MongoDB) Todo 예제

간단한 Todo 애플리케이션으로, FastAPI와 Motor(MongoDB)를 사용하여 구축되었습니다.

## 설치

1.  **저장소 복제:**

    ```bash
    git clone git@github.com:geoyeon/todo-fastapi.git
    cd todo-fastapi
    ```

2.  **가상 환경 생성 및 활성화:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    ```

3.  **의존성 설치:**

    ```bash
    pip install -r requirements.txt
    ```

## 사용법

애플리케이션을 실행하려면 다음 명령을 사용하세요.

```bash
uvicorn main:app --reload
```

이제 브라우저에서 `http://127.0.0.1:8000`으로 접속하여 API 문서를 확인하고 테스트할 수 있습니다.

## 의존성

이 프로젝트는 다음 라이브러리를 사용합니다.

- annotated-types==0.7.0
- anyio==4.10.0
- click==8.1.8
- exceptiongroup==1.3.0
- fastapi==0.116.1
- h11==0.16.0
- idna==3.10
- pydantic==2.11.7
- pydantic_core==2.33.2
- sniffio==1.3.1
- starlette==0.47.3
- typing-inspection==0.4.1
- typing_extensions==4.15.0
- uvicorn==0.35.0
- python-dotenv==1.0.0
- pydantic-settings==2.10.1
