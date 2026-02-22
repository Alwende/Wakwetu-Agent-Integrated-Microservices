# **PROJECT CHARTER: Project 2 (K8S-AGENT-2026)**

**Project Title:** Wakwetu Agentic-AI & Microservices Orchestration (AIME)

Lead Authority: Dan Alwende, PMP Designation: Technical PM | Solutions Architect | Enterprise Solutions Architect

**Status:** INITIATION

**Version:** 1.1 (Agentic AI Integrated)

---

### **1\. ROLE-BASED MISSION STATEMENT**

* As Enterprise Solutions Architect (ESA): I am aligning this build with the "Modernization" pillar of the Wakwetu Digital Strategy. The goal is to move the organization away from monolithic technical debt toward a Cloud-Native, AI-Supervised architecture that minimizes operational overhead and maximizes scalability.  
* As Solutions Architect (SA): I am designing a "Five-Nines" (99.999%) resilient infrastructure. I am selecting Amazon EKS (Fargate) to eliminate server management and Amazon Bedrock Agents to create an intelligent operational "control plane."  
* As Technical PM (TPM): I am responsible for the end-to-end delivery of the cluster. I am managing the transition from VPC networking to application deployment, ensuring that all security, cost, and compliance guardrails are met within the project timeline.

---

### **2\. BUSINESS CASE & STRATEGIC ALIGNMENT**

Wakwetu requires a production environment that is both resilient and intelligent.

* The Problem: Current application delivery is fragmented, and manual cluster management leads to configuration drift and operational burnout.  
* The Solution: An Agent-supervised EKS cluster. By integrating Agentic AI, we reduce the "Mean Time to Repair" (MTTR) by allowing a Bedrock Agent to monitor health and suggest remediations before a human is paged.

---

### **3\. TECHNICAL SCOPE (THE ARCHITECTURAL STACK)**

* Orchestration: Amazon EKS (Kubernetes Control Plane).  
* Execution Layer: AWS Fargate (Serverless Pods) – Decision: Eliminate EC2 maintenance to focus on code.  
* Intelligence: Amazon Bedrock Agents (Supervisor Pattern) with Knowledge Bases for Runbooks.  
* Security: IAM Roles for Service Accounts (IRSA) & Private VPC Networking.  
* Observability: Amazon CloudWatch Container Insights.

---

### **4\. PROJECT ROADMAP (THE TPM EXECUTION PLAN)**

| Phase | Milestone | Deliverable |
| :---- | :---- | :---- |
| **Phase 1** | **Network Fortress** | Multi-AZ VPC (6 Subnets, NATGW, IGW) |
| **Phase 2** | **The Control Plane** | EKS Cluster & Fargate Execution Profile |
| **Phase 3** | **Agentic Layer** | Bedrock Agent & API Action Group Integration |
| **Phase 4** | **Workload Deployment** | Containerized Banking App & Load Balancer |

---

### **5\. SUCCESS METRICS & SIGN-OFF**

1. High Availability: Successful automated failover across three Availability Zones.  
2. Agentic Operations: Agent successfully retrieves Pod Status via natural language query.  
3. Governance: All infrastructure defined via Code (GitHub) with 100% auditability.

---

### **INTERNAL FOLDER STRUCTURE (LOCAL SETUP)**

Before I open the AWS Console, ensure my **Desktop** folder Wakwetu-Agent-Integrated-Microservices is populated with these folders. **Organization is the mark of a Senior TPM.**

1. 📁 01-Governance/ (Save this Charter here as Wakwetu\_AIME\_Charter.md)  
2. 📁 02-Architecture-and-IaC/ (For VPC and EKS CloudFormation/Terraform)  
3. 📁 03-K8s-Manifests/ (For Kubernetes .yaml files)  
4. 📁 04-Agent-Config/ (For Bedrock Agent action groups & OpenAPI schemas)  
5. 📁 05-Artifacts/ (For your architecture diagrams and terminal logs)

---

### **PHASE 1 DEPLOYMENT: THE VPC FOUNDATION**

**ESA Requirement:** We must ensure maximum isolation.

**SA Requirement:** We need specific tagging for EKS to recognize the subnets.

**Task:** Navigate to the **VPC Console**. We are building the Wakwetu-AIME-VPC.

* **CIDR:** 10.0.0.0/16  
* **Public Subnets:** 3 (Tagged: kubernetes.io/role/elb \= 1)  
* **Private Subnets:** 3 (Tagged: kubernetes.io/role/internal-elb \= 1)


---
### **6. PROJECT LOG & EXECUTION HISTORY**

| Date | Milestone | Status | Notes |
| :--- | :--- | :--- | :--- |
| Feb 22, 2026 | Phase 1: Network Foundation | **COMPLETE** | Deployed Multi-AZ VPC via CloudFormation (4 Subnets validated). |
| Feb 22, 2026 | Phase 2: EKS Control Plane | **IN PROGRESS** | EKS Control Plane deployment initiated with Auto Mode enabled. Estimated completion: +15 minutes. |