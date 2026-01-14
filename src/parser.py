import re

def parse_stock_text(raw_text):
    results = []
    
    # 날짜 추출 (기존 로직 유지)
    date_match = re.search(r'(\d{4}년 \d{1,2}월 \d{1,2}일)', raw_text)
    post_date = date_match.group(1) if date_match else "날짜 미상"

    # 엄격한 종목 시작 패턴 정의
    # (\d+)\. : 숫자와 마침표로 시작하고
    # \s{1} : 반드시 정확히 공백 '한 칸'이 있어야 하며
    # (?=[가-힣A-Z]) : 그 공백 바로 뒤에는 한글 또는 영문 대문자가 와야 함
    # (.*?)(?=\s*\d+\.\s{1}[가-힣A-Z]|$) : 다음 종목의 시작 패턴이 나오기 전까지를 사유로 캡처
    pattern = re.compile(
        r'(\d+)\.\s{1}(?=[가-힣A-Z])([^(:]+)\(([^)]+)\)\s*:\s*(.*?)(?=\s*\d+\.\s{1}[가-힣A-Z]|\s*\[|\s*출처|$)',
        re.DOTALL
    )

    # 3. 전체 텍스트에서 매칭 수행
    matches = pattern.finditer(raw_text)
    
    for match in matches:
        num = match.group(1)
        name = match.group(2).strip()
        change = match.group(3).strip()
        reason = match.group(4).strip()

        # 첫 종목명에 제목(TOP30)이 섞인 경우 정제
        if "TOP30" in name:
            name = name.split("TOP30")[-1].strip()

        # 노이즈 필터링 (글자 수가 너무 길거나 http가 포함된 경우)
        if "http" in name or len(name) > 20: 
            continue

        results.append({
            '날짜': post_date,
            '종목명': name,
            '상승폭': change,
            '사유': reason.replace('\n', ' ').strip()
        })
            
    return results