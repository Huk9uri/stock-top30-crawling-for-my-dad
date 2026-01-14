import os
import pandas as pd
import re

def save_to_excel(data, filename):
    # 현재 작업 디렉토리 기준 절대 경로 생성
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_path, "data", "processed")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)
    df = pd.DataFrame(data)

    print(f"\n[디버깅] 총 {len(df)}개의 행을 저장 시도 중...")

    if df.empty:
        print("[경고] 저장할 데이터가 전혀 없습니다. 파싱 단계를 점검하세요.")
        return

    try:
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            for date, group in df.groupby('날짜'):
                clean_date = re.sub(r'[\\/*?:\[\]]', '', str(date))[:31]
                group.to_excel(writer, sheet_name=clean_date, index=False)
        print(f"✅ 파일 저장 완료: {filepath}")
    except Exception as e:
        print(f"❌ 엑셀 저장 실패: {e}")