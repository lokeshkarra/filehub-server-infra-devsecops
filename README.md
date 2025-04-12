
# 📁 FileHub Server - Cloud-Native Django Backend

A scalable, secure, and production-ready **Django backend** for a file management platform — built with modern DevSecOps principles using **Kubernetes, Jenkins, Argo CD, Terraform, AWS, Prometheus, and Grafana**.

---

## Architecture

<img src="https://github.com/lokeshkarra/filehub-server-infra-devsecops/blob/main/architecture-diagram/server-hld.png" width="800"/>

<img src="https://github.com/lokeshkarra/filehub-server-infra-devsecops/blob/main/architecture-diagram/architecture.png" width="800"/>


---

## 🚀 Tech Stack

| Layer         | Tech Used                                      |
|---------------|------------------------------------------------|
| **Backend**   | Django REST Framework, PostgreSQL (AWS RDS)    |
| **CI/CD**     | Jenkins (CI), Argo CD (CD), Docker             |
| **Infra**     | AWS EKS, RDS, S3, VPC, IAM — provisioned via Terraform |
| **Monitoring**| Prometheus, Grafana, Node Exporter, Django Metrics |
| **Storage**   | AWS S3 for static files and uploads            |
| **Frontend**  | React + TypeScript (Hosted on Netlify)         |

---

## 📦 Features

- 🧾 RESTful API for file management (upload, list, delete)
- ☁️ Static files uploaded directly to **AWS S3**
- 🐳 Dockerized and deployed via **Kubernetes (EKS)**
- 🔁 Continuous Integration via **Jenkins**
- 🚀 Continuous Deployment via **Argo CD** (GitOps)
- 📈 Application metrics via **django-prometheus**
- 📊 Monitoring dashboards via **Grafana**
- 🔐 Follows DevSecOps best practices

---

## 🧩 Architecture

```txt
             +------------------+
             |  Netlify Frontend|
             +--------+---------+
                      |
                      v
             +--------+---------+
             | Django Backend   |  <-- EKS Deployment (Docker)
             | REST API         |
             +--------+---------+
                      |
    +-----------------+------------------+
    |                                    |
    v                                    v
PostgreSQL (RDS)                 AWS S3 (Static files)
```

---

## ⚙️ Frontend Repo 


[https://github.com/lokeshkarra/filehub-client.git](https://github.com/lokeshkarra/filehub-client.git)



---

## ⚙️ Infrastructure as Code (IaC)

Infrastructure is provisioned using **Terraform**:

- `terraform/vpc` - VPC, subnets, routing
- `terraform/iam` - IAM roles for EKS
- `terraform/eks` - EKS cluster + node groups

### 🚀 Deploy:
```bash
terraform init
terraform apply
aws eks update-kubeconfig --name <cluster-name> --region <region>
```

---

## 🛠️ Jenkins CI Pipeline

The Jenkins pipeline automates:

- Code checkout and build
- Docker image build + push
- Kubernetes manifest update (optional)
- Git commit triggers Argo CD sync

---

## 🌀 Argo CD for GitOps Deployment

- Automatically deploys any change in Kubernetes YAMLs
- Keeps Git and cluster always in sync

```bash
argocd app create filehub-backend \
  --repo https://github.com/yourusername/your-k8s-manifests.git \
  --path k8s \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default
```

---

## 🔐 Secure Secrets with SealedSecrets

All sensitive environment variables and Django secrets are stored using **SealedSecrets**, ensuring Kubernetes secrets are encrypted and Git-safe.

- Replace `k8s/secrets.yaml` with `k8s/sealed-secret.yaml`
- Sealed using `kubeseal` and Bitnami SealedSecrets controller
- Automatically decrypted and mounted at runtime in cluster

### 🔑 How to seal a secret:

```bash
kubectl create secret generic django-secret \
  --from-literal=SECRET_KEY='your-secret-key' \
  --dry-run=client -o yaml > secret.yaml

kubeseal --controller-name=sealed-secrets \
  --controller-namespace=kube-system \
  -o yaml < secret.yaml > sealed-secret.yaml
```

---

## 📊 Monitoring

- Prometheus scrapes Django metrics via `/metrics` endpoint
- Grafana dashboards visualize request count, latency, and error rates
- Node Exporter monitors system-level metrics

> Dashboards auto-provisioned via Terraform or Helm

---

## 🔍 Django Metrics Integration

```python
# settings.py
INSTALLED_APPS += ["django_prometheus"]
MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    ...
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

# urls.py
path('', include('django_prometheus.urls'))
```

---

## 🧪 API Testing

Use the following tools for testing:

- Postman collection (`/docs/postman_collection.json`)
- Swagger (optional via DRF extensions)

---

## 🚧 Work in Progress

- [x] Backend API
- [x] Docker & Kubernetes deployment
- [x] Argo CD GitOps
- [x] Jenkins CI Pipeline
- [x] SealedSecrets for secure secrets
- [ ] Prometheus + Grafana monitoring
- [ ] Unit and integration tests
- [ ] Advanced S3 permission hardening

---

## 🧠 Learning Outcomes

- Kubernetes app deployment with EKS
- Secure AWS infrastructure provisioning via Terraform
- GitOps CI/CD using Argo CD
- End-to-end monitoring with Prometheus and Grafana
- Production-grade Django application design

---

## 📁 Repo Structure

```
.
├── app_code/
│   └── backend/
│       ├── Dockerfile
│       └── Django Server Code...
├── jenkins-pipeline/
│   └── jenkinsfile-backend
├── terraform/
│   ├── main.tf
│   ├── variable.tf
│   ├── outputs.tf
│   ├── vpc/
│   ├── eks/
│   ├── ec2/      
│   └── iam/
└──  k8s/
    ├── deployment.yaml
    ├── service.yaml
    ├── sealed-secret.yaml   <-- 🔐 Sealed Secret
```

---

## 📜 License

[Apache 2.0](https://github.com/lokeshkarra/filehub-server-infra-devsecops?tab=Apache-2.0-1-ov-file)


