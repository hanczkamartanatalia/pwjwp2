from flask import Flask, render_template, request, redirect, url_for
from zaj7.zad3.models.task import Task

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/tasks')
def tasks():
    all_tasks = Task.getAllTasks()
    print(all_tasks)
    return render_template('tasks.html', tasks=all_tasks)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/task-create')
def taskCreate():
    return render_template('task-create.html')


@app.route('/proces-task-create', methods=['POST'])
def proces_task_create():
    content = request.form.get('content')
    if content:
        Task.appendTask(content)
    return redirect(url_for('tasks'))


@app.route('/proces-task-remove', methods=['GET'])
def proces_task_remove():
    content = request.args.get('content')
    if content:
        Task.removeTask(content)
    return redirect(url_for('tasks'))


@app.route('/proces-task-done', methods=['GET'])
def proces_task_done():
    content = request.args.get('content')
    if content:
        Task.setASDone(content)
    return redirect(url_for('tasks'))


if __name__ == '__main__':
    app.run(debug=True)
