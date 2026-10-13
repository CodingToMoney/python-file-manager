# python-file-manager

A small Django app for uploading, listing, downloading and deleting files through a browser. I built it as a learning project to get comfortable with Django's request/response cycle, file handling and a PyInstaller build pipeline. It also doubles as a tiny personal cloud drive on my laptop.

## What it does

- Drag-and-drop or click-to-pick upload from the browser
- Server rejects duplicate file names
- Lists every uploaded file with a download link and a delete button
- Delete removes both the database record and the file on disk
- Ships with a PyInstaller spec so the whole thing can be wrapped into a standalone `.app` / `.exe`

## Stack

- Python 3
- Django
- SQLite (no setup, just `migrate`)
- PyInstaller for desktop packaging

## Project layout

```
file_manager/
├── app/
│   ├── migrations/
│   ├── templates/index.html   # drag-and-drop UI
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # UploadedFile
│   ├── tests.py
│   ├── urls.py
│   └── views.py               # upload / list / download / delete
├── file_manager_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── start.py                   # convenience launcher: runserver + open browser
├── start.spec                 # PyInstaller spec
├── manage.py
└── README.md
```

## Running it locally

```bash
python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Then open <http://127.0.0.1:8000/>.

If you'd rather skip the manual steps on macOS / Windows, just run `python start.py` — it boots the dev server and pops the page open in your default browser.

## Building a standalone executable

```bash
pip install pyinstaller
pyinstaller start.spec
```

The bundled binary lands in `dist/`.

## Things I'd do differently today

This is an early project, and it shows. A few honest notes:

- `start.py` shells out with `subprocess.Popen` and assumes port 8000 is free. Fine for a personal tool, not great as a reusable pattern.
- `settings.py` keeps `SECRET_KEY` and `DEBUG = True` inline. For a real deployment I'd move secrets to env vars and turn `DEBUG` off.
- CSRF is intentionally disabled in `MIDDLEWARE` to keep the drag-and-drop flow simple. That is fine for a local tool, not fine for anything exposed to the internet.
- The `UploadedFile` model only stores the file and its MIME type. There's no per-user separation, so anyone with the page can see and delete everything.

It's the kind of code I'd refactor before shipping — but it's a fair snapshot of where I was when I was learning Django forms and `FileField`.
