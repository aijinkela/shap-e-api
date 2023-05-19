from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uuid
import os
import ai

app = FastAPI()
if not os.path.exists("output"):
    os.makedirs("output")
app.mount("/output", StaticFiles(directory="output"), name="output")
@app.get("/txt2blend")
async def txt2blend(prompt: str):
    task_id = str(uuid.uuid4())
    ply_file = "output/" + task_id + ".ply"
    # # 将输入文本写入文件
    # with open(ply_file, "w") as f:
    #     f.write(prompt)

    # with open("output.blend", "w") as f:
    #     f.write(output)

    ai.txt2ply(prompt, ply_file)
    # 构建JSON响应
    download_url = f"/{ply_file}"
    json_response = {"download_url": download_url}

    return JSONResponse(content=json_response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)