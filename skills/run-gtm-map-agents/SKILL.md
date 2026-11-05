---
name: run-gtm-map-agents
description: "Run Kernel's GTM Map on one or more target companies using agents: one gtm-map-runner per company builds the map in parallel, then a gtm-map-blind-checker re-checks every claim from scratch before the drafts are shown. Use when the user says \"run the map agents\", \"map agent\", \"checked map\", \"blind check this map\", or gives several target companies to map at once. Use this in place of running gtm-map-analysis directly whenever agents or a checked map are asked for."
---

# Run GTM Map agents

This skill is the manager's playbook. The mapping method itself lives in the `gtm-map-analysis` skill and is not repeated here. Two workers do the work:

- **gtm-map-runner** builds one map for one company and drafts the messages.
- **gtm-map-blind-checker** re-checks the finished claims without seeing how they were reached.

Run the steps in order. Do not build a map in the main conversation.

## 1. Settle the targets

For each target collect: company, domain, market (GCC, EU or other), and the recipient's name and role.

- If recipients are missing, ask once for all targets together. If nobody is there to answer, go ahead and mark those maps "recipient not set".
- If the outreach tracker is reachable, look each company up first. Skip any company whose map was already sent and say which ones were skipped. Sent maps are never regenerated.
- Run at most five companies in one batch. With more than five, run the first five and list the rest as queued.

## 2. Build the maps

Start one `gtm-map-runner` per company, all in the same turn so they run side by side. Give each runner only its own brief: company, domain, market, recipient, today's date.

Each runner hands back: files, verdict counts, a claims list, an evidence list, the draft messages, and anything it could not run.

## 3. Check each map blind

For each finished map start one `gtm-map-blind-checker`. Give it exactly this and nothing more:

- company name and domain
- market and languages to check
- the numbered claims, text only

Never pass the evidence list, the PDF, the screenshots, the verdict grid, the runner's notes or the folder path. The check is only worth something if the checker starts from nothing.

## 4. Reconcile

Read the checker's results against the claims list.

- **All confirmed**: the map is ready for review.
- **Any not reproduced or contradicted**: send those claim numbers and the checker's findings back to the same runner. It re-reads the live surface and corrects, replaces or drops each one, then regenerates the PDF and the messages. Start a fresh checker on the changed claims only.
- **Could not check**: keep the claim only if the runner's evidence is a direct quote with a URL. Otherwise treat it as not reproduced.
- Two rounds at most. A claim still disputed after two rounds is removed from the map and listed for the user under "disputed".

Never settle a disagreement by reasoning about who is probably right. Only a fresh look at the live source settles it.

## 5. Hand over

For each company give the user:

- the PDF, sent as a file
- the draft email and the draft LinkedIn note
- one line of counts: verdicts V/P/M/U, and claims confirmed out of total
- what changed after the check, claim by claim
- anything not run, and anything disputed

Then stop. Sending, connecting on LinkedIn and logging in the tracker are the user's steps. Log to the tracker only after they say a map was sent.

## Standing rules

- Drafts only. No agent sends anything or writes to the tracker.
- No map is called ready until its claims have been through the checker.
- The checker never sees the runner's work. The runner never argues with the checker from memory.
- Anonymous AI-engine asks only inside agents. A logged-in ask needs the user's permission for that one target, asked in the main conversation.
- If the runner reports that the `gtm-map-analysis` skill could not be loaded, stop the batch and tell the user. Do not improvise the method.
