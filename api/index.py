from flask import Flask
from flask_apscheduler import APScheduler
# from drl_task import run_drl_task  # Ensure this function is defined in drl_task.py
from http.server import BaseHTTPRequestHandler
from datetime import datetime
# from drl_task import Drl

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()


def run_drl_task_local(request_handler):
    # request_handler.wfile.write(''.encode('utf-8'))
    request_handler.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
    current_time = datetime.now().time()
    request_handler.wfile.write(f'Current Time: {current_time}'.encode('utf-8'))
    # Drl(request_handler, 'req handler')
    
class handler(BaseHTTPRequestHandler):
# When a GET request is received, this method is automatically called.
    def do_GET(self):
        # Sends a 200 OK response status code to indicate the request was successful.
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('doGet:'.encode('utf-8'))
        run_drl_task_local(self)
        return
def scheduled_task():
    run_drl_task_local()    
    
if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    # Schedule the task to run every 10 seconds
    scheduler.add_job(id='Scheduled Task', func=scheduled_task, trigger='interval', seconds=10)
    app.run(debug=True)    

