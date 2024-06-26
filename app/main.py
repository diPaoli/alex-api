from fastapi import FastAPI, APIRouter
import uvicorn


app = FastAPI()
router = APIRouter(prefix='/rota_teste')


@router.get('')
def rota_teste():
    return {"message": "API do Alex alcançada com sucesso!!!"}


app.include_router(router)


print('')
print('')
print('')
print('')
print('')
print('TEste do Alex!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('')
print('')
print('')
print('')
print('')
print('')
print('')


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)