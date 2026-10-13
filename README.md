# Python File Manager

A small Django web application for uploading, listing, downloading and deleting files, packaged with PyInstaller for local desktop use.

## Features

- Upload a file via a simple HTML form
- Prevent duplicate file names
- List all uploaded files with their MIME types
- Download any uploaded file
- Delete a file (removes the disk file and the database record)
- Ready for packaging as a standalone executable via PyInstaller (`start.spec`)

## Tech Stack

- Python 3
- Django
- SQLite (default, no extra setup)
- PyInstaller (for distribution)

## Project Layout

```
file_manager/
├── app/
│   ├── migrations/
│   ├── templates/index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # UploadedFile model
│   ├── tests.py
│   ├── urls.py
│   └── views.py         # upload, list, download, delete
├── file_manager_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── build/               # PyInstaller output (gitignored)
├── dist/                # PyInstaller output (gitignored)
├── start.py             # Convenience launcher: runserver + open browser
├── start.spec           # PyInstaller spec
├── manage.py
└── README.md
```

## Local Development

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install Django
pip install django

# 3. Run migrations
python manage.py migrate

# 4. Start the dev server
python manage.py runserver 127.0.0.1:8000
```

Then open <http://127.0.0.1:8000/> in your browser.

## One-Click Launch (macOS / Windows)

`start.py` boots the dev server and opens the default browser at the same time:

```bash
python start.py
```

## Building a Standalone Executable

```bash
pip install pyinstaller
pyinstaller start.spec
```

The packaged binary lands in `dist/`.

## Notes

- Uploaded files are stored under `media/uploads/` (gitignored).
- The default SQLite database is `db.sqlite3` (gitignored).
- `start.spec` is the PyInstaller spec used to build the desktop bundle.
