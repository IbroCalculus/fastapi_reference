from fastapi import FastAPI, Response, Request

app = FastAPI()


# Cookies are used to store information on the browser. Can accept different data types.


@app.get('/set_cookies')
async def set_cookies():
    response = Response(media_type='text/plain')
    response.set_cookie('cookie_name', 'cookie_value', expires=60)  # Cookie 1, expires in 60 seconds
    response.set_cookie('cookie_name2', 'cookie_value2', expires=120)  # Cookie 2, expires in 120 seconds
    response.body = b"Cookies are set"
    return response


@app.get('/retrieve_cookies')
async def retrieve_cookies(request: Request):
    cookie_name = request.cookies.get('cookie_name')
    cookie_name2 = request.cookies.get('cookie_name2')
    return {
        "cookie_name": cookie_name,
        "cookie_name2": cookie_name2
    }


@app.get('/clear_cookies')
async def clear_cookies():
    response = Response(media_type='text/plain')
    response.delete_cookie('cookie_name')
    response.delete_cookie('cookie_name2')
    response.body = b"Cookies are cleared"
    return response
