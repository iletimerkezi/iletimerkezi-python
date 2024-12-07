import math
from typing import Dict, List, Optional
from ..base_response import BaseResponse

class BlacklistResponse(BaseResponse):
    def __init__(self, response_body: Dict, http_status_code: int, page: int = 1) -> None:
        super().__init__(response_body, http_status_code)
        self._numbers: List[str] = []
        self.customize_data()
        self._current_page = page

    def customize_data(self) -> None:
        """Process and store blacklist data from response"""
        self._numbers = self.data.get('blacklist', {}).get('number', [])

    def count(self) -> int:
        """Get total count of blacklisted numbers"""
        return int(self.data.get('blacklist', {}).get('count', 0))

    def numbers(self) -> List[str]:
        """Get all blacklisted numbers"""
        return self._numbers

    def total_pages(self) -> int:
        """Get total number of pages"""
        return math.ceil(self.count() / 1000)

    def current_page(self) -> int:
        """Get current page number"""
        return self._current_page

    def has_more_pages(self) -> bool:
        """Check if there are more pages"""
        return self.current_page() < self.total_pages()