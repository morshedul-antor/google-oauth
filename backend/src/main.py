from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.responses import JSONResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi import FastAPI
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="db4c78abc5fd022e53e7070a651a4f9e1de43ef374f012b773689886c05f1548"
)

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id="",
    client_secret="",
    client_kwargs={'scope': 'email openid profile'}
)


@app.get("/")
def root():
    return {"message": "Google OAuth"}


@app.get("/auth/login")
async def login(request: Request):
    url = str(request.url_for('auth'))
    return await oauth.google.authorize_redirect(request, url)


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return {"error": e.error}

    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
        return RedirectResponse(url="http://localhost:3000/welcome")

    return RedirectResponse(url="http://localhost:3000")


@app.get("/auth/user")
async def get_user(request: Request):
    user = request.session.get('user')
    if user:
        return {"user": user}
    return {"user": None}


@app.post('/auth/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return JSONResponse({'message': 'Logged out'})

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000,
        reload=True, log_level="info"
    )
