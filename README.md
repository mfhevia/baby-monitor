# Baby Monitor API

This project is a serverless FastAPI-based application deployed on AWS Lambda using Serverless Framework and `uv` for dependency management.

## 🚀 Setup and Installation

Ensure you have `uv` installed. If not, install it with:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1️⃣ Install Dependencies
Install all required dependencies with:

```sh
uv pip install
```

### 2️⃣ Generate `requirements.txt`
Export dependencies to `requirements.txt` for deployment:

```sh
uv export --frozen --no-dev --no-editable -o requirements.txt
```

## 🏗️ Running the Application Locally
To run the FastAPI application locally, execute:

```sh
uv sync
uv run fastapi dev ./app/api/main.py
```

## 🚀 Deploying to AWS Lambda

### 1️⃣ Install Serverless Framework
If you haven't installed Serverless, do it with:

```sh
npm install -g serverless
```

### 2️⃣ Deploy the Application
To deploy using Serverless Framework, run:

```sh
serverless deploy
```

### 3️⃣ Remove Deployment
If you need to remove the deployed service:

```sh
serverless remove
```

---

This project follows a lightweight, serverless-first approach, making it easy to develop, deploy, and maintain. 🚀

