from flask import Flask
import os

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "80")
app = Flask("demo")

@app.get("/")
def hello():
    return "Hello World !!!"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    
    
    
