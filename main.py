from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get('/', status_code=200)
def root_fn():
    return 'This is the api root'

@app.get('/name', status_code=200)
def return_name():
    name = os.environ.get('NAME')
    if name is not None:
        return {'Name': name}
    else:
        return {'name not found'}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True, debug=True)



