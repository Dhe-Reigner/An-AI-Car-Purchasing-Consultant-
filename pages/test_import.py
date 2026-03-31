# pages/test_import.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from car.src.car.utils import run_ai

print(run_ai({"name": "Test"}))