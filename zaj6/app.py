from flask import Flask, render_template, request

from zaj6.models.task import Task

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/tasks')
def tasks():
    return render_template('tasks.html', tasks=Task.tasksList)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/task-create')
def taskCreate():
    return render_template('task-create.html')


@app.route('/proces-task-create', methods=['POST'])
def proces_task_create():
    Task.appendTask(request.form.get('content'))
    return render_template('tasks.html', tasks=Task.tasksList)


@app.route('/proces-task-remove', methods=['GET'])
def proces_task_remove():
    Task.removeTask(request.args.get('content'))
    return render_template('tasks.html', tasks=Task.tasksList)


@app.route('/proces-task-done', methods=['GET'])
def proces_task_done():
    Task.setASDone(request.args.get('content'))
    return render_template('tasks.html', tasks=Task.tasksList)


if __name__ == '__main__':
    app.run(debug=True)
