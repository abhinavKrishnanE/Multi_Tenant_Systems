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
