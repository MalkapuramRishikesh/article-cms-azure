# Write-up: Deploying a CMS Application on Azure

## Introduction

This project is a Flask-based Content Management System (CMS) application deployed on Microsoft Azure. The application allows users to create, edit, and manage articles with images. It integrates Azure services such as Azure App Service, Azure SQL Database, Azure Blob Storage, and Microsoft Authentication (MSAL).

---

## Analyze, Choose, and Justify the Appropriate Resource Option

### 🔹 Virtual Machine (VM)

**1. Cost:**
Using a Virtual Machine requires continuous payment for compute resources, even when idle. Additional costs include storage, networking, and maintenance, making it more expensive.

**2. Scalability:**
Scaling must be configured manually using Virtual Machine Scale Sets, making it less flexible.

**3. Availability:**
High availability must be set up manually using availability zones or load balancers.

**4. Workflow:**
Requires manual setup of OS, runtime, dependencies, and security updates, increasing operational complexity.

---

### 🔹 Azure App Service

**1. Cost:**
App Service provides a cost-effective solution with flexible pricing and pay-as-you-go model.

**2. Scalability:**
Supports automatic scaling based on traffic and load.

**3. Availability:**
Provides built-in high availability with SLA guarantees.

**4. Workflow:**
Simplifies deployment with GitHub integration and removes the need to manage infrastructure.

---

## ✅ Final Choice: Azure App Service

Azure App Service is the best choice for deploying this CMS application.

**Justification:**
It simplifies deployment, reduces operational overhead, and provides built-in scalability and availability. It allows developers to focus on application logic instead of infrastructure management.

---

## Application Architecture

* **Flask Application** – Handles routing and business logic
* **Azure SQL Database** – Stores user and article data
* **Azure Blob Storage** – Stores uploaded images
* **Azure Active Directory (MSAL)** – Provides Microsoft login authentication
* **Azure App Service** – Hosts the web application

---

## Authentication (MSAL)

The application uses Microsoft Authentication Library (MSAL) to enable users to sign in with their Microsoft accounts.

Flow:

* User clicks “Sign in with Microsoft”
* Redirected to Microsoft login page
* Authorization code is returned
* Token is generated and stored in session
* User is logged into the application

---

## Logging and Monitoring

Application logs are captured using:

* Azure App Service Log Stream
  OR
* Local terminal logs

These logs help monitor:

* Successful login attempts
* Failed login attempts
* Application behavior

---

## Assess App Changes That Would Change the Decision

The decision to use Azure App Service may change if:

* Full control over OS is required
* Custom software or configurations are needed
* Advanced networking or security setups are required
* Non-web workloads or background services are needed

In such cases, a Virtual Machine would be more appropriate.

---

## Conclusion

Azure App Service is the most suitable platform for deploying this CMS application due to its ease of use, cost efficiency, scalability, and built-in availability. It significantly reduces infrastructure management effort and allows developers to focus on building application features.
