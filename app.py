from flask import Flask, render_template
import datetime

app = Flask(__name__)


def time_until_olympics():
    olympics_start_time = datetime.datetime(2024, 7, 26, 0, 0, 0)  # Update with the actual start time
    current_time = datetime.datetime.utcnow()
    time_remaining = olympics_start_time - current_time
    return max(time_remaining, datetime.timedelta(0))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/timer')
def timer():
    remaining_time = time_until_olympics()
    return render_template('timer.html', remaining_time=remaining_time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
