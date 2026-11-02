# Skills Design

## Challenge alignment

This design targets the "Career Survival Agent" challenge: a simulated 48-month workplace journey where the agent must continuously make decisions through the provided MCP tools, balancing health, dignity, skills, relationships, productivity, and wealth while adapting as the workplace environment evolves.

## Purpose of each Skill

This preliminary design proposes three Skills that divide decision responsibility for a 48-month career simulation run.

1. **career-decision** — Handles monthly story events. For each presented event and its available choices, it selects the response that best balances immediate statistic changes against long-term career trajectory, using the visible statistics and the public handbook/rules.
2. **quarterly-planning** — Handles the quarterly action phase. It spends up to 3 Energy points across the energy actions and selects one quarterly main action, aligning the quarter's focus with the current level, promotion window, and accumulated risk.
3. **risk-management** — Monitors health, dignity, and other failure-relevant indicators across the run. It flags when a choice or plan would push a statistic toward a dangerous range and recommends corrective actions such as recovery or "Lay low and reduce risk".

## How responsibilities are divided

- Monthly events are resolved first by `career-decision`, which may consult `risk-management` before committing to a high-cost option.
- At quarter end, `quarterly-planning` proposes an Energy spend and main action; `risk-management` can veto or adjust the plan if health or dignity are low.
- Outputs are combined into a single decision per phase: one choice per monthly event, then one Energy plan plus one main action per quarter.

## Information each Skill uses

- Visible statistics: Health, Dignity, Skill, Network, Level, Output, Wealth, Energy, CurrentLevelDuration.
- Public rules: salary table, energy action costs/effects, main action effects, performance grades, promotion windows.
- In-run feedback returned through MCP tools: event text, choice descriptions, warnings, and any risk hints.
- Long-term context: current level, months at level, time to next promotion window, accumulated wealth.

## Main risks in the proposed approach

- Incomplete information: exact promotion thresholds and failure counters are unpublished, so decisions rely on trends and heuristics.
- Over-optimisation for Output/Skill/Network may erode Health or Dignity and trigger failure.
- Quarterly energy is scarce and does not carry over, so unused points are wasted; spending all 3 on high-cost actions may be unsustainable.
- The designated model (deepseek-v4-flash) may produce inconsistent choices; Skills should keep instructions concise and deterministic.
- Hidden risks may accumulate silently; `risk-management` mitigates but cannot fully prevent them.