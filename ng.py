from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_ngrok():
    try:
        subprocess.run(["ngrok", "http", "--domain=intent-sharply-kodiak.ngrok-free.app", "8000"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}
    return {"message": "Ngrok tunnel started successfully"}

@app.route("/start-ngrok", methods=["GET"])
def start_ngrok_tunnel():
    result = run_ngrok()
    return jsonify(result)

if __name__ == "__main__":
    app.run()  
