import uvicorn

if __name__ == "__main__":
    # web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
    uvicorn.run("server.app:app", host="0.0.0.0", port=5000, reload=True)
