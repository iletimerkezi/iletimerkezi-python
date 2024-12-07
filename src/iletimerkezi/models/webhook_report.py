from typing import Dict, Optional

class WebhookReport:
    MESSAGE_STATUS_MESSAGES = {
        110: 'WAITING',
        111: 'DELIVERED',
        112: 'UNDELIVERED'
    }

    def __init__(self, data: Dict):
        """
        Initialize WebhookReport with webhook data
        
        Args:
            data: Webhook payload data
        """
        self.data = data

    def get_order_id(self) -> int:
        """Get order ID from webhook data"""
        return self.data.get('report', {}).get('id')

    def get_packet_id(self) -> int:
        """Get packet ID from webhook data"""
        return self.data.get('report', {}).get('packet_id')

    def get_status(self) -> str:
        """Get message status from webhook data"""
        return self.MESSAGE_STATUS_MESSAGES.get(self.get_status_code(), 'UNKNOWN')

    def get_status_code(self) -> int:
        """Get message status from webhook data"""
        return self.data.get('report', {}).get('status')

    def get_to(self) -> str:
        """Get recipient number from webhook data"""
        return self.data.get('report', {}).get('to')

    def get_body(self) -> str:
        """Get message body from webhook data"""
        return self.data.get('report', {}).get('body')