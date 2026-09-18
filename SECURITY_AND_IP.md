# 🔒 Security Invariants, IP & Access Policy

This document outlines the intellectual property guidelines, academic evaluation context, and procedure for requesting confidential source code access.

---

## 1. Why is the Core Engine Kept in a Private Repository?

**Cyber Arena** contains proprietary evaluation algorithms, deterministic mutation operators, and active vulnerability targets developed as part of an advanced cybersecurity capstone research project.

The source repository is currently set to **Private** to ensure:
- **Academic Review Integrity**: Ensuring challenge suites and evaluation harnesses remain confidential during faculty and institutional grading.
- **Evaluation Sandbox Security**: Restricting candidate exploit templates and reference oracles from premature public distribution.
- **Intellectual Property Protection**: Safeguarding the dual-oracle architecture and multi-axis scoring engine.

---

## 2. Requesting Full Source Code Access (For Hiring Managers & Evaluators)

If you are a **recruiter, engineering hiring manager, or academic evaluator** who would like to inspect the complete codebase, review the commit trajectory, or schedule an interactive live walkthrough:

### Fast-Track Access:
1. Send an email to **[amitgupta150306@gmail.com](mailto:amitgupta150306@gmail.com)** with the subject:
   `[Cyber Arena Code Access Request] - <Your Company / Organization Name>`
2. Include your **GitHub username**.
3. You will be added as a **read-only collaborator** to the private development repository (`ABHIGH15/cyber-arena`) within 24 hours.

---

## 3. Supported Demonstration Capabilities

Upon receiving collaborator access or during a live interview walkthrough, you will be able to verify:
- **Full Backend Pipeline**: Express 5.2 API, PostgreSQL connection pooling, and child process orchestration.
- **Docker Sandbox Runner**: Real-time cgroups resource capping (`0.5 CPU`, `512MB RAM`, `pids-limit=100`, `cap-drop=ALL`).
- **Deterministic 6-Axis Mutation Matrix**: 17 versioned test cases spanning SQL injection, boolean differential testing, comment injections, and encoding mutations.
- **Explainability Dashboard & Live Arena**: React 18 frontend with sub-second responsive state management, glassmorphism design tokens, and live second countdown timers.

---

<div align="center">
  <sub>Cyber Arena Research Project • Confidential & Proprietary</sub>
</div>
