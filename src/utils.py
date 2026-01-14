import os
import pandas as pd

def save_to_excel(data, filename):
    # 1. 파일 저장 경로 설정
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_path, "data", "processed")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)
    
    # 2. 데이터프레임 생성
    df = pd.DataFrame(data)

    if df.empty:
        print("[경고] 저장할 데이터가 없습니다.")
        return

    # 3. 날짜 기준 내림차순 정렬 (완전 보강)
    temp_date = df["날짜"].str.extract(r'(\d{4}년 \d{1,2}월 \d{1,2}일)', expand=False)
    
    # 형식을 datetime으로 변환
    df["sort_key"] = pd.to_datetime(temp_date, format='%Y년 %m월 %d일', errors='coerce')
    
    # 내림차순 정렬 (최신 날짜가 위로), 변환 안 된 날짜는 마지막으로
    df = df.sort_values(by="sort_key", ascending=False, na_position="last").drop(columns=["sort_key"])

    # 4. 단일 시트에 저장
    try:
        df.to_excel(filepath, index=False, sheet_name='TOP30_모음')
        print(f"✅ 총 {len(df)}행 데이터가 한 시트에 저장되었습니다: {filepath}")
    except Exception as e:
        print(f"❌ 엑셀 저장 실패: {e}")