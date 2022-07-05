# Family budget webapp

This is simple REST backend API project made with Django REST Framework

---

## Features

- [x] register user endpoint
  

- [x] CRUD for budgets (only for authenticated users)
- [x] sharing budgets with other users
  - [ ] an additional endpoint for sharing functionality
    

- [x] CRUD for incomes and expenses within budgets
- [ ] grouping incomes and expenses separately


- [ ] tests (only basic endpoints tests for now)


- [ ] filtering
- [ ] pagination

---

## Endpoints

- Standard django admin panel
```
admin/
```
- New user registration
```
register/
```
- users list
```
user/
```
- budgets CRUD
```
budgets/
budgets/<pk>/
```
- budgets shared with user
```
shared_budgets/
shared_budgets/<pk>/
```
- cash flow CRUD nested in budgets
```
budgets/<budget_pk>/cashflows/
budgets/<budget_pk>/cashflows/<pk>/
```
---

## Running under docker

To run app, use `docker-compose` within main directory:
```bash
docker-compose build
docker-compose up
```

DRF WebAPI is available under URL: `http://127.0.0.1`

---