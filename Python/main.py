from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="HTML")

app.mount("/static", StaticFiles(directory="CSS"), name="static")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request=request, name='Main_Page.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)