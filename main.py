# main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from models.models import Plague
from typing import List, Optional
from contextlib import asynccontextmanager


plagues_db = {}
plagues_counter = 0



def init_plagues():
    global plagues_counter
    plagues = [
        Plague(
            name="Холера",
            type="бактерия",
            lethality=2,
            incubation_period=1,
            is_vaccine=True,
            image="holera.png",
            description="Бактерия холеры, распространяющаяся в странах Африки"
        ),
        Plague(
            name="Ветряная Оспа(ветрянка)",
            type="вирус",
            lethality=0,
            incubation_period=21,
            is_vaccine=True,
            image="vetryanka.png",
            description="Вирус ветряной оспы, распространённый по всему миру"
        ),
        Plague(
            name="БКЯ(Болезнь Крейтцфельдта — Якоба",
            type="прион",
            lethality=100,
            incubation_period=365,
            is_vaccine=False,
            image="bkya.png",
            description="Болезнь Крейтцфельдта - Якоба. Распространена в Северной и Южной Америке"
        )
    ]

    for plague in plagues:
        plagues_counter += 1
        plague.id = plagues_counter
        plagues_db[plagues_counter] = plague.model_dump()


# ✅ Правильный lifespan с подключением
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Запускаем приложение...")
    init_plagues()
    print(f"📚 Загружено болезней: {len(plagues_db)}")

    yield  # Приложение работает

    # Shutdown
    print("👋 Останавливаем приложение...")

# ✅ Передаём lifespan в приложение
app = FastAPI(title="Коллекция болезней", lifespan=lifespan)
# Подключаем папки с шаблонами и статическими файлами
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# 📄 Эндпоинт для отображения карточки
@app.get("/plague/{plague_id}", response_class=HTMLResponse)
async def get_monster_card(request: Request, plague_id: int):

  pass



@app.get("/plagues", response_class=HTMLResponse)
async def get_monsters_list(request: Request):
  pass

# API эндпоинты (JSON)
@app.get("/api/plagues", response_model=List[Plague])
async def get_monsters_api():
  pass


@app.get("/api/plagues/plague_id}", response_model=Plague)
async def get_monster_api(plague_id: int):
  pass