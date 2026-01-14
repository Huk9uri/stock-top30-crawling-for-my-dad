import os
import pandas as pd
import re

def save_to_excel(data, filename):
    """
    수집된 데이터를 날짜별로 시트를 나누어 data/processed/ 폴더에 저장합니다.
    """
    output_dir = "data/processed"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filepath = os.path.join(output_dir, filename)
    
    # 리스트 데이터를 데이터프레임으로 변환
    df = pd.DataFrame(data)
    
    if df.empty:
        print("[Warning] 저장할 데이터가 없습니다.")
        return

    # 날짜별로 그룹화하여 시트 분리 저장
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        # '날짜' 컬럼을 기준으로 그룹핑
        groups = df.groupby('날짜')
        
        for date, group in groups:
            # 엑셀 시트 이름에 사용할 수 없는 문자 제거 및 길이 제한(31자)
            sheet_name = re.sub(r'[\/:*?"<>|]', '', str(date))[:31]
            # 인덱스를 제외하고 시트별로 저장
            group.to_excel(writer, sheet_name=sheet_name, index=False)
            
    print(f"\n[Success] 날짜별 시트 분리 저장 완료: {filepath}")