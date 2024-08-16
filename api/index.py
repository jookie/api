# from flask import Flask
# from flask_apscheduler import APScheduler
# from drl_task import run_drl_task  # Ensure this function is defined in drl_task.py
from http.server import BaseHTTPRequestHandler
from drl_task import run_drl_task

def run_drl_task_local(request_handler):
    print("Running DRL task...")
    # Add your DRL script
    print("Running DRL task...")
    # Add your DRL script logic here
    # request_handler.wfile.write('drl_task()'.encode('utf-8'))
    
class handler(BaseHTTPRequestHandler):
# When a GET request is received, this method is automatically called.
    def do_GET(self):
        # Sends a 200 OK response status code to indicate the request was successful.
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
        print("Running DRL task...")
        # run_drl_task_local(self)
        # run_drl_task("n/Running DRL many task...")
        return

