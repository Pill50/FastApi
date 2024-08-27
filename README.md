# FastApi Assignment

## Overview

This project is a web application built with FastAPI, PostgreSQL, and Alembic for database migrations. Follow the steps below to set up the development environment, migrate your database schema, and run the application.

## Prerequisites

- Docker
- Python 3.8 or higher
- Pip (Python package installer)

## Setup

### 1. **Install Required Python Packages**

First, install all required Python packages by running:

```bash
pip install -r requirements.txt
```

### 2. **Run PostgreSQL Using Docker**
To start a PostgreSQL container, execute the following command:

```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=123456 \
  -e POSTGRES_DB=fastapi_db \
  -p 5432:5432 \
  postgres:latest
```

### 3. **Migrate Database Tables Using Alembic**

```bash
alembic upgrade 647be04a6025  # Migrate to create the company table
alembic upgrade 81c33b22fe78  # Migrate to create the user table
alembic upgrade f0a9ecd9aa94  # Migrate to create the task table
```

### 4. **Run the application**
```bash
cd app
uvicorn main:app --reload
```

### 5. **Access the API Documentation**
Once the application is running, you can view the interactive API documentation at:

http://localhost:8000/docs

### 6. **Note**
Two accounts are setting by default:
- User account
    - username: user
    - password: 123456
- Admin account
    - username: admin
    - password: 123456

## Author
- Name: Tran Vinh Phuc
- Email: vinhphuccse@gmail.com 

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.