from __future__ import annotations

from typing import cast

import kss


def split_into_sentences(raw_text: str) -> list[str]:
    """텍스트를 받아 KSS로 문장 단위 분리 후 정제합니다.

    Args:
        raw_text: 게시글 본문 원문 문자열.

    Returns:
        5자 미만 문장을 제거하고 양끝 공백을 제거한 문장 리스트.
    """
    # 1. 한국어 문장 분리 (raw_text를 str로 고정해 반환 타입을 list[str]로 명확화)
    sentences = cast(list[str], kss.split_sentences(raw_text))

    # 2. 정제: 5자 미만 짧은 문장 제거 및 양끝 공백 제거
    refined = [s.strip() for s in sentences if len(s.strip()) >= 5]

    return refined