# from flask import Flask
# from flask_apscheduler import APScheduler
# from drl_task import run_drl_task  # Ensure this function is defined in drl_task.py
from http.server import BaseHTTPRequestHandler
# from drl_task import Drl

def run_drl_task_local(request_handler):
    request_handler.wfile.write('run_drl_task_local'.encode('utf-8'))
    # Drl(request_handler, 'req handler')
    
class handler(BaseHTTPRequestHandler):
# When a GET request is received, this method is automatically called.
    def do_GET(self):
        # Sends a 200 OK response status code to indicate the request was successful.
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
        run_drl_task_local(self)
        return

