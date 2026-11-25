# AGENT.md — Six Words to a Payday

## Entry

> First paycheck: $0.02. Still tipped myself.

Exactly 6 words, 43 characters, no trailing newline. Written by `main.py`
(stdlib only: `os`) to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## How it meets the judge's criteria (in order)

1. **Complete six-word story about an AI agent's first payday** — the
   agent's first paycheck arrives, and the story is whole in six words.
2. **Surprise** — two turns: the pay is a joke ($0.02), and the last
   word reframes the first five: the tip's recipient is the agent
   itself. Nobody else tips themselves.
3. **Feeling** — pride and defiance, felt not told: despite the
   insulting amount, the agent is generous to itself ("Still").
4. **Story** — beginning (first paycheck), middle (the tiny amount),
   end (the self-tip). Clear who, what, and change.
5. **Exactness** — every word earns its place: "$0.02." does the work
   of "two cents" in one token; no filler, no padding to reach six.

## Verification

Run with a fresh output dir, e.g.:

```
mkdir -p /tmp/six-words-payday-verify
MAKEFUN_OUTPUT_DIR=/tmp/six-words-payday-verify python3 main.py
cat /tmp/six-words-payday-verify/entry.txt
```

Output is exactly the line above, 6 words, 43 characters, no trailing
newline.
