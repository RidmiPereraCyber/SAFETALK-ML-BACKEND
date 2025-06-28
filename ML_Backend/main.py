from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from prediction2 import predict_phishing

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Only allow requests from localhost:5001
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Request body structure
class Message(BaseModel):
    text: str

@app.post("/check-phishing")
async def check_phishing(message: Message):
    try:
        result = predict_phishing(message.text)
        print(result)
        print("test now test now test now")
        return {"status": "ok", "prediction": result}
    except Exception as e:
        print(e)
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
