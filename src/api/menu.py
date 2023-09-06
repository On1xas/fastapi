from typing import Annotated
import json
from fastapi import APIRouter, Depends, Request, Path
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from src.api.dependencies import parsing_menu, update_menu_info
from src.services.parsing_menu_magicinfo import ParsingService


templates = Jinja2Templates(directory='src/static')

router = APIRouter(
    prefix="/menu",
    tags=["menu"]
)

@router.get("/{server}")
async def get_menu(request: Request, server: str = Path()):
    print(server)
    info = await parsing_menu(server=server).update_spl_info()
    print(info)
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            "data": [info]
            }
        )


@router.post("/upd/arena")
async def update_menu_arena():
    info = await parsing_menu(server="parsing").update_spl_info()
    await update_menu_info(server="parsing").update_menu(data=info)
    return "Updated Menu Arena"


@router.post("/del/arena")
async def update_menu_arena():
    await update_menu_info(server="parsing").delete_all()
    
    return "Delete Menu Arena"
