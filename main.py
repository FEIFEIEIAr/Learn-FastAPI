from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse, Response

app = FastAPI()


@app.get("/")
async def root():
    html_content = """
    <html>
        <body><p style="color:red">Hello World</p></body>
    </html>"""
    return HTMLResponse(content=html_content, status_code=200)

# @app.get("/user/{user_id}")   # http://127.0.0.1:8000/user/7
@app.get("/user")  # http://127.0.0.1:8000/user?user_id=7
def users(user_id, token=Header(None)):
    return {"message": "Hello Users", "user_id": user_id, "token": token}

@app.route("/login", methods=["POST", "GET", "PUT"])
def login(username=Form(None), password=Form(None)):
    return {"data": {"username": username, "password": password}}


if __name__=='__main__':
    import uvicorn
    uvicorn.run(app="main:app", reload=True,)