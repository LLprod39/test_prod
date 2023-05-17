# utils/project_manager.py
import os
import venv

class ProjectManager:
    def create_project_folder(self, project_name):
        os.makedirs(f"projects/{project_name}", exist_ok=True)

    def create_venv(self, project_name):
        venv.create(f"venvs/{project_name}", with_pip=True)

    def run_project(self, project_name):
        os.chdir(f"projects/{project_name}")
        process = subprocess.Popen(f"../venvs/{project_name}/bin/python main.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        os.chdir("../..")
        if process.returncode != 0:
            return f"Error running script: {stderr.decode()}"
        else:
            return stdout.decode()