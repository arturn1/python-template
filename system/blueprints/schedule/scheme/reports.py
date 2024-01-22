from datetime import datetime
from flask import Blueprint

import schedule

import time
import os

from importlib import import_module
from ..utils.load_jobs_from_folder import load_jobs_from_folder


work_blueprint = Blueprint("reports", __name__)


def load_jobs_to_schedule():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    jobs_folder = os.path.abspath(
        os.path.join(current_directory, '..', 'jobs'))

    load_jobs_from_folder(jobs_folder)


load_jobs_to_schedule()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Inicializado em {current_time}")

while True:
    schedule.run_pending()
    time.sleep(1)
