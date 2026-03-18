# Parking Management System

## Project Description

This is a Parking Management System developed using **FastAPI (backend)** and **React (frontend)**.
The system helps manage vehicle entry, exit, parking slots, pricing, and user authentication.

---

## Technologies Used

* **Frontend:** React (Vite)
* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **Authentication:** JWT (JSON Web Token)

---

## Features

* User Registration & Login
* JWT-based Authentication
* Role-based Access (Admin / Staff)
* Vehicle Entry & Exit Management
* Parking Slot Management
* Pricing Management
* Parking History Tracking

---

## Workflow

1. User logs in through frontend
2. Frontend sends request to backend API
3. Backend validates user and generates JWT token
4. Token is used for accessing protected routes
5. Vehicle entry/exit is managed through API calls
6. Backend interacts with PostgreSQL database
7. Results are sent back and displayed in frontend

---

## Database Configuration

The project uses PostgreSQL.
Database connection is configured using `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/parking_db
```

---

## How to Run the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Project Structure

```
backend/
 ├── app/
 │   ├── models/
 │   ├── schemas/
 │   ├── services/
 │   ├── repositories/
 │   ├── utils/
 │   └── routers/
 ├── main.py
 └── requirements.txt

frontend/
 ├── src/
 ├── components/
 ├── pages/
 └── package.json
```

---

## Environment Variables

* `DATABASE_URL`
* `SECRET_KEY`
* `ALGORITHM`
* `ACCESS_TOKEN_EXPIRE_MINUTES`

---

