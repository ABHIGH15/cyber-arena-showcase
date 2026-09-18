import re

with open('docs/PATENT_AND_SUBMISSION_DOSSIER.md', 'r') as f:
    content = f.read()

# 1. Update "Inventive Novelty"
content = content.replace("## 2. Academic Problem Statement & Core Novelty", "## 2. Academic Problem Statement & Proposed Inventive Concept")
content = re.sub(
    r"(> \*\*A candidate defense is empirically validated.*?\*\*)",
    r"\1\n\n*Note on Inventive Novelty:* While this mechanism is highly useful for deterministic evaluation, \"inventive novelty\" is not asserted merely based on utility. A comprehensive prior-art search is required to establish whether this specific combination (reference-validated adversarial mutation gating combined with static AST correlation) is actually novel and non-obvious.",
    content
)

# 2. RFC 8785 + SHA-256 as an implementation limitation, not principal inventive concept.
# Modify Section 5: Remove box 7 from the ASCII art, move to a new section.
ascii_art_pattern = r"(┌─────────────────────────────────────────────────────────────────────────────┐\n│ 7\. Canonical Deterministic Serialization & Tamper-Evident SHA-256 Digest    │\n│    - Key-order-independent canonical JSON representation                    │\n│    - 64-character SHA-256 audit digest detecting any unauthorized mutation  │\n└─────────────────────────────────────────────────────────────────────────────┘)"
content = re.sub(ascii_art_pattern, "", content)
content = content.replace("## 5. Seven Core Inventive Concepts (Patent Foundations)", "## 5. Six Core Inventive Concepts (Patent Foundations)")

# Remove the downward arrow before box 7
content = content.replace("└─────────────────────────────────────────────────────────────────────────────┘\n                                      │\n                                      ▼\n\n```", "└─────────────────────────────────────────────────────────────────────────────┘\n```\n\n### Implementation & Integrity Limitations\n- **Cryptographic Auditability:** Integrity mechanisms (such as RFC 8785 Canonical JSON serialization and SHA-256 hashing) are treated as implementation-specific integrity limitations securing the evaluation pipeline, rather than the principal inventive concept.")

# 3. Clean up the Independent claims (Claim 1 and Claim 8) and add dependent claim embodiments.
# In Claim 1, step 13, generalize the SHA-256 to a "cryptographic digest".
content = content.replace("computing a deterministic Secure Hash Algorithm (SHA-256) audit digest thereof", "computing a deterministic cryptographic audit digest thereof")
# In Claim 8, generalize SHA-256
content = content.replace("SHA-256 evaluation digests", "cryptographic evaluation digests")

# Claim 9: generalize SHA-256
content = content.replace("deterministic canonical SHA-256 digest", "deterministic cryptographic digest")

# Add new dependent claims for the narrow implementation details
new_dependent_claims = """
### Claim 10: Dependent Claim (Specific Execution Boundaries)
The method of Claim 1, wherein the isolated execution sandbox restricts computing resources according to specifically tailored container limits, comprising enforcing a CPU quota of `--cpus=0.5` and bounding the maximum evaluation duration to exactly 20 minutes to prevent resource exhaustion attacks by submitted patches.

### Claim 11: Dependent Claim (Specific AST Source/Sink Embodiments)
The method of Claim 1, wherein tracing the intra-procedural data flow from the untrusted user input source node comprises tracking specific web application request objects, such as `req.body`, and tracing to specific database execution sink nodes, such as `db.query`.

### Claim 12: Dependent Claim (Specific Database Error Signatures)
The method of Claim 1, wherein the database engine syntax error signature comprises a specific structured query language exception code, such as PostgreSQL error `42601`, indicative of an unhandled syntax violation resulting from adversarial mutation injection.
"""

content = content.replace("### Claim 8: Independent System Claim", new_dependent_claims + "\n### Claim 8: Independent System Claim")

with open('docs/PATENT_AND_SUBMISSION_DOSSIER.md', 'w') as f:
    f.write(content)

