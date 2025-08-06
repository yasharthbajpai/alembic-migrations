
# 🚀 Python Database Migrations with Alembic & Docker

A hands-on project demonstrating how to manage database schema changes in a Python application using Alembic, with a PostgreSQL database running in a Docker container.

---

## ✨ Tech Stack

- **Language**: Python 3.10
- **Database**: PostgreSQL
- **Containerization**: Docker
- **ORM**: SQLAlchemy
- **Migration Tool**: Alembic
- **Environment Management**: Conda

---

## 🏁 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Make sure you have the following tools installed:
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Conda (Miniconda or Anaconda)](https://docs.conda.io/en/latest/miniconda.html)

### 1. Clone the Repository

First, clone this project to your local machine.

```bash
git clone <your-repository-url>
cd my_cool_project
````

### 2\. Start the Database 🐳

The project uses Docker to run a PostgreSQL database in a container. The configuration is defined in `docker-compose.yml`.

To start the database, run:

```bash
docker-compose up -d
```

This will start a PostgreSQL server accessible on `localhost:5430`.

### 3\. Set Up the Python Environment 🐍

We use Conda to manage our Python packages and environment.

**a. Create and activate the Conda environment:**

```bash
# Create the environment
conda create --name my_project_env python=3.10

# Activate it
conda activate my_project_env
```

**b. Install the required packages:**

```bash
conda install -c conda-forge alembic sqlalchemy psycopg2
```

### 4\. Apply Database Migrations ✅

With the environment set up and the database running, apply all existing migrations to create the database schema.

```bash
alembic upgrade head
```

Your database is now up-to-date and ready to use\!

-----

## 🛠️ Alembic Workflow

This is the standard workflow for making changes to the database schema.

### Generating a New Migration

Whenever you change a model in `my_app/models.py` (e.g., add a new table or a new column), generate a new migration script automatically.

```bash
# Example: alembic revision --autogenerate -m "Add bio column to users table"
alembic revision --autogenerate -m "A short description of the change"
```

This creates a new file in `migrations/versions/`. **Always review this file** to ensure it's correct before proceeding.

### Applying a Migration (Upgrading)

To apply the latest migration(s) to your database, run:

```bash
alembic upgrade head
```

### Reverting a Migration (Downgrading)

To undo the very last migration, run:

```bash
alembic downgrade -1
```

-----

## 🗄️ Connecting to the Database Directly

You can connect directly to the database inside the Docker container to run raw SQL queries using `psql`.

1.  **Get a shell inside the container:**

    ```bash
    docker exec -it my_project_db psql -U myuser -d mydatabase
    ```

2.  **Enter the password** when prompted: `mypassword`

3.  **Run SQL commands:**

    ```sql
    -- Example: See all tables
    \dt

    -- Example: View all data in the users table
    SELECT * FROM users;

    -- Example: Exit the psql shell
    \q
    ```

-----

## 📄 License

This project is licensed under the MIT License.

Copyright (c) 2025 Yasharth
