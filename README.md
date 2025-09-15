# Multi-Tenant Systems in Django  

This repository demonstrates **different multi-tenancy approaches in Django**, allowing developers to understand and experiment with various ways to isolate tenant data in a SaaS-like environment.  

It is designed **for learning purposes**, helping developers explore how multi-tenancy can be implemented in real-world scenarios.  

---

## 🌐 What is Multi-Tenancy?  
**Multi-tenancy** allows a single application to serve multiple clients (tenants) while keeping their data **isolated**.  

This repository demonstrates three common strategies:  

---

### 1. Separated Database (`seperatedb`)  

Each tenant has its own **dedicated database**. All models for a tenant are stored in that tenant's database.  

- Each tenant is assigned a separate database.  
- When a tenant makes a request, the application connects to that tenant's database dynamically using routers.  

**✅ Pros**  
- Strong data isolation.  
- Easy backup, restore, and scaling per tenant.  

**⚠️ Cons**  
- Higher resource usage if there are many tenants.  
- Database management and migrations can be complex.  

---

### 2. Separated Schema (`seperateschema`)  

All tenants share a **single database**, but each tenant has its own **schema**. Models are duplicated in each schema.  

- A single database is used.  
- Each tenant has its own schema (`tenant1_schema`, `tenant2_schema`, etc.).  
- Queries are routed to the correct schema based on the tenant.  

**✅ Pros**  
- Balanced isolation and resource efficiency.  
- Easier to manage compared to separated databases.  

**⚠️ Cons**  
- Schema migrations must be applied for all tenant schemas.  
- Some database engines may have limitations on schema count.  

---

### 3. Shared Schema (`sharedschema`)  

All tenants share the **same database and schema**. Tenant data is distinguished using a **tenant identifier column** (e.g., `tenant_id`).  

- One database, one schema.  
- Tenant separation is achieved at the row level.  

**✅ Pros**  
- Cost-effective and simple to manage.  
- Easy to scale horizontally.  

**⚠️ Cons**  
- Careful handling required to prevent accidental data leaks.  
- Less isolation compared to other approaches.  

---

## 🚀 Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/abhinavKrishnanE/Multi_Tenant_Systems.git
cd Multi_Tenant_Systems
```
### 2. Add .env file

- Create a .env file in the root of the project.
- Add your database credentials:
DB_NAME=your_db_name 
DB_USER=your_db_user 
DB_PASSWORD=your_db_password 
DB_HOST=your_db_host 
DB_PORT=your_db_port

### 3. Choose a multi-tenancy approach

- Navigate to the folder of your choice (seperatedb, seperateschema, or sharedschema).
- Each folder contains a Django project configured for that specific approach.

### 4. Run the project

```bash
python manage.py migrate
python manage.py runserver
```

### Notes:
- This repository is intended for learning purposes.
- Each approach shows a working setup to understand data isolation techniques.
- Developers can experiment with creating tenants, isolating data, and testing queries to see how each approach behaves.
