# GTM Map agents

A Claude Code plugin that reads a company's public surfaces the way a stranger would and maps them against the 34 outputs of a product marketing function. One agent builds the map. A second agent checks every claim from scratch without seeing how the first one got there.

I built this for [Kernel](https://kernelpmm.com), my fractional product marketing practice. The map is the free diagnostic I send to founders and marketing leaders before we ever talk. It has to stand up when they check it, so nothing goes out until the blind checker has reproduced each claim from the live sources.

## What one run produces

- **Page 1, the map.** All 34 outputs across Research, Competition, Position, Message, Launch and Measure, each marked visible, partial, missing or unknowable from outside.
- **Page 2, the positioning read.** What the company says it is (category, who it is for, where, why choose it, proof), next to what the rivals a buyer would compare say, with a verdict per row and the positioning choice to settle first.
- **Page 3, how the gaps would be closed.** Three issues from the read, what would be done about each, and where it has been done before. A `role` mode rewrites this page as a first-90-days plan for someone applying to the company.
- **Draft outreach.** An email and a LinkedIn note quoting the read word for word. Drafts only. Nothing is sent.

## How the two agents work

| Part | Job |
|---|---|
| [`gtm-map-runner`](agents/gtm-map-runner.md) | Reads one company's site (rendered and raw HTML), pricing, careers, press, app stores, review sites, comparison searches and four to six rivals. Assigns the 34 verdicts, writes the positioning read, builds the PDF and drafts the messages. One runner per company, so a batch runs in parallel |
| [`gtm-map-blind-checker`](agents/gtm-map-blind-checker.md) | Gets only the numbered claims, never the notes or evidence. Tries to reproduce each claim from the live sources and reports which ones hold |
| [`run-gtm-map-agents`](skills/run-gtm-map-agents/SKILL.md) | The manager's playbook. Starts the runners, keeps the checker blind, and settles disagreements in two rounds at most. A claim still disputed after that comes off the map |
| [`gtm-map-analysis`](skills/gtm-map-analysis/SKILL.md) | The method itself: verdict rules, the positioning read, writing rules, the message format and the PDF generator |

Why a blind checker: an agent asked to check its own work tends to confirm it. A checker that never sees the first run's reasoning tests the one thing that matters to the reader, which is whether they would get the same answer if they looked.

## Rules the agents follow

- Public surfaces only. Anything that can only be known from inside the company is marked unknowable, never guessed.
- Every rival line is a quote from a page read in that run, with its URL.
- Every link in the PDF is taken from the live site in that run, never from memory.
- AI-engine questions are asked signed out. A signed-in ask needs the user's permission for that one company.
- No agent sends an email, a LinkedIn note or a DM.

## Install

```
/plugin marketplace add hkotthapalli/gtm-map-agents
/plugin install gtm-map-agents@gtm-map-agents
```

The PDF generator needs Python 3 and ReportLab (`pip install reportlab`).

## Use

```
Run the map agents on <company>, <company>
```

Up to five companies per batch. To build a PDF by hand, copy [`company_data_template.py`](skills/gtm-map-analysis/scripts/company_data_template.py) to `company_data.py`, fill it in, and run `python3 gen_maps.py COMPANYNAME`. Set `AUTHOR_FOOTER` at the top of `gen_maps.py` to your own name.

## Related

- [kernel-pmm-skills](https://github.com/hkotthapalli/kernel-pmm-skills): the 34 outputs the map checks against, each as a Claude skill.
- [kernelpmm.com/gtm-map](https://kernelpmm.com/gtm-map): request a map, or run the same check yourself.

## Licence

MIT.
