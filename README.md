# Backend – Gestion de Stock

A RESTful API for managing product inventory built with **Django** and **Django REST Framework**, using **PostgreSQL** as the database.

## ⚙️ Features

- CRUD for products
- Image upload support
- CORS-enabled API for frontend
- Dockerized environment

## 🧪 API Endpoints

| Method | Endpoint                  | Description         |
|--------|---------------------------|---------------------|
| GET    | `/api/produits/`          | List all products   |
| POST   | `/api/produits/`          | Create a product    |
| GET    | `/api/produits/:id/`      | Retrieve product    |
| PUT    | `/api/produits/:id/`      | Update product      |
| DELETE | `/api/produits/:id/`      | Delete product      |
