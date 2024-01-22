import os

import schedule

from importlib import import_module


def load_jobs_from_folder(folder_path):
    job_files = [os.path.join(folder_path, folder) for folder in os.listdir(folder_path)
                 if os.path.isfile(os.path.join(folder_path, folder))]

    for folder in job_files:
        load_job_from_file(folder)


def load_job_from_file(file_path):
    job_module = import_module(
        f"system.blueprints.schedule.jobs.{os.path.basename(file_path)[:-3]}", package=__name__)

    if hasattr(job_module, 'work') and callable(getattr(job_module, 'work')):
        job_instance = getattr(job_module, 'work')()

        if hasattr(job_instance, 'exec') and callable(getattr(job_instance, 'exec')):
            schedule.every().day.at(job_instance.time).do(job_instance.exec)
            # schedule.every(job_instance.time).minutes.do(job_instance.exec)
