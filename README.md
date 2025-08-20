# 🏥 HealthHub – A FastAPI & Masonite ORM Backend for Managing Patients, Medical Records, Appointments, and Medications
Creating a fast and efficient API by integrating FastAPI with Masonite ORM for data storage and retrieval and using the pydantic library. 

## Skills - 
> [!TIP]
> Web Frameworks, API Development, Backend Development


## ⚡ At a Glance
- **p95 latency:** `91 ms`
- **Stack:** FastAPI · Masonite ORM · SQLite/Postgres · JWT · Uvicorn
- **Ops:** Docker · GitHub Actions (CI/CD) · Render/Railway deployment
- **Reliability:** health probes, structured logs, input validation


## 🏗 Architecture

```text
           ┌──────────────┐
HTTP       │   FastAPI    │  Routers: /patients, /appointments, /medical_records, /medication, /auth, /overview
Requests → │  (app layer) │  Dependencies: JWT auth, role checks, pagination, validation
           └──────┬───────┘
                  │ calls
                  ▼
           ┌──────────────┐   CRUD + queries (filter, search)
           │  MasoniteORM │ ──────────────────────────────────────────────────────────┐
           └──────┬───────┘                                                           │
                  │ SQL                                                               │
                  ▼                                                                   ▼
           ┌────────────────┐                                                 ┌────────────────┐
           │  SQLite (dev)  │  or  PostgreSQL (prod)                          │  Redis/Celery  │ (optional: reminders, email jobs)
           └────────────────┘                                                 └────────────────┘

Observability: structured logs + health endpoints  |  CI/CD: GitHub Actions → deploy  |  Future: tracing, metrics

```

## Features
- CRUD for Patients, Appointments, MedicalRecords, Medications
- Auth & RBAC: signup/login (JWT), roles: patient | clinician | admin
- Pagination & filtering on list endpoints (limit, offset, q)
- Patient overview: /overview/patients/{id} returns records + meds + appointments
- Validation: Pydantic v2
