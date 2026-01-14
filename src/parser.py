import re

def parse_stock_text(raw_text):
    """
    텍스트에서 날짜와 종목 정보를 구조적으로 추출합니다.
    결과: [{'date': '...', 'name': '...', 'change': '...', 'reason': '...'}, ...]
    """
    results = []
    
    # 1. 날짜 추출 (예: 2026년 1월 13일)
    date_match = re.search(r'(\d{4}년 \d{1,2}월 \d{1,2}일)', raw_text)
    post_date = date_match.group(1) if date_match else "날짜 미상"

    # 2. 종목 정보 추출을 위한 정규식
    # 패턴: 번호. 종목명(상승폭) : 사유
    # 그룹 설명: 1:종목명, 2:상승폭, 3:사유
    pattern = re.compile(r'\d+\.\s+([^(]+)\(([^)]+)\)\s*:\s*(.*)')

    lines = raw_text.split('\n')
    for line in lines:
        match = pattern.search(line)
        if match:
            stock_name = match.group(1).strip()
            change_rate = match.group(2).strip()
            reason = match.group(3).strip()
            
            results.append({
                '날짜': post_date,
                '종목명': stock_name,
                '상승폭': change_rate,
                '사유': reason
            })
            
    return results