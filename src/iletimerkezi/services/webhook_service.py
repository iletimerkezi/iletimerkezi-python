import json
from typing import Optional
from ..models.webhook_report import WebhookReport

class WebhookService:
    def handle(self, raw_body: Optional[str] = None) -> WebhookReport:
        """
        Process webhook data
        
        Args:
            raw_body: Optional raw POST data. If None, will read from request body.
        
        Raises:
            ValueError: If no POST data received or invalid JSON payload
        """
        if raw_body is None:
            # In Python, we'll let the web framework handle getting raw body
            raise ValueError("POST data must be provided")

        if not raw_body:
            raise ValueError("No POST data received")

        try:
            data = json.loads(raw_body)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON payload")

        return WebhookReport(data)