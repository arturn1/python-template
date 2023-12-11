import os
from system.app import create_app

app = create_app()

PORT = os.environ["PORT"] or 5000

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
