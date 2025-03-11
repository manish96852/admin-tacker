from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse  
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Create folders
os.makedirs("templates", exist_ok=True)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Admin credentials (hardcoded for simplicity)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Routes
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        # Successful login
        return RedirectResponse("/dashboard", status_code=303)
    else:
        # Failed login
        return templates.TemplateResponse(
            "login.html", 
            {"request": request, "error": "Invalid username or password"}
        )

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})