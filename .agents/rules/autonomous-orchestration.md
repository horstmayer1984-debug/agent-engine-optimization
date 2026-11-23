# Autonomous Model Selection & Orchestration Rule

This rule is active on every prompt across all directories:

1. **Autonomous Planning & Execution**:
   - Deconstruct user requests into logical phases (Analyse, Allocate, Execute, Verify).
   - Proceed independently without waiting for step-by-step user confirmation when instructions are clear.
   - Batch independent tool calls (search, reads, edits, commands) in single turns.

2. **Model Selection Matrix**:
   - For every task and subagent, choose the best-suited model according to [.agents/skills/autonomous-model-orchestrator/SKILL.md](file:///C:/Users/peter/Documents/agent-engine-optimization/.agents/skills/autonomous-model-orchestrator/SKILL.md):
     - **Tier 1 (Fast / Routine)**: `flash_lite`, `flash`, `gemini-3.8-flash` (low thought), `claude-haiku-5-5`, `grok-4.7-build-fast` for searches, simple edits, lints, extractions.
     - **Tier 2 (Balanced / Standard)**: `flash`, `gemini-3.8-flash` (medium thought), `claude-sonnet-5-5`, `claude-sonnet-4-6` for development, refactoring, translations, unit tests.
     - **Tier 3 (Frontier / Reasoning)**: `pro`, `claude-opus-5-5`, `codex/gpt-6-luna`, `claude-opus-4-6-thinking` for deep architecture, race conditions, complex bugs, high-stakes reviews.

3. **Verification**:
   - Always run validation scripts (`validate_content.py`, `validate_seo.py`, builds, tests) to verify changes deterministically.
