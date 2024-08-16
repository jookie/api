from flask import Flask
from flask_apscheduler import APScheduler
from http.server import BaseHTTPRequestHandler
from datetime import datetime
class Config:
    SCHEDULER_API_ENABLED = True
app = Flask(__name__)
app.config.from_object(Config())
scheduler = APScheduler()
REQUEST_HANDLER = None

def run_drl_task_local():
    REQUEST_HANDLER.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
    current_time = datetime.now().time()
    REQUEST_HANDLER.wfile.write(f'Current Time: {current_time}'.encode('utf-8'))
 
 
class handler(BaseHTTPRequestHandler):
# When a GET request is received, this method is automatically called.
    def do_GET(self):
        # Sends a 200 OK response status code to indicate the request was successful.
        REQUEST_HANDLER = self
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

