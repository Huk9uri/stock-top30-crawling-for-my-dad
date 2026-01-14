import requests
from bs4 import BeautifulSoup
import time
from src.parser import split_into_sentences

class StockCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.base_url = "https://stockinfo7.com"

    def get_post_ids(self, page):
        """목록 페이지에서 게시글 ID 리스트를 추출합니다."""
        list_url = f"{self.base_url}/stock/top30/list?page={page}&search="
        response = requests.get(list_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 상세 페이지 링크 추출 (/stock/top30/text/1593 등)
        links = soup.select('a[href*="/stock/top30/text/"]')
        post_ids = list(
            {
                str(link.get("href", "")).split("/")[-1]
                for link in links
                if link.get("href")
            }
        )
        return post_ids

    def get_detail_content(self, post_id):
        """상세 페이지에서 본문 텍스트를 추출합니다."""
        url = f"{self.base_url}/stock/top30/text/{post_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            return ""
            
        soup = BeautifulSoup(response.text, 'html.parser')
        # 사이트 구조에 맞춰 본문 영역 지정 (일반적으로 article 혹은 특정 class)
        content_area = soup.find("div", class_="content") or soup.body
        if content_area is None:
            return ""
        return content_area.get_text(separator=" ", strip=True)