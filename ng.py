from flask import Flask
import subprocess

app = Flask(__name__)

def run_ngrok():
    try:
        while True:
            subprocess.run(["ngrok", "http", "--domain=intent-sharply-kodiak.ngrok-free.app", "8000"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        # Handle the error, if needed
        pass

if __name__ == "__main__":
    # Start ngrok
    ngrok_process = subprocess.Popen(["ngrok", "http", "--domain=intent-sharply-kodiak.ngrok-free.app", "8000"])
    
    # Start Flask app
    app.run(port=8000, debug=True)
    
    try:
        while True:
            ngrok_process.wait(timeout=1)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, stopping ngrok...")
        ngrok_process.terminate()
