# Write-up: Deploying a CMS Application on Azure

## Analyze, choose, and justify the appropriate resource option for deploying the app

### 🔹 Virtual Machine (VM)

**1. Cost:**
Using a Virtual Machine requires paying for compute resources continuously, even when the application is idle. Additional costs include storage, networking, and maintenance. This makes it generally more expensive compared to platform-managed services.

**2. Scalability:**
Scaling in a VM setup is manual or requires additional configuration such as Virtual Machine Scale Sets. This makes it less flexible and slower to scale compared to managed services.

**3. Availability:**
High availability must be configured manually using availability sets or zones. The developer is responsible for ensuring uptime, backups, and failover mechanisms.

**4. Workflow:**
The workflow is more complex because the developer must manage OS updates, security patches, runtime environment, and server configurations. Deployment and maintenance require more effort.

---

### 🔹 Azure App Service

**1. Cost:**
Azure App Service provides a cost-effective solution with flexible pricing tiers. It supports scaling based on demand, which helps optimize cost by only using necessary resources.

**2. Scalability:**
App Service supports automatic scaling (auto-scale) based on traffic and load. This makes it highly efficient for handling varying workloads.

**3. Availability:**
It offers built-in high availability with SLA guarantees. Azure manages infrastructure, ensuring reliability and minimal downtime.

**4. Workflow:**
The workflow is simple and developer-friendly. Deployment can be done directly from GitHub, and Azure handles infrastructure, updates, and runtime management. This significantly reduces operational overhead.

---

### ✅ Final Choice: Azure App Service

Azure App Service is the most suitable choice for deploying the CMS application.

**Justification:**
App Service simplifies deployment and management by removing the need to handle infrastructure manually. It provides built-in scalability, high availability, and seamless integration with GitHub. For a web application like a CMS, which requires quick deployment and minimal maintenance, App Service is the best option. It allows developers to focus on application logic instead of infrastructure management.

---

## Assess app changes that would change your decision

The decision to use Azure App Service could change if the application requirements become more complex.

For example, if the application requires:
- Full control over the operating system
- Custom software installations or configurations
- Specialized networking or security setups
- Running background services or non-web workloads

In such cases, a Virtual Machine would be more appropriate.

Additionally, if the application needs fine-grained control over hardware resources or specific runtime environments not supported by App Service, switching to a VM would be necessary.

Thus, while App Service is ideal for standard web applications, a VM becomes a better choice when deeper infrastructure control and customization are required.
