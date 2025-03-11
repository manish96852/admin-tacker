from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create templates directory if it doesn't exist
os.makedirs("templates", exist_ok=True)

# Templates setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "message": "Hello World"})