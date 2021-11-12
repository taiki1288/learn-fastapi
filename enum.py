from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    # strとEnumを継承したサブクラス
    # 第一引数strを継承することで値が文字列でなければいけないようになり正確にレンダリングできるようになる。
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    # 固定値のクラス属性を作り、その値が使用可能な値となる。

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # ModelNameクラスではstr型を定義しているので値は文字列にならないといけない。
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

    
