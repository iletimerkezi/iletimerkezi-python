from ..base_response import BaseResponse

class SmsResponse(BaseResponse):
    def customize_data(self) -> None:
        if 'order' in self.data and 'id' in self.data['order']:
            self.data['id'] = self.data['order']['id']
    
    def order_id(self) -> str:
        """Get the order ID from the response"""
        return self.data.get('id')