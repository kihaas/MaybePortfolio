import uvicorn
from fastapi import FastAPI



app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

#init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    # Здесь нужно указать модуль и объект приложения в формате "module:app"
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)