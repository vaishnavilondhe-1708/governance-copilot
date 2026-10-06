from fastapi import FastAPI

app = FastAPI(
    title="Governance Copilot",
    description="AI Governance & Risk Management Platform for Banking",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Governance Copilot"
    }