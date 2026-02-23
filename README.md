## **README: Wakwetu Agentic-AI & Microservices Orchestration (AIME)**

Real talk: Infrastructure is just a cost center until it’s intelligent. This repository contains the end-to-end implementation of a **Cloud-Native Banking Microservice** supervised by an **Agentic AI Control Plane**. This isn't a sandbox experiment; it's a production-ready blueprint for autonomous system oversight.

---

### **Project Vision**

As part of the **Wakwetu Digital Strategy**, this project replaces manual cluster management with an AI-supervised execution model. By bridging **Amazon EKS** and **Amazon Bedrock**, we achieve a self-documenting, queryable infrastructure that reduces operational overhead for Technical PMs and Architects.

---

### **Core Architectural Stack**

* **Orchestration**: Amazon EKS (Elastic Kubernetes Service) utilizing Auto Mode for serverless pod execution.
* **Intelligence**: Amazon Bedrock Agents powered by **Claude 3.5 Sonnet**.
* **Runtime**: Containerized Python/Flask Banking API.
* **Bridge**: AWS Lambda acting as a secure Action Group executor.
* **Schema**: OpenAPI 3.0 specification for natural language tool-calling.

---

### **Repository Structure**

Organization is the mark of a Senior TPM. The repository is structured to maintain 100% auditability:

* 📁 `01-Governance/`: Project Charter and closure documentation.
* 📁 `02-Architecture-and-IaC/`: VPC networking and EKS configuration.
* 📁 `03-K8s-Manifests/`: Kubernetes deployment and service YAMLs.
* 📁 `04-Agent-Config/`: Bedrock Agent action groups and OpenAPI schemas.
* 📁 `05-Artifacts/`: Terminal logs and execution history.

---

### **Deployment Workflow**

#### **1. Microservice Rollout**

Build and deploy the banking backend to the EKS cluster:

```bash
docker build -t wakwetu-banking-backend .
docker tag wakwetu-banking-backend:latest [AWS_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/wakwetu-banking-backend:latest
docker push [AWS_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/wakwetu-banking-backend:latest
kubectl rollout restart deployment wakwetu-banking-backend

```

#### **2. Agentic Integration**

The Bedrock Agent utilizes an **AWS Lambda bridge** to query the EKS Load Balancer. This requires a specific IAM ModelInvocation policy to handle foundation model lifecycles:

```bash
aws iam put-role-policy \
    --role-name AmazonBedrockExecutionRoleForAgents_6EJVDT2NFMB \
    --policy-name BedrockModelInvoke \
    --policy-document '{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Action": "bedrock:InvokeModel","Resource": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-*"}]}'

```

---

### **Success Metrics Achieved**

* **Zero-Downtime Deployment**: Verified via `kubectl` rollouts.
* **Agentic Sovereignty**: Successfully retrieved real-time banking data (Balance: **$5,250.75**) via natural language queries.
* **Security Compliance**: Resolved Anthropic use-case gates and implemented least-privilege Resource-based policies for Lambda.

---

### **Project Closure**

**Status**: COMPLETED (Feb 23, 2026)
**Lead Authority**: Dan Alwende, PMP