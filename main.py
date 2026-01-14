from src.crawler import StockCrawler
from src.utils import save_to_excel
from src.parser import split_into_sentences
import time

def run_project(start_page, end_page):
    crawler = StockCrawler()
    all_sentences_data = []

    for page in range(start_page, end_page + 1):
        print(f"\n>>> 현재 {page} 페이지 크롤링 중...")
        post_ids = crawler.get_post_ids(page)
        
        for pid in post_ids:
            print(f"  - 게시글 {pid} 분석 중...", end='\r')
            raw_text = crawler.get_detail_content(pid)
            
            # 문장 분해 실행
            sentences = split_into_sentences(raw_text)
            
            for sent in sentences:
                all_sentences_data.append({
                    'Page_Num': page,
                    'Post_ID': pid,
                    'Sentence': sent
                })
            time.sleep(0.5) # 서버 부하 방지

    # 최종 저장
    if all_sentences_data:
        filename = f"stock_data_p{start_page}_to_p{end_page}.xlsx"
        save_to_excel(all_sentences_data, filename)
    else:
        print("수집된 데이터가 없습니다.")

if __name__ == "__main__":
    # 예: 0페이지부터 1페이지까지 총 20개 게시글 수집
    run_project(start_page=0, end_page=1)