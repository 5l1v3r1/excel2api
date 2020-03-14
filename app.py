# define core engine
from fastapi import FastAPI
from starlette import applications
from starlette.middleware.cors import CORSMiddleware

# import controller
from apps.routes import google_router, raw_url_router
from connection import Connection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# register routes
app.include_router(google_router)
app.include_router(raw_url_router)


@app.on_event("startup")
def startup():
    applications.conf = dict()
    # define connection
    conn = Connection()
    # get config
    applications.conf['config'] = conn.get_config


@app.on_event("shutdown")
def shutdown():
    print("[Execute value when shutdown]")

# Running application
# uvicorn app:app --reload --port 8000
