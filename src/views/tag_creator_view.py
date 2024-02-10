from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    ''' 
    Responsável pela interação com HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):

        # Lógica de regra de negócio
        print('Estou na minha view')
        print(http_request)
        # Retorno HTTP
        return HttpResponse(status_code=200, body={"hello": "world"})
