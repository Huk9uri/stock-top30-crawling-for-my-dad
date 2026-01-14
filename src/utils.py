import os
import pandas as pd

def save_to_excel(data, filename):
    """수집된 데이터를 data/processed/ 폴더에 엑셀로 저장합니다."""
    output_dir = "data/processed"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filepath = os.path.join(output_dir, filename)
    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)
    print(f"\n[Success] 파일 저장 완료: {filepath}")