import uvicorn
from fastapi import FastAPI
from sqlalchemy.event import api

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

#init_db()

# app.include_router(skills.router)
# app.include_router(projects.router)
# app.include_router(pages.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    # Здесь нужно указать модульь и объект приложения в формате "module:app"
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)



