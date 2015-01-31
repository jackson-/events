class ajax( object ):

    def process_request( self, request ):

        request.context_dict = {
        	'base_template': 'users/_base.html'
        }

        if request.is_ajax():
            request.context_dict[ 'base_template' ] = 'users/_ajax.html'

    # may be used, please leave for refernace.
    # def process_response(self, request, response):

    #     if getattr(request, 'locale', False):
    #         response.cookies['locale'] = request.locale
