# OAuth - Google Authentication

- **Frontend**: Next.js
- **Backend**: FastAPI

## Getting Started

To get started with Google OAuth locally, follow these steps:

1. Clone this repository `git clone https://github.com/morshedul-antor/google-oauth.git`

### 3. Backend

At first create:
`client_id` and `client_secrect` from google console, copy the value and paste it into the
`oauth.register()` within the `main.py` file located at `backend/src`

Then, run this steps at `google-oauth/backend`:

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

cd src
python3 main.py
```

Access the `Fastapi` server at `http://localhost:8000`

### 4. Frontend

Run this steps at `google-oauth/frontend`:

```
npm install
npm run dev
```

Access the application in your browser at `http://localhost:3000`
