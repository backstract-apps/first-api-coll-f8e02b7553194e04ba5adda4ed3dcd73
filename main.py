from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - first-api-coll-f8e02b7553194e04ba5adda4ed3dcd73',debug=False,docs_url='/flamboyant-archimedes-c6c318cabed811ef8b0f0242ac12000548/docs',openapi_url='/flamboyant-archimedes-c6c318cabed811ef8b0f0242ac12000548/openapi.json')

app.include_router(router, prefix='/flamboyant-archimedes-c6c318cabed811ef8b0f0242ac12000548/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()