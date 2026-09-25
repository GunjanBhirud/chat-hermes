from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.conversations import router as conversations_router
from .api.messages import router as messages_router

app = FastAPI(title="Chat Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:5175", "http://127.0.0.1:5173", "http://127.0.0.1:5174", "http://127.0.0.1:5175"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversations_router)
app.include_router(messages_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
