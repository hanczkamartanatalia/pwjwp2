from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'teachers.db'


# --- Inicjalizacja bazy danych ---
def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE Teacher (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                subject TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')
        # Dodaj kilku nauczycieli
        cursor.executemany('''
            INSERT INTO Teacher (name, subject, time)
            VALUES (?, ?, ?)
        ''', [
            ("Anna Kowalska", "Matematyka", "08:00"),
            ("Jan Nowak", "Fizyka", "09:00"),
            ("Maria Wiśniewska", "Chemia", "10:00")
        ])
        conn.commit()
        conn.close()


# --- Pobierz wszystkich nauczycieli ---
def get_teachers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Teacher")
    teachers = cursor.fetchall()
    conn.close()
    return teachers


# --- Dodaj nauczyciela ---
def add_teacher(name, subject, time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Teacher (name, subject, time) VALUES (?, ?, ?)", (name, subject, time))
    conn.commit()
    conn.close()


# --- Usuń nauczyciela ---
def delete_teacher(teacher_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Teacher WHERE id = ?", (teacher_id,))
    conn.commit()
    conn.close()


# --- Widok główny z formularzem ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'delete_id' in request.form:
            delete_teacher(request.form['delete_id'])
        else:
            name = request.form['name']
            subject = request.form['subject']
            time = request.form['time']
            add_teacher(name, subject, time)
        return redirect('/')

    teachers = get_teachers()
    return render_template_string('''
        <h1>Lista nauczycieli</h1>
        <ul>
            {% for id, name, subject, time in teachers %}
                <li>
                    {{ name }} — {{ subject }} o {{ time }}
                    <form method="post" style="display:inline">
                        <input type="hidden" name="delete_id" value="{{ id }}">
                        <button type="submit">Usuń</button>
                    </form>
                </li>
            {% endfor %}
        </ul>

        <h2>Dodaj nauczyciela</h2>
        <form method="post">
            Imię i nazwisko: <input type="text" name="name" required><br>
            Przedmiot: <input type="text" name="subject" required><br>
            Godzina: <input type="text" name="time" required><br>
            <button type="submit">Dodaj</button>
        </form>
    ''', teachers=teachers)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
