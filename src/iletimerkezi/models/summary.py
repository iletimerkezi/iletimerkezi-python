from typing import Dict, Optional

class Summary:
    ORDER_STATUS_MESSAGES = {
        113: 'SENDING',
        114: 'COMPLETED',
        115: 'CANCELED'
    }

    def __init__(self, data: Dict):
        """
        Initialize Summary with summary response data
        
        Args:
            data: Summary payload data
        """
        self.data = data

    def get_order_id(self) -> Optional[str]:
        """Get order ID from webhook data"""
        return self.data.get('id')

    def get_order_status_code(self) -> int:
        """Get order status code from webhook data"""
        return self.data.get('status')

    def get_order_status(self) -> str:
        """Get order status from webhook data"""
        return self.ORDER_STATUS_MESSAGES.get(self.get_order_status_code(), 'UNKNOWN')

    def get_total(self) -> int:
        """Get total message count from webhook data"""
        return self.data.get('total')

    def get_delivered(self) -> int:
        """Get delivered message count from webhook data"""
        return self.data.get('delivered')

    def get_undelivered(self) -> int:
        """Get undelivered message count from webhook data"""
        return self.data.get('undelivered')

    def get_waiting(self) -> int:
        """Get waiting message count from webhook data"""
        return self.data.get('waiting')

    def get_submit_at(self) -> str:
        """Get order submit date from webhook data"""
        return self.data.get('submitAt')

    def get_send_at(self) -> str:
        """Get order send date from webhook data"""
        return self.data.get('sendAt')

    def get_sender(self) -> str:
        """Get order sender from webhook data"""
        return self.data.get('sender')