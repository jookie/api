from flask import Flask, render_template_string
from flask_apscheduler import APScheduler
from datetime import datetime

app = Flask(__name__)

class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

current_time = ""

def drl_task():
    global current_time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@scheduler.task('cron', id='drl_task', day_of_week='mon-fri', second='*/5')
def scheduled_drl_task():
    drl_task()

@app.route('/')
def index():
    return render_template_string('''
        <html>
            <head>
                <title>Current Time Display</title>
                <script type="text/javascript">
                    function fetchTime() {
                        fetch('/time')
                            .then(response => response.text())
                            .then(data => {
                                document.getElementById('time').innerText = data;
                            });
                    }
                    setInterval(fetchTime, 5000);  // Fetch time every 5 seconds
                </script>
            </head>
            <body>
                <h1>Current Time:</h1>
                <p id="time"></p>
            </body>
        </html>
    ''')

@app.route('/time')
def get_time():
    return current_time

if __name__ == "__main__":
    app.run(debug=True)
