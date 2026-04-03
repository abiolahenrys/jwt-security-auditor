from fastapi import FastAPI

app = FastAPI(title="Vulnerable jwt api", description="for security testing purposes only")


@app.get("/")
def root():
    return {"message": "Welcome to the vulnerable jwt api. Try /login and /user/me later."}