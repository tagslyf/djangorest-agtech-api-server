from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    res = {}

    if response is not None:
        if response.status_code != 200:
            if 'detail' in response.data:
                response.data['error'] = response.data['detail']
                response.data.pop('detail')
            else:
                for k,v in response.data.items():
                    if isinstance(response.data[k], list):
                        res[k] = response.data[k]
                        response.data.pop(k)
                    else:
                        res.update(v)
                        response.data.pop(k)

                response.data['error'] = res

                #     if isinstance(response.data[k], dict):
                #         # response.data.update(v)
                #         res.update(v)
                #         response.data['error'] = res
                #         response.data.pop(k)
                #     else:
                #         response.data['error'] = 'trace'#response.data[k]
                #         # response.data[k] = response.data[k]


            # response.data['error']  = response.data['detail'] if 'detail' in response.data else dict((k) for k in response.data.items())
            # response.data.pop('detail') if 'detail' in response.data else [response.data.pop(k) for k in response.data if k != 'error']

    return response