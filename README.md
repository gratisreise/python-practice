# Python Practice

파이썬 학습과 작은 실습 코드를 정리하기 위한 프로젝트입니다.

## 구조

```text
.
├── src/python_practice/   # 재사용 가능한 파이썬 코드
├── tests/                 # pytest 테스트 코드
├── examples/              # 실행해보는 예제 스크립트
├── docs/                  # 학습 노트와 문서
├── scripts/               # 보조 스크립트
└── pyproject.toml         # 프로젝트 설정
```

## 시작하기

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## 실행

```bash
python -m python_practice
python examples/hello.py
```

## 테스트

```bash
pytest
```
