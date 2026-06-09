# DevSecOps Pipeline Architecture

Developer
↓
GitHub Repository
↓
GitHub Actions
↓
Semgrep (SAST)
↓
SonarQube (Code Quality & Security)
↓
Trivy (Container Vulnerability Scan)
↓
Docker Image Build
↓
Container Registry
↓
Kubernetes Deployment
↓
Continuous Monitoring

## Security Gates

1. Semgrep must pass.
2. SonarQube quality gate must pass.
3. Trivy critical vulnerabilities must be zero.
4. Docker image must build successfully.
5. Kubernetes deployment validation must pass.
