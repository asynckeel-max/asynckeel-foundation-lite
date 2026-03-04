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
```

Visit: http://127.0.0.1:8000/docs

## The Problem

Most FastAPI SaaS projects start simple — and slowly turn into:

- Mixed responsibilities
- Fat routers
- Scattered business logic
- Hard-to-test services

AsyncKeel provides a clean, minimal structure from day one.

---

## Design Principles

- Lean dependencies
- Clear service layer separation
- Async-first architecture
- Environment-driven configuration
- Built for maintainability, not demos

---

## Who Is This For?

- Indie hackers building SaaS products
- Developers who care about backend architecture
- Builders who don't want to reinvent auth & structure every time

---

Full SaaS version (Auth, Payments, Production patterns) coming soon.


