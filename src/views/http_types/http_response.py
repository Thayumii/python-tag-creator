from typing import Dict, Any

class HttpResponse:

    def __init__(self, status_code: int, body: Dict[str, Any]) -> None:
        self.status_code = status_code
        self.body = body
