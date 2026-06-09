# Dockerization

## Objective

Containerize the application to ensure consistency across development, testing, and production environments.

## Steps

1. Created Dockerfile.
2. Added Flask application.
3. Exposed port 5000.
4. Built Docker image.
5. Tested container locally.

## Commands

```bash
docker build -t devsecops-demo .
docker run -p 5000:5000 devsecops-demo
```

## Result

Application successfully deployed in a Docker container and accessible through localhost.
