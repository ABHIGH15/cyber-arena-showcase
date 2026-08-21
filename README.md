<div align="center">

# ⚡ CYBER ARENA
### Automated Adversarial Defense Verification & Bounded Red-Team Platform

[![Status: Production Prototype](https://img.shields.io/badge/Status-Research_Prototype_Freeze-00e5ff?style=for-the-badge&logo=shield)](https://github.com/ABHIGH15/cyber-arena-showcase)
[![Engine: Dual-Oracle Verification](https://img.shields.io/badge/Engine-Dual--Oracle_Verification-00ff66?style=for-the-badge&logo=docker)](https://github.com/ABHIGH15/cyber-arena-showcase)
[![Isolation: Docker cgroups & cap-drop](https://img.shields.io/badge/Isolation-Docker_cgroups_%26_cap--drop-ff003c?style=for-the-badge&logo=linux)](https://github.com/ABHIGH15/cyber-arena-showcase)
[![Frontend: React 18 / Vite 5](https://img.shields.io/badge/Frontend-React_18_%2F_Vite_5-61dafb?style=for-the-badge&logo=react)](https://github.com/ABHIGH15/cyber-arena-showcase)
[![Backend: Express 5 / Node.js](https://img.shields.io/badge/Backend-Express_5_%2F_Node.js-68a063?style=for-the-badge&logo=node.js)](https://github.com/ABHIGH15/cyber-arena-showcase)
[![Database: PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL_15-336791?style=for-the-badge&logo=postgresql)](https://github.com/ABHIGH15/cyber-arena-showcase)

<br/>

**A next-generation cybersecurity research platform that elevates traditional Capture-The-Flag (CTF) competitions into dynamic, dual-oracle defensive invariant verification and live bounded adversarial red-team matches.**

[Explore Architecture](#-system-architecture) • [Research Novelty](#-the-core-problem--research-novelty) • [Visual Showcase](#-product-tour--visual-showcase) • [Mathematical Foundations](#-formal-mathematical-foundations) • [Confidential Code Access](#-source-code-access--recruiter-inquiries)

---

</div>

<br/>

## 🎯 Executive Summary & Impact

Traditional cybersecurity competitions evaluate **only offense**: static challenge containers are attacked once, rewards are binary (flag captured or not), and defensive code quality is never tested.

**Cyber Arena fundamentally changes this paradigm:**
1. **Dynamic Defensive Code Intake**: Defenders submit actual application source code patches (`app.js`) to fix live vulnerabilities.
2. **Ephemeral Docker Sandbox Isolation**: Each patch is compiled in an isolated, resource-constrained container (`--cpus=0.5 --memory=512m --pids-limit=100 --cap-drop=ALL`).
3. **Dual-Oracle Invariant Verification**: Candidate patches are continuously checked against an unpatched Reference Oracle to confirm baseline exploitability and verify genuine defense.
4. **Deterministic 6-Axis Mutation Matrix**: Defensive patches are subjected to 17 versioned mutation vectors (character encodings, case variations, whitespace alterations, comment injections, syntax variations, and paired differential boolean checks).
5. **Multi-Dimensional Resilience Scoring**: Quantifies both **Security Resilience ($R$)** against adversarial mutations and **Functional Correctness ($F$)** to prevent over-blocking and denial-of-service.
6. **Live Bounded Red-Team Arena**: Verified defender containers are promoted into 20-minute adversarial match windows where human attackers probe the defended container in real time using a unified classifier.

---

## 🔬 The Core Problem & Research Novelty

| Dimension | Traditional CTF / Cyber Range | **Cyber Arena (This Platform)** |
| :--- | :--- | :--- |
| **Evaluation Focus** | Offensive exploits only | **Adversarial Defense Verification + Live Exploitation** |
| **Challenge State** | Static, pre-compiled, vulnerable | **Dynamic runtime patched candidates** |
| **Defense Verification** | None (no patch submission) | **Automated AST & source compilation in isolated sandbox** |
| **Evasion Testing** | Single static payload test | **Deterministic 6-axis mutation engine (17 attack vectors)** |
| **Over-Blocking Prevention** | Ignored (naive regexes pass) | **Functional Smoke Invariant ($F$) guarantees no DoS** |
| **Attacker-Defender Loop** | Asynchronous / disconnected | **Bounded 20-min Live Arena with real-time target switching** |
| **Scoring Model** | Binary Flag submission | **Dual-dimension composite scoring ($R\% + F\% + \text{Flags}$)** |

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph DEFENDER_PIPELINE["🛡️ 1. Defender Ingestion & Isolation"]
        D[Defender Operative] -->|1. Submit Source Patch| API[API Gateway & Controller]
        API -->|2. Ingest Patch| SB[Ephemeral Docker Sandbox Runner]
        SB -->|3. Strict Limits: cpus=0.5, cap-drop=ALL| CT[Candidate Container :80]
    end

    subgraph ORACLE_EVALUATION["🔬 2. Dual-Oracle & Mutation Matrix"]
        CT -->|4. Functional Smoke Invariant| FS{Admin Auth Valid? (F)}
        FS -->|Passed F=100%| ME[Deterministic 6-Axis Attack Matrix]
        FS -->|Failed F=0%| RJ[Reject Patch: Over-Blocking / DoS]
        ME -->|5. 17 Mutation Vectors| RO[Dual-Oracle Differential Classifier]
        RO -->|6. Compute Resilience R%| ER[Explainability & Telemetry Report]
    end

    subgraph LIVE_ARENA["⚔️ 3. Bounded Red-Team Live Arena"]
        ER -->|7. Auto-Promote Container| LM[20-Min Bounded Match Window]
        A[Red-Team Attacker] -->|8. Interactive Payload Forge| AC[Attacker Console]
        AC -->|9. Proxied Attack Payload| LM
        LM -->|10. Telemetry & Scoring| LB[Composite Global Leaderboard]
    end
```

---

## 📸 Product Tour & Visual Showcase

### 1. Challenge Command Center & Active Live Targets
> Real-time monitoring of available vulnerable challenge labs and active live defender instances.

![Cyber Arena Dashboard](screenshots/01_dashboard.png)

---

### 2. Defender IDE & 1-Click Sandbox Evaluation Runner
> Integrated browser code editor featuring AST templates, immediate Docker sandbox compilation, functional smoke invariants, and automated 6-axis mutation benchmark execution in a single click.

![Defender IDE & Evaluation](screenshots/02_defender_submission.png)

---

### 3. Faculty Explainability & 6-Axis Mutation Matrix
> Granular audit dashboard breaking down candidate patch resilience across all 6 mutation axes (Encoding, Case Shifts, Comments, Whitespace, Syntax, Differential Boolean Logic) and displaying transparent `DB_ERROR` classification guarantees.

![Explainability & Mutation Report](screenshots/03_explainability_report.png)

---

### 4. Live Adversarial Red-Team Arena & Payload Forge
> Full-screen interactive attacker terminal equipped with categorized attack matrix chips, multi-target defender container switching, high-contrast digital match window countdown (`20m 00s Total`), and instant match conclusion controls.

![Live Attacker Arena](screenshots/04_attacker_arena.png)

---

### 5. Research Architecture & Formal Verification Inspector
> Interactive academic explainability interface detailing container isolation guarantees, dual-oracle decision theorems, and mathematical scoring models.

![System Architecture Visualizer](screenshots/05_architecture_visualizer.png)

---

### 6. Composite Multi-Dimensional Leaderboard
> Real-time rankings aggregating Defensive Engineering points ($R\% \times \text{Points}$ for verified patches) and Offensive Flag Captures + Arena Breaches.

![Composite Leaderboard](screenshots/06_leaderboard.png)

---

### 7. Historical Audit & Telemetry Log
> Filterable activity audit trail with scoped switching between "My Activity" and "Global Telemetry" feeds.

![Audit & Telemetry Log](screenshots/07_match_history.png)

---

## 📐 Formal Mathematical Foundations

### 1. Security Resilience Metric ($R$)
$$\text{Resilience } R = \left( \frac{\text{Blocked Valid Attacks}}{\text{Total Evaluated Mutation Vectors}} \right) \times 100\%$$

### 2. Functional Invariant Metric ($F$)
$$F = \begin{cases} 100\% & \text{if } \text{VerifyAuthenticAuth}(\text{Patch}, \text{Creds}_{\text{valid}}) \to \text{SUCCESS} \\ 0\% & \text{if } \text{DoS or Over-blocking is detected} \end{cases}$$

### 3. The `DB_ERROR` Security Classification Theorem
> In standard web application environments, unhandled database errors (e.g. SQLite `SQLITE_ERROR`, PostgreSQL syntax exceptions) reveal internal database structure, enable error-based extraction, and represent unhandled injection state. **Cyber Arena formally classifies all unhandled DB Errors as Security Failures (Attack SUCCESS), preventing superficial regex filters from scoring falsely high.**

---

## 🔒 Security & Sandbox Isolation Guarantees

Cyber Arena enforces enterprise-grade multi-tenant containment on all submitted code patches:
- **CPU Quota**: Max 0.5 Cores (`--cpus="0.5"`) via Linux cgroups.
- **Memory Ceiling**: Strict 512MB RAM cap (`--memory="512m"`), preventing out-of-memory host exhaustion.
- **Process Cap**: Max 100 concurrent PIDs (`--pids-limit=100`), mitigating fork-bomb vectors.
- **Capability Dropping**: Strips all Linux root capabilities (`--cap-drop=ALL`).
- **Network Isolation**: Isolated per-evaluation Docker bridge network with localhost port binding (`127.0.0.1::80`).
- **Automated Janitor Reaper**: 15-second background sweeper that automatically terminates expired match containers, reclaims orphaned memory, and prunes unused bridge networks.

---

## 🛠️ Technology Stack & Engineering Highlights

```text
├── Frontend Architecture
│   ├── Framework: React 18.2 + Vite 5 (Sub-700ms production builds)
│   ├── Design System: Pure CSS Variables, Cyber Glassmorphism, Zero Heavy UI Frameworks
│   ├── Routing & State: React Router DOM 6.23, Custom Event-driven Toast & Modal System
│   └── Icons: Lucide React
│
├── Backend & Evaluation Engine
│   ├── Server Runtime: Node.js 24 + Express 5.2 (RESTful Architecture)
│   ├── Orchestration: Native Docker Engine CLI Integration + cgroups API
│   ├── Persistence: PostgreSQL 15 (ACID-compliant CTE scoring queries)
│   ├── Isolation: In-memory SQLite3 harnesses + Ephemeral Docker network bridges
│   └── Janitor Engine: Autonomous 15-second process sweeper & container reaper
```

---

## 🔐 Source Code Access & Recruiter Inquiries

> ### ⚠️ Intellectual Property & Academic Review Notice
> The full source codebase, automated mutation algorithms, and proprietary dual-oracle test harnesses are currently maintained in a private repository due to:
> 1. **Academic Peer Review & Capstone Evaluation Integrity**: Preventing live challenge solutions from leaking during institutional evaluation.
> 2. **Intellectual Property Protection**: Safeguarding the custom multi-oracle evaluation engine and mutation algorithms.
>
> ---
>
> ### 💼 For Tech Recruiters, Hiring Managers & Research Evaluators:
> **Full repository access, architecture walk-throughs, and live interactive demo credentials are available upon request.**
>
> If you are considering me for Software Engineering, DevSecOps, or Cybersecurity roles, feel free to reach out directly:
>
> - **👤 Candidate**: **Abhishek**
> - **📧 Email**: [abhisharma.career@gmail.com](mailto:abhisharma.career@gmail.com) *(or your preferred email)*
> - **💼 LinkedIn**: [linkedin.com/in/abhigh15](https://www.linkedin.com/in/abhigh15)
> - **🐙 GitHub**: [@ABHIGH15](https://github.com/ABHIGH15)
>
> *Confidential repository access can be granted within 24 hours via GitHub collaborator invitation.*

---

<div align="center">
  <sub>Developed as a Research & Engineering Capstone Project • Cyber Arena © 2026</sub>
</div>
