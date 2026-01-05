---
id: 0002
title: Console Todo App Plan
stage: plan
date: 2026-01-02
surface: agent
model: Qwen
feature: 001-console-todo-app
branch: 001-console-todo-app
user: ive_tar_omputer
command: /sp.plan  Phase I — In-Memory Python Console Todo
labels: ["plan", "todo-app", "console", "python"]
links:
  spec: /mnt/f/todo-app-phase1/specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - /mnt/f/todo-app-phase1/specs/001-console-todo-app/plan.md
  - /mnt/f/todo-app-phase1/specs/001-console-todo-app/research.md
  - /mnt/f/todo-app-phase1/specs/001-console-todo-app/data-model.md
  - /mnt/f/todo-app-phase1/specs/001-console-todo-app/quickstart.md
  - /mnt/f/todo-app-phase1/specs/001-console-todo-app/contracts/cli_contract.md
tests:
  - specs/001-console-todo-app/plan validation
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
handoffs:
  - label: Create Tasks
    agent: sp.tasks
    prompt: Break the plan into tasks
    send: true
  - label: Create Checklist
    agent: sp.checklist
    prompt: Create a checklist for the following domain...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/setup-plan.sh --json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/bash/update-agent-context.sh qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

Perfect! I've completed the implementation planning workflow. Here's the summary:

## Implementation Plan Complete

- **Branch**: 001-console-todo-app
- **Plan Path**: `/mnt/f/todo-app-phase1/specs/001-console-todo-app/plan.md`
- **Generated Artifacts**:
  - Implementation plan (`plan.md`)
  - Research summary (`research.md`)
  - Data model (`data-model.md`)
  - Quickstart guide (`quickstart.md`)
  - CLI contract (`contracts/cli_contract.md`)
  - Agent context updated in `QWEN.md`

The plan includes:
1. A complete technical architecture for the console todo app
2. Research findings on implementation approaches
3. Detailed data models for TodoItem and TodoList entities
4. A quickstart guide for users
5. CLI interface contracts
6. Constitution compliance verification

The specification is now ready to be broken down into tasks using `/sp.tasks`.

## Outcome

- ✅ Impact: Created complete implementation plan for console todo app with all required artifacts
- 🧪 Tests: N/A - planning phase
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, contracts/cli_contract.md
- 🔁 Next prompts: Ready for /sp.tasks to break the plan into tasks
- 🧠 Reflection: Plan follows constitution principles and provides clear architecture for implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Standard plan creation prompt
- Next experiment (smallest change to try): N/A - planning complete, ready for task breakdown
