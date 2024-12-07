from typing import Dict, Any, Optional

class BaseResponse:
    def __init__(self, data: Dict[str, Any], status_code: int):
        self.data = data.get('response', {})
        self.status = data.get('response', {}).get('status', {})
        self.status_code = status_code
        self.customize_data()

    def customize_data(self) -> None:
        """Override this method to customize response data"""
        pass

    def ok(self) -> bool:
        """Check if the request was successful"""
        return self.status.get('code') == 200

    def get_error(self) -> Optional[str]:
        """Get error message if request failed"""
        if not self.ok():
            return self.status.get('message')
        return None

    def get_status_code(self) -> int:
        """Get HTTP status code"""
        return self.status_code