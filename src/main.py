from fastapi import FastAPI

import src.iris

app = FastAPI()
app.include_router(src.iris.router)