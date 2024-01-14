import importlib
from typing import Annotated

from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    answers = {
        "part1": 0,
        "part2": 0,
    }
    return templates.TemplateResponse("index.html", {"request": request, **answers})


@app.post("/solve", response_class=HTMLResponse)
async def solve(
    request: Request,
    day: Annotated[int, Form()],
    user_input: Annotated[str, Form()],
):
    solution = importlib.import_module(f"solutions.y2023d{day}")
    part1_solver = solution.Part1Solution(user_input)
    part2_solver = solution.Part2Solution(user_input)
    answers = {
        "part1": part1_solver.solve(),
        "part2": part2_solver.solve(),
    }
    return templates.TemplateResponse(
        "partials/input_form.html",
        {"request": request, **answers},
    )
