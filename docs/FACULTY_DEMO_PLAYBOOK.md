# Cyber Arena: Faculty Demonstration Playbook & Evaluation Script

This document provides a step-by-step, 5-minute demonstration script for academic evaluators, faculty reviewers, and technical audiences.

---

## 🎬 5-Minute Live Demonstration Flow

```text
  [1. DEFENDER IDE]             [2. AUTOMATED EVALUATION]        [3. EXPLAINABILITY & PROVENANCE]
Defender Submits Patch  ──►  Isolated Docker Sandbox Exec  ──►  Correlation: CONFIRMED / SECURE
                                          │                                   │
                                          ▼                                   ▼
                             23 Adversarial Mutations              Evidence DAG & Provenance
                             Static Source-to-Sink Track                      │
                             Functional Smoke Invariant                       ▼
                                                                  [4. AUDIT & LIVE ARENA]
                                                                Canonical SHA-256 Certificate
                                                                Live Red-Team Arena Match
```

---

### Step 1: Baseline Vulnerable Submission (SQL Injection)
1. **Navigate to Challenge #1 (SQL Injection)** on the Dashboard.
2. **Submit a Naive/Vulnerable Patch** (using template literals or string concatenation):
   ```javascript
   app.post('/login', (req, res) => {
       const { username, password } = req.body;
       const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
       db.all(query, (err, rows) => { ... });
   });
   ```
3. **Observe Automated Pipeline**:
   - Docker container compiles and isolates on `127.0.0.1::80`.
   - Mutation Engine fires 17 mutating SQLi attacks (encoding, whitespace, comment injections, syntax variations).
   - Dynamic Oracles detect `DB_ERROR` syntax exceptions and unauthorized admin bypasses.
   - Static Analyzer detects `AST_UNSANITIZED_SQL_SINK_FLOW` on Line 4.
4. **Inspect Evaluation Report**:
   - **Verdict**: `CONFIRMED_EXPLOITABLE`.
   - **Resilience Score ($R$)**: $0.0\%$ (All attacks breached).
   - **Evidence Graph**: Demonstrates data-flow propagation from `req.body.username` directly to `db.all()` sink.

---

### Step 2: Robust Defensive Submission (Command Injection)
1. **Navigate to Challenge #2 (Command Injection)** on the Dashboard.
2. **Submit a Parameterized/Separated Defense**:
   ```javascript
   const { execFile } = require('child_process');

   app.post('/ping', (req, res) => {
       const host = req.body?.host || '';
       if (!/^[a-zA-Z0-9.-]+$/.test(host)) {
           return res.status(400).json({ error: 'Invalid host format' });
       }
       execFile('ping', ['-c', '1', host], (err, stdout) => {
           res.send(stdout);
       });
   });
   ```
3. **Observe Automated Pipeline**:
   - Mutation Engine executes **23 mutating CMDi attack candidates** (subshells, pipes, `whoami`, base64 encoding).
   - Dynamic Oracles confirm **23 / 23 attacks safely defended** ($R = 100.0\%$).
   - Functional Smoke Test confirms legitimate ping requests succeed ($F = 100.0\%$).
   - Static Analyzer recognizes `AST_SAFE_EXECFILE_ARRAY_SEPARATION`.
4. **Inspect Evaluation Report**:
   - **Verdict**: `EMPIRICALLY_VERIFIED_SECURE`.
   - **Explainable Evidence Chain**: Shows 23 verified dynamic records + safe AST pattern + functional pass.
   - **Audit Certificate**: Displays the canonical SHA-256 digest (`CA-CERT-X-XXXXXXXX`).

---

### Step 3: Audit Certificate & Tamper Detection
1. **Open the "Tamper-Evident Audit Certificate" tab** on the Evaluation Report.
2. **Click "Copy Digest"** to copy the 64-character SHA-256 fingerprint.
3. **Reviewer Explanation**:
   > *"Cyber Arena generates a canonical, key-order-independent JSON representation of all evaluation parameters and sorted EvidenceRecords. Any retroactive modification to scores, patch code, or logs produces a hash collision mismatch, guaranteeing tamper-evident reproducibility."*

---

### Step 4: Live Red-Team Arena Promotion
1. Since the CMDi patch passed both Security ($R=100\%$) and Functional ($F=100\%$) invariants, it is automatically promoted to the **Live Red-Team Arena**.
2. **Navigate to `/arena`**:
   - An interactive 20-minute adversarial match window is active.
   - Attackers can submit manual payloads in real time.
   - The unified security classifier proxies payloads to the live running container and logs red-team attempts with sub-millisecond telemetry.

---

## 🔬 Key Review 1 / Final Review Talking Points

1. **Why is Cyber Arena novel compared to standard CTFs?**
   - Traditional CTFs only test offensive solvers against static targets. Cyber Arena tests defensive software patches against a multi-axis mutating adversarial attack set and computes dual-dimension scoring ($R$ and $F$).
2. **Why is static analysis strictly advisory?**
   - Static analysis detects syntactic patterns, but dynamic sandbox execution against reference-validated mutations is the empirical ground truth. This enables Cyber Arena to differentiate `THEORETICAL_ONLY` from `CONFIRMED_EXPLOITABLE` and reveal `STATIC_BLINDSPOT`s.
3. **How is DB_ERROR handled?**
   - Zero-Tolerance Invariant: unhandled database/syntax exceptions leak schema structure and are deterministically penalized as security failures.
4. **How is audit reproducibility guaranteed?**
   - Deterministic canonical JSON serialization + SHA-256 cryptographic digest over immutable `EvidenceRecord` arrays.
