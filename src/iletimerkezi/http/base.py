from abc import ABC, abstractmethod
from typing import Dict, Any

class HttpClient(ABC):
    @abstractmethod
    def post(self, url: str, options: Dict[str, Any]) -> 'HttpClient':
        pass

    @abstractmethod
    def get_body(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_status_code(self) -> int:
        pass

    @abstractmethod
    def get_payload(self) -> str:
        pass