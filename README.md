# AsyncKeel Foundation Lite

A minimal, opinionated FastAPI foundation for indie hackers building SaaS products.

## Why AsyncKeel?

Most FastAPI projects start simple — and become messy.

AsyncKeel provides a clean, production-ready structure from day one.

## Structure

app/
 ├─ api/
 ├─ core/
 ├─ services/
 ├─ models/
 ├─ schemas/
 ├─ db/
 ├─ tests/

## Philosophy

- Lean dependencies
- Clean service layer
- Async-first
- Built for maintainability

## Quick Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

Visit: http://127.0.0.1:8000/docs
