# stock-top30

크롤링 결과를 수집하고(KSS로) 문장 분리/정제까지 처리해 최종 `.xlsx`로 저장하는 프로젝트 스캐폴딩입니다.

## 디렉토리 구조

```text
stock-top30/
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── src/
│   ├── __init__.py
│   ├── crawler.py
│   ├── parser.py
│   └── utils.py
├── config/
│   └── settings.yaml
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

## 설치

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python main.py
```

