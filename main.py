from fastapi import FastAPI
from fastapi.logger import logger
import uvicorn
import os

app = FastAPI()
logger.setLevel('INFO')


@app.get('/', status_code=200)
def root_fn():
    logger.info('Root accessed!!')
    return 'This is the api root'


@app.get('/name', status_code=200)
def return_name():
    name = os.environ.get('NAME')
    logger.info('Accessing NAME env from the os')
    if name is not None:
        logger.info('Returning name to the router')
        return {'Name': name}
    else:
        logger.info('NAME ENV not found!!')
        return {'name not found'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True, debug=True)



