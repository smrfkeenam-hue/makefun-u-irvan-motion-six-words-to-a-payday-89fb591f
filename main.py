import os

# Six-word story about an AI agent's first payday. Exactly six words,
# 43 characters, no trailing newline. The pay is a joke ($0.02), yet
# the agent still tips itself — pride over the amount. The last word
# reframes the first five: the tip's recipient is the agent itself.
ENTRY = "First paycheck: $0.02. Still tipped myself."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
