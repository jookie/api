import subprocess

def handler(request, response):
    subprocess.run(["python", "your_notebook_script.py"])
    return response.status(200).send("Notebook ran successfully.")
