from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    res = {}

    # Now add the HTTP status code to the response.
    if response is not None:
    	if response.status_code != 200:
    		response.data['error']  = dict((k) for k in response.data.items())
    		[response.data.pop(k) for k in response.data if k != 'error']

    return response