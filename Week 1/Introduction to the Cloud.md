# ☁️ Core Computing Architecture: SDLC & Cloud Service Models

This module explores the core foundations of system delivery, spanning the theoretical frameworks of software deployment life cycles and the practical consumption categories of modern cloud service delivery models.

---

## 🌀 1. The Software Development Life Cycle (SDLC)

The **Software Development Life Cycle (SDLC)** is a structured framework used by engineering teams to design, develop, test, and deploy high-quality software systems efficiently.

### 📋 The Phases of SDLC

* **1. Requirement Analysis:** Gathering business constraints, user demands, and technical dependencies from stakeholders.
* **2. System Design:** Architecting software components, data models, infrastructure topologies, and interface definitions.
* **3. Implementation (Coding):** Translating design specifications into actual application logic using target programming languages.
* **4. Testing & QA:** Validating software stability against original business logic, security flaws, performance benchmarks, and functional edge cases.
* **5. Deployment:** Releasing the fully tested code artifact into production environments using systematic release methodologies.
* **6. Maintenance & Operations:** Monitoring logs, patching emerging bugs, upgrading libraries, and scaling systems dynamically.

---

## 🏛️ 2. Cloud Computing Service Models

Cloud computing eliminates the need to buy and maintain physical servers. Instead, infrastructure responsibilities are divided between you and the cloud provider using a framework called the **Shared Responsibility Model**.

### 📦 Infrastructure as a Service (IaaS)
* **Definition:** Provides raw computing resources over the internet on a pay-as-you-go basis. You rent the foundational components without managing physical wires or hardware.
* **What the Provider Manages:** Physical data centers, cooling systems, network switches, storage drives, and physical hypervisors.
* **What You Control:** The Operating System (OS), installed middleware, runtime runtimes, applications, and networking traffic rules.
* **Examples:** AWS EC2, Google Compute Engine (GCE), Microsoft Azure VMs, DigitalOcean Droplets.

### ⚙️ Platform as a Service (PaaS)
* **Definition:** Provides a pre-configured environment optimized for building, testing, and deploying applications without the overhead of operating system maintenance.
* **What the Provider Manages:** All physical layers, the OS kernel, automated security patching, middleware configuration, and runtime execution layers.
* **What You Control:** Strictly the source code of the application and configuration settings specific to your environment.
* **Examples:** AWS Elastic Beanstalk, Heroku, Render, Google App Engine.

### 💻 Software as a Service (SaaS)
* **Definition:** Delivers a complete, ready-to-use software product managed entirely by the vendor through a web browser or client interface.
* **What the Provider Manages:** The entire technical stack from physical data center rooms up to the frontend UI rendering.
* **What You Control:** Basic end-user application settings and user profiles.
* **Examples:** Google Workspace (Docs/Slides), Microsoft 365, Slack, Zoom, Salesforce.

---

## 📊 Summary: The Shared Responsibility Matrix

| Infrastructure Layer | On-Premise | IaaS | PaaS | SaaS |
| :--- | :---: | :---: | :---: | :---: |
| **Applications** | 👤 You | 👤 You | 👤 You | ☁️ Vendor |
| **Data & Governance** | 👤 You | 👤 You | 👤 You | ☁️ Vendor |
| **Runtime / Middleware** | 👤 You | 👤 You | ☁️ Vendor | ☁️ Vendor |
| **Operating System (OS)** | 👤 You | 👤 You | ☁️ Vendor | ☁️ Vendor |
| **Virtualization / Hypervisors**| 👤 You | ☁️ Vendor | ☁️ Vendor | ☁️ Vendor |
| **Physical Compute & Servers** | 👤 You | ☁️ Vendor | ☁️ Vendor | ☁️ Vendor |
| **Physical Network & Storage** | 👤 You | ☁️ Vendor | ☁️ Vendor | ☁️ Vendor |
| **Data Center Facilities** | 👤 You | ☁️ Vendor | ☁️ Vendor | ☁️ Vendor |
