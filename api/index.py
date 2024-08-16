from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time</title>
        <script>
            function updateTime() {
                const now = new Date();
                document.getElementById('time').innerText = now.toLocaleTimeString();
            }
            setInterval(updateTime, 3000); // Update every 3 seconds
        </script>
    </head>
    <body>
        <h1>Current Time:</h1>
        <div id="time"></div>
        <script>updateTime();</script> <!-- Initial call to display time immediately -->
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
