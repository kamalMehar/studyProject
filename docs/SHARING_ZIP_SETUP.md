# Sharing this Django project as a ZIP (and running it on a friend's computer)

This document explains **what to include in the ZIP**, **what software your friend needs**, and **the exact steps to run the project** on another computer.

---

### 1) What to include (and what NOT to include) in the ZIP

#### Include
- **Project code** (everything under `studyapp/` and the top-level `requirements.txt`)
- **Templates & static assets** (already inside `studyapp/templates/` and `studyapp/public/static/`)
- **Media uploads (optional)**: `studyapp/public/media/` can be huge. Include it only if you want your friend to see existing uploaded files.

#### Do NOT include
- **Virtual environment**: do not include `myenv/`, `.venv/`, `venv/`, etc.
- **Python cache**: `__pycache__/`, `*.pyc`
- **Local/secret config**: anything like `.env`, `local_settings.py`, or files containing passwords/keys.

---

### 2) Software your friend needs to install

Minimum (to run locally):
- **Python** (recommend: Python 3.11+)
- **pip** (comes with Python)

Required for your current default database config:
- **PostgreSQL** (a running Postgres server)

Optional (only if you want Redis-backed Channels):
- **Redis** (a running Redis server)
  - If `REDIS_URL` is NOT set, the project falls back to an in-memory channel layer (fine for local/dev).

Recommended tools:
- A code editor (VS Code / Cursor)
- pgAdmin (optional GUI for Postgres)

---

### 3) Steps on your friend's computer (Windows / PowerShell)

#### A) Unzip and open a terminal
1. Unzip the project to a folder like `D:\Projects\studyapp`
2. Open PowerShell in the project root (where `requirements.txt` exists)

#### B) Create & activate a virtual environment
From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

#### C) Install Python dependencies

```powershell
pip install -r requirements.txt
```

#### D) Configure the database (Postgres)

Your project is currently configured to use **PostgreSQL** in `studyapp/studyapp/settings.py`.

On your friend's machine they must ensure:
- A Postgres server is running
- A database exists (example: `studyappproject`)
- Credentials in `DATABASES` match their local Postgres setup

**Option 1 (recommended for sharing):** Your friend edits these values in:
- `studyapp/studyapp/settings.py` → `DATABASES["default"]`

**Option 2 (more secure):** Before sharing, you move DB creds to environment variables and keep secrets out of the repo (recommended for any real deployment).

#### E) Run migrations
Go into the Django project folder (where `manage.py` is):

```powershell
cd .\studyapp\
python manage.py migrate
```

#### F) (Optional) Create test users
This project includes a management command documented in `studyapp/TEST_USERS.md`:

```powershell
python manage.py create_test_users
```

#### G) Start the server

```powershell
python manage.py runserver
```

Then open:
- `http://127.0.0.1:8000/study/home/`
- Admin: `http://127.0.0.1:8000/admin/`
- Staff login: `http://127.0.0.1:8000/account/login/`

---

### 4) If your friend wants Redis-backed WebSockets (optional)

If Redis is installed and running, set `REDIS_URL` before starting the server:

```powershell
$env:REDIS_URL = "redis://127.0.0.1:6379/0"
python manage.py runserver
```

---

### 5) Common problems / fixes

#### “Error loading psycopg2 / could not build wheels”
- On Windows, `psycopg2-binary` is typically easier than compiling `psycopg2`.
- Your `requirements.txt` currently lists **both** `psycopg2` and `psycopg2-binary`. It’s better to keep only one.

#### “password authentication failed for user postgres”
- Your friend's Postgres user/password/db name likely differ.
- Update `studyapp/studyapp/settings.py` → `DATABASES` to match their local Postgres credentials.

#### “WebSocket is not connecting”
- For local/dev, the in-memory layer works if you do **not** set `REDIS_URL`.
- For multi-process / production-like setups, install & run Redis and set `REDIS_URL`.

---

### 6) Important note before sharing

This repository currently contains hardcoded secrets (example: `SECRET_KEY` and Postgres password in settings).

Before sharing publicly (or deploying), you should:
- **Rotate** the Django `SECRET_KEY`
- Remove hardcoded DB password from `settings.py`
- Use environment variables for secrets


