# I Built an AI-Powered SEO & Content Machine! (N8n + AI Automation)

**Source:** [I Built an AI-Powered SEO & Content Machine! (N8n + AI Automation)](https://www.youtube.com/watch?v=BAF5GJFuvMU)
**Speaker:** Kasra Dash
**Research scope:** Practical walkthrough using n8n (self-hostable automation platform), Anthropic Claude (Sonnet), the Detailed SEO Chrome extension, and WordPress — covering the full pipeline from competitor URL to published draft

---

## Executive Summary

This tutorial walks through building a fully automated, one-click SEO content pipeline using **n8n** as the orchestration layer. The workflow accepts a blog title and competitor subheadings via a simple form, passes them to an AI model of your choice, and uploads the generated article as a draft post to WordPress — all without manual intervention between steps.

The result is a system that gets you roughly **70% of the way to a publish-ready article** out of the box. The remaining 30% comes from refining your prompt. The underlying workflow is model-agnostic: swap between Claude, OpenAI, Gemini, DeepSeek, or any other supported provider in a single click.

**n8n pricing:** $20/month hosted, or approximately $1–2/month self-hosted. A 14-day free trial requires no card details.

---

## Tools Required

| Tool | Purpose | Cost |
|---|---|---|
| n8n | Workflow automation and orchestration | $20/mo hosted; ~$1–2/mo self-hosted; 14-day free trial |
| Anthropic Claude (Sonnet) | Content generation | Pay-per-use via API |
| Detailed SEO Extension | Extract competitor subheadings from any URL | Free (Chrome extension) |
| WordPress | Content management and publishing destination | Your existing site |

**Model flexibility:** n8n supports Anthropic, OpenAI, Gemini, AWS Bedrock, DeepSeek, and others. The AI node can be swapped at any time without rebuilding the workflow.

---

## Workflow Overview

The pipeline consists of three nodes executed in sequence:

1. **Form Trigger** — Accepts blog title and subheadings as input
2. **AI Agent** — Generates the article using your chosen model and prompt
3. **WordPress Node** — Uploads the output as a draft post

---

## Step-by-Step Build

### Step 1: Create the Form Trigger

In n8n, add a new node and select **Form Trigger**. This creates a simple web form that kicks off the workflow on submission.

**Configure two fields:**

- **Blog Title** (text input, required) — The target article title, e.g. *11 Best SEO Tools in 2025*
- **Subheadings** (text area) — Competitor subheadings pasted in from the Detailed SEO extension

To get competitor subheadings: install the **Detailed SEO Chrome extension**, navigate to a competitor's ranking page, and copy the subheadings it surfaces. Paste them directly into the Subheadings field on the form.

Test the trigger by clicking **Test Setup** and submitting a sample entry. Confirm the form output shows your blog title, subheadings, submission date, and form mode — this confirms the trigger is passing data correctly.

---

### Step 2: Configure the AI Agent Node

Add an **AI Agent** node connected to the form trigger. This node handles content generation.

**Model selection:**
- Connect to your preferred provider (Anthropic, OpenAI, Gemini, DeepSeek, etc.)
- For content generation, Claude Sonnet currently produces strong output — but benchmark against other models periodically, as relative performance shifts frequently

**Prompt configuration:**
Set the source to **Expression** and build a dynamic prompt that pulls in the form fields. A minimal working prompt:

```
I want you to write an article about [Blog Title].

Here are the subheadings to use: [Subheadings]

Feel free to remove any irrelevant subheadings.

Target article length: 1,300 words.

Include a commonly asked questions section at the end.
```

This prompt produces serviceable output — approximately 1,000–1,300 words — and is intentionally simple. See the Prompt Optimisation section below for how to push output quality higher.

Click **Test Setup** and allow 30–60 seconds for the AI node to complete. A tick on the node confirms successful generation. Inspect the output panel to verify the article content before proceeding.

---

### Step 3: Connect the WordPress Node

Add a **WordPress** node and authenticate with your site credentials.

**Configure the node:**
- **Action:** Create Post
- **Title:** Map to the Blog Title field from the form
- **Content:** Map to the AI Agent output
- **Status:** Draft (recommended — review before publishing)

Optional fields available: category, tags, sticky post toggle, comments on/off. For initial testing, title and content are sufficient.

Click **Test Step** to push the article to WordPress. Navigate to your WordPress dashboard and confirm the draft has been created with the correct title and body content.

---

## Running the Full Workflow

Once all three nodes are tested individually, run the end-to-end workflow:

1. Open the form URL
2. Enter a blog title (e.g. *Best WordPress SEO Plugins*)
3. Paste competitor subheadings from the Detailed SEO extension
4. Submit the form
5. Monitor node status in n8n — the workflow completes in roughly 1–2 minutes
6. Review the draft in WordPress

The article publishes as a draft. No content goes live without manual review, which is the appropriate default for AI-generated output.

---

## Prompt Optimisation

The baseline prompt gets you to roughly **6–7 out of 10** quality. Investing 1–2 hours refining the prompt can push output to publication-ready. Areas to address:

**Specificity**
- Define exact word count targets per section
- Specify tone and reading level
- Instruct the model to avoid generic filler phrases

**Structure control**
- Provide a fixed H2/H3 hierarchy if consistency across articles matters
- Instruct the model to flag and skip subheadings that are not relevant to the article topic (it will include everything by default)

**Content depth**
- Include a directive to add concrete examples, tool names, or data points rather than abstract descriptions
- Request a FAQ section with a minimum number of questions
- Specify that introductions should not restate the title

**Brand voice**
- Add 2–3 sentences describing your site's style — formal/informal, first person vs third, target audience
- Include any terminology to use or avoid

The more context the prompt contains, the less editing the draft requires after generation.

---

## Actionable Checklist

### Setup
- [ ] Create an n8n account (hosted or self-hosted) — no card required for 14-day trial
- [ ] Install the Detailed SEO Chrome extension (free)
- [ ] Connect your WordPress site to n8n using the WordPress node credentials
- [ ] Select your preferred AI provider and model in the AI Agent node

### Workflow Build
- [ ] Create a Form Trigger with Blog Title (text, required) and Subheadings (text area) fields
- [ ] Connect the AI Agent node to the form trigger
- [ ] Configure a dynamic prompt using Expression mode, referencing form field values
- [ ] Connect the WordPress node; set action to Create Post with status set to Draft
- [ ] Test each node individually before running the full workflow

### Content Operations
- [ ] Use the Detailed SEO extension to pull subheadings from the top-ranking competitor page for each target keyword
- [ ] Submit the form and allow 1–2 minutes for the workflow to complete
- [ ] Review the WordPress draft — check for irrelevant subheadings, thin sections, and factual accuracy
- [ ] Edit and publish once the draft meets your quality bar

### Prompt Refinement
- [ ] Spend 1–2 hours iterating on the prompt before running the workflow at scale
- [ ] Add word count guidance, tone instructions, and FAQ requirements to the prompt
- [ ] Test prompt changes against varied article types before committing to a production version
- [ ] Reassess model choice every few weeks — performance rankings shift regularly

---

## Honest Caveats

**This is a starting point, not a finished product.** Out of the box, the workflow produces a solid draft — not a publish-ready article. Expect to review and edit every output, particularly around thin sections and generic introductions.

**Prompt quality determines output quality.** The AI node is only as good as the instructions it receives. The baseline prompt in this tutorial is intentionally minimal; production use requires a more detailed prompt tailored to your niche, audience, and content standards.

**Model performance changes frequently.** The best-performing model for content generation shifts week to week. The n8n setup makes it trivial to swap providers — treat model selection as an ongoing test rather than a one-time decision.

**Self-hosting reduces cost significantly.** At $1–2/month for hosting versus $20/month for the managed plan, self-hosting is worth evaluating for anyone running the workflow at volume. The core functionality is identical.
