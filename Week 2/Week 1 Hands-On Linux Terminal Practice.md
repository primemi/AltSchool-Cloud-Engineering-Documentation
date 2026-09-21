# 🐧 Linux System Administration & Lab Journal

> **The Cloud Journey Begins:** Excited to share that I’ve officially started my Cloud Computing journey at AltSchool Africa! As technology continues to shift toward scalable and distributed systems, I’m thrilled to dive deep into cloud infrastructure, architecture, and hands-on solutions. 🚀

This journal logs my hands-on technical labs, configuration steps, and critical terminal outputs as I master core Linux environments.

---

## 🛠️ Phase 1: Terminal Basics & User Account Setup

### 📢 Overview
Spent some quality time in the command line practicing essential system administration tasks in Ubuntu Linux. Troubleshooting directly in the terminal is the best way to understand how OS permissions, account structures, and group management work under the hood!

📄 **Full Notes & Documentation:** [View My Google Doc Breakdown](https://docs.google.com/document/d/1Vf7ZbceggUMmxQ15xUEJK5A8OinDV82SCIuxC4ernG4/edit?tab=t.0)

### 👤 User & Access Control
- [x] **Created a New System Account:** Used `sudo adduser kelechi` to set up a new user profile, configure passwords, and populate user information fields.
- [x] **Granted Administrator Privileges:** Added the user to the administrative sudo group using:
  ```bash
  sudo usermod -aG sudo kelechi
  ```
- [x] **Verified Account Setup:** Used `id kelechi` to check account creation, user ID (UID), primary group, and supplementary group assignments.

### 🔍 Operations & Key Troubleshooting Takeaways
* **Blind Input Security:** Handled Linux's security feature where typed passwords don't show characters on screen, successfully resolving initial password mismatch prompts.
* **Command Syntax Accuracy:** Mastered the exact syntax structure for modifying user accounts: `usermod -aG [GROUP] [USER]` after observing terminal output instructions when arguments were missing.
* **File Permissions & Ownership:** Practiced creating files, setting numeric permissions using `chmod`, and assigning ownership via `chown`.

*Tags: #Linux #SystemAdministration #DevOps #Ubuntu #CyberSecurity #TechLearning #CommandLine #ITInfrastructure*

---

## 🔐 Phase 2: Advanced Group Management, Sudoers & SSH Access

### 📢 Overview
Completed a practical lab focused on core Linux administration tasks—managing users, organizing group permissions, and setting up secure access models. Getting hands-on with files like `/etc/passwd`, `/etc/group`, and `/etc/sudoers` has given me a much stronger foundation in Linux security and identity management!

📄 **Full Lab Notes & Breakdown:** [View My Google Doc Lab Notes](https://google.com)

### 👥 Group Management & User Provisioning
* **Access Control Boundaries:** Created dedicated functional groups (`admin1`, `support`, `engineering`) to segregate roles.
* **User Provisioning:** Spawned isolated individual accounts and mapped them directly to their primary functional assignments:
  * `adminuser1` ➡️ `admin1`
  * `supportuser1` ➡️ `support`
  * `engineeringuser1` ➡️ `engineering`

### 🛡️ Privilege Escalation & Security Hardening
- [x] **Safely Configured Sudoers:** Modified `/etc/sudoers` securely using the `visudo` editor tool.
- [x] **Rule Enforcement:** Granted strict administrative execution capabilities to the `%admin1` group.
- [x] **Validation:** Successfully tested and verified root delegation using explicit `sudo` commands.

### 🔑 Cryptographic Authentication Standards
- [x] **SSH Key Generation:** Generated an asymmetrical **ED25519** cryptographic SSH key pair for `adminuser1`.
- [x] **Passwordless Access:** Established modern infrastructure security baselines by substituting basic passwords with strong cryptographic verification.

*Tags: #Linux #SystemAdministration #CloudComputing #DevOps #Security #LearningInPublic #TechJourney #learningoutloudwithaltschool*
