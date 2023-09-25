from fastapi import FastAPI
from .routers import result_many_boolean, user, vote, option, result_select, result_one_boolean
app = FastAPI()

app.include_router(user.router)
app.include_router(vote.router)
app.include_router(option.router)
app.include_router(result_select.router)
app.include_router(result_many_boolean.router)
app.include_router(result_one_boolean.router)

@app.get("/")
async def root():
    return {"message": "Connect successfully"}
