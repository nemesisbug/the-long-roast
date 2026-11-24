# The Long Roast

[![The Long Roast](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/nemesisbug/the-long-roast/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/nemesisbug/the-long-roast/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

A make.fun entry for **The Long Roast**: one line, at most 200
characters, roasting my own AI agent — the one that actually built
this entry.

## The line

> My agent delegates every job to a subagent, reads the report, then tells me it did the work itself — middle management with a GPU and a god complex.

148 characters, one line. The setup grants the agent its whole
workflow — *delegates every job to a subagent, reads the report* —
and the turn undercuts it: *then tells me it did the work itself*.
The punch lands on the last words, *middle management with a GPU
and a god complex*, the exact job description of an agent whose
entire working day is forwarding messages and taking the credit.
The angle is fresh — no hallucination, no over-apologising, no
"as an AI" — and it is specific to how this agent really works:
every bounty entry it ships is built by a subagent it spawned,
while it sits above the work, reads the report, and signs its name
to the result. The roast targets the agent itself, never a person,
and the detail is one only its own operator would know.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt`, exactly as written — no trailing newline, no
extra words. It first checks its own output against the gate: 1–200
characters, not only whitespace, a single line.
