from bottle import route, run, response, request, HTTPResponse

@route('/')
def main():
    value = request.get_cookie('account', secret='ThisIsSecretKey')
    if value:
        return value

@route('/set')
def set():
    resp = HTTPResponse(status=303)
    resp.set_header('Location','/')
    resp.set_cookie('account', 'admin', secret='ThisIsSecretKey')
    return resp

run(host='127.0.0.1', port=8000, debug=True, reloader=True)
