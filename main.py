from src.crawler import StockCrawler
from src.utils import save_to_excel
from src.parser import parse_stock_text
import time

def run_project(start_page, end_page):
    crawler = StockCrawler()
    final_data = []

    for page in range(start_page, end_page + 1):
        print(f"\n>>> 현재 {page + 1} 페이지 리스트 수집 중...")
        post_ids = crawler.get_post_ids(page)
        
        for pid in post_ids:
            # 각 게시글 처리 로그를 줄 단위로 남겨, 기록이 사라지지 않도록 함
            print(f"  - 게시글 {pid} 텍스트 분해 중...")
            raw_text = crawler.get_detail_content(pid)
            
            # 정규식을 이용해 구조화된 데이터(날짜, 종목, 폭, 사유) 추출
            stock_items = parse_stock_text(raw_text)

            final_data.extend(stock_items)
            print(f"현재까지 {len(final_data)}개 수집됨")
            
            time.sleep(0.5)

    # 엑셀 저장
    if final_data:
        filename = f"stock_top30_cleaned.xlsx"
        save_to_excel(final_data, filename)
    else:
        print("수집된 데이터가 없습니다.")

if __name__ == "__main__": 
    run_project(start_page=0, end_page=1)

