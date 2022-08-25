import imp
from fastapi import FastAPI, Request
import json
from fastapi import FastAPI, Form, Request, File, UploadFile, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from .settings import Settings
from pyngrok import ngrok, conf
import sys
import logging
# from fastapi.logger import logger
logger = logging.getLogger('uvicorn')
settings = Settings()
conf.get_default().auth_token = settings.ngrok_token
conf.get_default().region = settings.ngrok_region
app = FastAPI(title = settings.app_name)
templates = Jinja2Templates(directory="webapp/templates")
app.mount("/static", StaticFiles(directory="webapp/static"), name="static")
port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000
# loggers = [name for name in logging.root.manager.loggerDict]
# print(loggers)
# Open a ngrok tunnel to the dev server
public_url = ngrok.connect(port).public_url
settings.public_url = public_url
logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# Update any base URLs or webhooks to use the public ngrok URL
# settings.BASE_URL = public_url

@app.get('/')
async def index(request: Request, response: Response):
    return templates.TemplateResponse('index.html', {'request': request})


