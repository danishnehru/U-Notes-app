from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config.dib import conn
from schema.note import noteEntity, notesEntity

templates = Jinja2Templates(directory="templates")

note = APIRouter()

db = conn["mydatabase"]
collection = db["notes"]


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    docs = collection.find({})
    newDocs = notesEntity(docs)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "notes": newDocs
        }
    )


@note.post("/")
async def add_note(
    title: str = Form(...),
    desc: str = Form(...),
    important: bool = Form(False)
):

    new_note = {
        "title": title,
        "desc": desc,
        "important": important
    }

    collection.insert_one(new_note)

    return RedirectResponse(
        url="/",
        status_code=303
    )