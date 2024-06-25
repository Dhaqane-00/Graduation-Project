import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve host and port from environment variables
host = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', 5000)

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from __init__ import create_app

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host=host, port=int(port), debug=True)