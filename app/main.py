from fastapi import FastAPI
from routers.apis import user 
app = FastAPI(
    title="USER APIS"
)
app.include_router(user)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)

