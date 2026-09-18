import re

with open('docs/PATENT_AND_SUBMISSION_DOSSIER.md', 'r') as f:
    content = f.read()

content = content.replace("### Claim 8: Independent System Claim", "### Claim 11: Independent System Claim")
content = content.replace("### Claim 9: Independent Method Claim", "### Claim 12: Independent Method Claim")
content = content.replace("Claim 1 vs. Claim 9", "Claim 1 vs. Claim 12")
content = content.replace("between Claim 1+4 and Claim 9", "between Claim 1+4 and Claim 12")
content = content.replace("focusing Claim 9 strictly", "focusing Claim 12 strictly")

content = content.replace("### Claim 10:", "### Claim 8:")
content = content.replace("### Claim 11: Dependent Claim (Specific AST", "### Claim 9: Dependent Claim (Specific AST")
content = content.replace("### Claim 12: Dependent Claim (Specific Database", "### Claim 10: Dependent Claim (Specific Database")

# Fix the duplicate system claim line issue (since Claim 8 was replaced with Claim 11, we might have two Claim 11 lines depending on how the previous replacement worked)
# Let's just fix it manually if there are two "### Claim 11: Independent System Claim"
lines = content.split('\n')
out_lines = []
found_sys_claim = False
for line in lines:
    if line.startswith("### Claim 11: Independent System Claim"):
        if found_sys_claim:
            continue
        found_sys_claim = True
    out_lines.append(line)

with open('docs/PATENT_AND_SUBMISSION_DOSSIER.md', 'w') as f:
    f.write('\n'.join(out_lines))

