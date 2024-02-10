from typing import Dict

class HttpRequest:
    def __init__(self, header: Dict[str, str] = None, body: Dict[str, str] = None, 
                 query_params: Dict[str, str] = None) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
