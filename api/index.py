from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime

app = Flask(__name__)

# Configuration for APScheduler
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())

# Initialize the scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Define a job to run every 5 seconds
@scheduler.task('interval', id='show_time', seconds=5, misfire_grace_time=900)
def show_time():
    print(f"Current time: {datetime.now()}")

if __name__ == '__main__':
    app.run(debug=True)
