import uvicorn
from fastapi import FastAPI
from src.handlers import router

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application
    
app = get_application()


# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=80, log_level='info')
