from flask import Flask
from flask_apscheduler import APScheduler
from http.server import BaseHTTPRequestHandler
from datetime import datetime

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())
scheduler = APScheduler()

request_handler_global = None  # Global variable to store the request handler

def run_drl_task_local():
    global request_handler_global
    if request_handler_global:
        request_handler_global.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
        current_time = datetime.now().time()
        request_handler_global.wfile.write(f'Current Time: {current_time}'.encode('utf-8'))
    else:
        print("No request handler available")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global request_handler_global
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('doGet:'.encode('utf-8'))
        request_handler_global = self  # Store the current request handler
        run_drl_task_local()
        return
    
def scheduled_task():
    run_drl_task_local()  # Use the stored request handler

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    scheduler.add_job(id='Scheduled Task', func=scheduled_task, trigger='interval', seconds=5)
    app.run(debug=True)
