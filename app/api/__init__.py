import os
import sys
from dotenv import load_dotenv
load_dotenv(override=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
