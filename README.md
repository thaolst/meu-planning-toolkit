# MEU Planning Toolkit

Backward planning from Monthly Engaging User (MEU) targets to campaign calendar - with prompts, lifecycle treatment framework, and MEU calculator.

Built from real fintech growth campaigns in SEA.

## Why backward planning

Most campaign planning starts from a brief or a budget. This repo starts from the MEU gap:

> "Mình can bao nhieu MEU nua de hit target? Campaign nao se dong gop nhieu nhat?"

That question drives everything else - event mix, lifecycle treatment, channel selection, budget split.

## What's inside

| Folder | What it does |
|---|---|
| 01-framework | MEU backward planning logic + event tiering (Mega/Big/Medium/Small) |
| 02-prompts | 4 prompt workstreams, each with bootstrap + resumption files |
| 03-tools | meu_calculator.py - input target, output campaign ladder |
| 04-templates | Annual calendar template, blank and reusable |

## How to use

**Step 1 - Gap analysis first**
Open `02-prompts/01-meu-gap-analysis/bootstrap.md`. Input your current MEU base and target. The prompt outputs your gap by lifecycle stage.

**Step 2 - Pick your event mix**
Use `02-prompts/02-event-mix-planner/bootstrap.md` to translate the gap into a campaign calendar (seasonal spikes + repeated mechanics + always-on treatment).

**Step 3 - Lifecycle treatment**
`02-prompts/03-lifecycle-treatment/bootstrap.md` assigns campaign mechanics to each lifecycle stage: Acquisition, Activation, Retention, Resurrection.

**Step 4 - Run the calculator**
`03-tools/meu_calculator.py` - input your numbers, get a prioritized campaign ladder with estimated MEU contribution per activity.

## Stack

- Prompts: Claude (tested on Sonnet 4.6)
- Calculator: Python 3.10+
- No external dependencies for prompts

## Who this is for

Growth marketers in fintech, super-apps, or any platform where MEU/MAU is the north star metric. Works best if you have historical campaign data to calibrate the calculator.

---

[LinkedIn](https://linkedin.com/in/thaolst) - [GitHub](https://github.com/thaolst) - [Substack](https://thaolst.substack.com)
