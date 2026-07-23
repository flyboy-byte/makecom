> **Tier:** Low-level (technical spine) · **Audience:** implementer/engineer building
> and operating the actual Make.com pipelines · **Use when:** designing a scenario,
> writing an SOW, or setting SLA terms. This is the original source document the rest
> of the packet in `docs/` is built from — see
> [`docs/documentation-guide.md`](./docs/documentation-guide.md) for how it fits.

# **2026 Production Systems Engineering & Enterprise Operations Manual**

**Document ID:** EOPS-2026-HARDENED  
**Version:** 2.4.0  
**Classification:** Internal Operating Blueprint & Technical SOP  
**Applicability:** Systems Architects, Integration Engineers, Compliance Officers

## **Executive Summary: The Workflow Repair Framework**

This document supersedes all previous agency model documentation. It transitions the organizational framework away from speculative "autonomous digital employee" narratives and establishes the technical specifications for a **Workflow Repair Agency**. Grounded in empirical data, this framework acknowledges that while 76% of organizations engage in surface-level AI tool experimentation, deep operational pipeline integration remains constrained to roughly **14%**. The primary blockers are data quality failures, unmapped human heuristics, and unhardened integration architecture.  
The core mandate of this agency is to engineer deterministic, fault-tolerant pipelines connecting fragmented legacy systems (emails, PDFs, invoices, CRM fields, and trade dispatch software) without relying on the assumption of model infallibility. Every system deployed under this manual must enforce structural validation, idempotent execution, multi-layered data governance, and human-in-the-loop review gates.

## **Phase 1: Intake, Video Capture, & Technical Scoping**

Project failure is almost always an upstream discovery failure. To eliminate scope creep and unbillable edge-case engineering, clients must be qualified through a rigid asynchronous intake process.

### **1.1 The Client Intake Questionnaire**

Prior to scheduling a synchronous technical audit, the prospect must submit written documentation answering the following operational questions:

> 1. What specific app, inbox, or trigger event initiates this workflow?  
> 2. What are the exact downstream systems (CRM, ERP, Accounting Software) that must receive this data?  
> 3. How many times per week does this exact sequence execute?  
> 4. What are the top 3 reasons a human currently has to stop, flag, or manually fix an entry in this process?  
> 5. If this system goes completely offline for 24 hours, what is the immediate financial or operational impact on the business?

### **1.2 The Asynchronous Video Capture Mandate**

The client must provide a minimum of **5 distinct, consecutive recordings** (e.g., via Loom) of staff manually executing the target workflow. The recordings must capture:

* The exact data origin (e.g., opening an unformatted email inquiry).  
* All intermediate processing steps (e.g., cross-referencing names or parts numbers across tabs).  
* The precise manual decision logic used to resolve irregular or incomplete payloads.

### **1.3 The 3-Trait Qualification Test**

Every captured process must satisfy the 3-Trait Matrix before a Statement of Work (SOW) can be generated:

                  \[Inbound Workflow Opportunity\]  
                                │  
                                ▼  
               \[3-TRAIT QUALIFICATION CHECKPLATE\]  
                                │  
         ┌──────────────────────┼──────────────────────┐  
         ▼                      ▼                      ▼  
  \[Trait 1: Volume\]     \[Trait 2: Input\]       \[Trait 3: Output\]  
  Is execution frequency  Does the input text/   Can the data resolve  
  ≥ 10 instances/week?   image require parsing?  to a strict schema?  
         │                      │                      │  
         └──────────────────────┼──────────────────────┘  
                                │  
                     (All Traits Satisfied)  
                                │  
                                ▼  
                 \[Proceed to Technical Audit\]

* **Trait 1: Volume Threshold:** The workflow must execute $\\ge 10$ times per week. Lower volumes do not justify agency development friction and limit the data loop necessary to isolate runtime exceptions.  
* **Trait 2: Unstructured Input Payload:** The workflow must ingest data requiring contextual extraction (e.g., body text of an auto-repair quote request, a scanned supplier invoice PDF, or a raw missed-call transcription).  
* **Trait 3: Structured Destination Schema:** The extracted data must map to a rigid, machine-readable destination schema (JSON) that can be ingested natively by downstream software APIs.

### **1.4 Concrete Vertical Mapping**

Engineers must prioritize concrete, repeatable trade and local operations workflows over abstract enterprise management structures:

| Target High-Volume Workflows (Concrete & Mapped) | High-Risk Workflows (Abstract / Unqualified) |
| :---- | :---- |
| **Inbound Quote Intake (HVAC/Automotive):** Processing messy email quote requests and mapping them into dispatch software. | **Fully Autonomous Customer Service Bots:** Open-ended, unmonitored customer interaction loops with no human guardrails. |
| **Invoice Extraction & Parts Tracking:** Parsing supplier PDFs to update inventory quantities and unit costs. | **Replacing a Unmapped Human Process:** Attempting to automate an operational layer before it has been structurally diagrammed. |
| **Missed-Call Lead Resuscitation:** Triggering instant text-based follow-ups to unreturned customer phone calls. | **Vague "AI Executive Assistant" Promotes:** Open-ended, non-linear tasks lacking strict schema inputs and outputs. |

## **Phase 2: Defensive Engineering & Idempotence Blueprint**

Make.com operations are governed by a **Credit-Based Billing System** where native platform AI features scale dynamically based on token volume, files, or processing tasks. Unoptimized loops or unguarded webhooks will drain a client's credit allocation. Scenarios must be constructed using a decoupled, gated topology designed to mitigate rate limits ($60/\\text{min}$ Core, $120/\\text{min}$ Pro, $240/\\text{min}$ Teams, $1,000/\\text{min}$ Enterprise) and prevent duplicate data entry.

### **2.1 Hardened Multi-Stage Infrastructure Architecture**

\[Inbound Webhook Trigger\]  
          │  
          ▼  
\[Webhook Signature Verification\] ──(Invalid Signature)──► \[Instant Drop (401 Unauthorized)\]  
          │  
  (Valid Signature)  
          ▼  
\[Idempotency Key Check\] ──────────(Key Already Exists)─► \[Acknowledge 200 OK & Halt Loop\]  
          │  
  (Unique Payload Key)  
          ▼  
\[Deterministic Regex Filter\] ─────(Fails Validation)───► \[Instant Scenario Halt (0-1 Credit)\]  
          │  
  (Passes Validation)  
          ▼  
\[HTTP Module: Raw API Call\] ────► \[Bypasses Native Make AI Markup / Direct Token Control\]  
          │  
          ▼  
\[JSON Parse & Schema Enforcement\] ─(Invalid JSON)──────► \[Error Log Routing & Slack Alert\]  
          │  
    (Valid JSON)  
          ▼  
\[Human-in-the-Loop Gate\] ───────► \[Generates Draft State / Pushes UI Approval Webhook\]  
          │  
  (Human Action: Approve)  
          ▼  
\[Downstream System Write (CRM/ERP)\]

### **2.2 Advanced Technical Integration Standards**

#### **Webhook Signature Verification**

To prevent malicious payload injections, all instant webhook entry nodes must validate cryptographic signatures. If the sending platform supports it, verify the X-Hub-Signature or authorization header using a native Make data store or a deterministic script step. Drop unsigned or unverified requests immediately with an HTTP 401 Unauthorized status code.

#### **Idempotency Key Enforcement**

To prevent duplicate webhook firings (caused by network retries or upstream server glitches) from creating duplicated records or multiple customer texts, implement an **Idempotency Gate**:

> 1. Upon webhook ingestion, compute a unique hash string of the payload (e.g., combining the upstream Event ID, timestamps, or phone number strings).  
> 2. Query an internal **Data Store module** or lightweight cache database using that hash as the key.  
> 3. If the key already exists in the cache, terminate the scenario execution instantly with an HTTP 200 OK response. Do not pass the data downstream; do not execute any AI modules.  
> 4. If the key is unique, write it to the cache with a 24-hour expiration window and proceed with the workflow.

#### **Token Isolation via HTTP Modules**

Avoid utilizing built-in Make.com AI connectors for high-volume execution pathways. Instead, construct standard API payloads using the native **HTTP App** to interface directly with language model endpoints (e.g., Anthropic, OpenAI). This ensures the execution step consumes exactly 1 Make credit, bypasses platform token pricing markups, and provides precise rate-limit visibility inside your dedicated provider developer accounts.

#### **Human-in-the-Loop (HITL) Protocol**

Automations are strictly barred from updating public records or messaging end customers without an intervening review step. The scenario must only populate a **Draft State**, write a **Pending Review** flag inside the trade software, or push an interactive Slack/Teams approval button. The client's operational staff remains the final authority for execution, completely isolating the agency from liability caused by data errors or hallucinations.

## **Phase 3: Staging, Failure Mode Testing, & Deployment**

Deploying code modifications directly into a live production scenario processing active operations introduces severe data corruption risks. A disciplined deployment pipeline must be strictly followed.

### **3.1 Environment Isolation & Secret Storage**

Engineers must maintain separate **Sandbox** and **Production** folders inside Make.com.

* All API keys, connection secrets, and webhook tokens must be stored using Make's native encrypted connection profiles or an external, secure vault.  
* Never hardcode sensitive environment strings, authorization headers, or private keys directly into individual module input fields.

### **3.2 Defined Acceptance & Testing Criteria**

A scenario cannot be migrated to production based on a basic error-free run. It must pass an intentional **Failure Mode Testing Suite**:  
                       \[TESTING & DEPLOYMENT STACK\]  
                                     │  
         ┌───────────────────────────┴───────────────────────────┐  
         ▼                                                       ▼  
\[A. Valid Payload Stress Test\]                        \[B. Intentional Failure Testing\]  
Run 50 unique, valid payloads.                       Inject 10 malformed/corrupted payloads.  
Target: 100% Success, 0 Flags.                       Target: 100% Caught by Filters, 0 AI Credits Burned.  
         │                                                       │  
         └───────────────────────────┬───────────────────────────┘  
                                     │  
                        (Both Test Suites Passed)  
                                     │  
                                     ▼  
                      \[Blueprint JSON Export/Import\]  
                                     │  
                                     ▼  
                     \[Production Live Webhook Swap\]

* **Test Suite A: The 50-Run Stress Test:** Inject 50 distinct, valid mock payloads representing varied data formats into the Sandbox scenario. The system must process 100% of these inputs to completion with **0 unexpected error flags**.  
* **Test Suite B: Intentional Failure Isolation:** Inject 10 intentionally corrupted, partial, or malformed payloads (e.g., missing phone numbers, blank invoice files, or spam strings) into the Sandbox scenario. **Criteria for Success:** 100% of these payloads must be successfully identified and halted by the deterministic logic filters or JSON schema validation blocks *before* triggering any external LLM or AI modules, verifying that zero runaway credits are consumed by garbage data.

### **3.3 Deployment Execution Sequence**

> 1. Export the confirmed scenario architecture from the Sandbox environment as a raw JSON blueprint file.  
> 2. Import the blueprint into the Live Production folder.  
> 3. Manually map the connection variables from test app endpoints to live production CRM/ERP API tokens.  
> 4. Point the source application's live webhook URL to the newly instantiated production scenario address.  
> 5. Retain the old production scenario version, renamed with a \[DEPRECATED\_YYYY\_MM\_DD\] prefix, for exactly 14 calendar days as an immediate rollback fallback option.

## **Phase 4: Hardened Data Governance & Compliance**

Handling business communications, customer invoices, and trade dispatch records involves interacting with sensitive data. Engineers must treat data transit paths with extreme caution.

### **4.1 Multi-Layered Retention Mapping**

The agency must explicitly distinguish between **Data Training Restrictions** and **Data Retention Lifespans**. Simply turning on a single platform configuration flag does not establish an end-to-end data governance pipeline.

                  \[DATA PAYLOAD TRANSIT PATHWAY\]  
                                │  
                                ▼  
         \[Make.com Webhook Queue\] ──► Cached for transit; cleared after run.  
                                │  
                                ▼  
         \[Make Scenario Runtime\]  ──► Data Confidentiality \= TRUE (Scrubbed).  
                                │  
                                ▼  
         \[Model API Provider\]     ──► No Training (Default); 30-Day Retention.  
                                │     \*ZDR must be negotiated for full wipe.\*

* **Make.com Confidentiality & Queues:** Activating the **"Data is confidential"** configuration flag to **TRUE** within the settings panel of a scenario scrubs the request strings and variable payloads from Make's visual execution logs *after the run completes*. However, engineers must recognize that incoming data is still temporarily held in Make’s underlying webhook queue during processing transit, and standard webhook retention rules continue to apply to meta-logs.  
* **Model API Retention vs. Training:** When connecting via the custom HTTP App to OpenAI or Anthropic developer APIs, commercial terms ensure that data inputs and outputs are **not used for model training by default**. However, standard data retention rules dictate that these providers cache your payloads on their servers for up to **30 days** to monitor for platform abuse before deletion.  
* **Zero Data Retention (ZDR):** If a client handles highly sensitive data, engineers must formally request Zero Data Retention (ZDR) configuration lines within their enterprise API portal or utilize specialized compliance endpoints to permanently prevent provider caching.

### **4.2 Master Services Agreement (MSA) Legal Guardrails**

To shield the agency from third-party liabilities, the standard client contract must contain these explicit clauses:

* **Hallucination & Execution Waiver:** The Client acknowledges that machine learning systems interpret unstructured natural language probabilistically. Because the Agency engineers mandatory Human-in-the-Loop review gates into all customer-facing workflows, the Client assumes full operational and legal liability for verifying the correctness of any data passed to end-users or financial accounting ledgers.  
* **Upstream System Drift Exemption:** The Agency provides no warranty and assumes zero liability for integration breaks, data delivery failures, or system delays caused by sudden API deprecations, unannounced endpoint modifications, or downtime experienced by third-party software platforms (e.g., ServiceTitan, QuickBooks Online, HubSpot).

## **Phase 5: Productized Retainers & SOW Framework**

An automation agency cannot maintain financial viability on flat-fee project delivery alone. Systems drift, app updates, and edge-case operational changes will consistently break static configurations. Long-term margins are driven entirely by managing the ongoing workflow infrastructure.

### **5.1 Productized Maintenance Retainer Menu**

Every project delivery requires a mandatory, tiered **Operational SLA Retainer** scaled to the business structure:

                  ┌──────────────────────────────┐  
                  │ SELECT MAINTENANCE SLA LEVEL │  
                  └──────────────┬───────────────┘  
          ┌──────────────────────┼──────────────────────┐  
          ▼                      ▼                      ▼  
    \[ESSENTIALS\]             \[GROWTH\]              \[ENTERPRISE\]  
   \- 12-Hr Patch Window     \- 4-Hr Patch Window    \- 2-Hr Patch Window  
   \- Monthly Audits         \- Weekly Audits        \- Bi-Weekly Audits  
   \- Up to 10k Credits      \- Up to 50k Credits    \- Custom Credit Pool  
   \- $499 / Month           \- $1,250 / Month       \- $2,950+ / Month

#### **Tier 1: Essentials SLA — $499 / Month**

* **API Drift Remediation:** Verification and patching of broken endpoints within a 12-business-hour response window.  
* **Exception Log Auditing:** Monthly review of scenario failure histories to optimize regex patterns and logic gates.  
* **Credit Pool Allocation:** Includes management of up to 10,000 Make.com scenario credits per month.

#### **Tier 2: Growth SLA — $1,250 / Month**

* **API Drift Remediation:** Priority patching of broken integrations within a strict 4-business-hour response window.  
* **Exception Log Auditing:** Weekly deep-dive log audits to identify user input variances and iteratively update prompt configurations.  
* **Credit Pool Allocation:** Includes management and monitoring of up to 50,000 Make.com scenario credits per month, with proactive loop optimization (e.g., row lookups converted to batch array lookups to maximize credit margins).

#### **Tier 3: Enterprise Operations SLA — $2,950+ / Month**

* **API Drift Remediation:** Mission-critical response window providing a dedicated engineer patch within 2 business hours.  
* **Exception Log Auditing:** Bi-weekly operational reviews, schema restructuring, and continuous performance optimization updates.  
* **Credit Pool Allocation:** Custom dedicated credit boundaries with multi-tenant workspace isolation.

## **Phase 6: Statement of Work (SOW) Blueprint**

Below is the mandatory one-page framework required for drafting all project scopes:

### **STATEMENT OF WORK: WORKFLOW INTEGRATION & REPAIR**

**1\. Project Overview & Objective**  
This project implements a deterministic, fault-tolerant automation pipeline connecting \[Client Trigger App\] to \[Client Destination CRM/ERP\]. The explicit business objective is to eliminate manual data entry errors and reduce lead response times to under 180 seconds.  
**2\. Core Technical Deliverables**

* **Phase 1 (Discovery):** Mandated asynchronous video capture audit of current manual heuristics.  
* **Phase 2 (Sandbox Build):** Construction of gated scenario architecture featuring cryptographic webhook verification, an idempotency key check module, and custom HTTP API model connections.  
* **Phase 3 (Testing & Governance):** Execution of a 50-run stress-test suite alongside a 10-run failure mode isolation check. Activation of Make-layer data confidentiality protocols.  
* **Phase 4 (Deployment):** Direct webhook migration with an active 14-day deprecated fallback scenario.

**3\. Human-in-the-Loop Guardrails**  
In accordance with standard engineering rules, this automation will not write live data directly to outward-facing fields. It will output entries strictly as a \[Draft/Pending Review State\] inside the target application, requiring manual approval by a staff member before final execution.  
**4\. Financial Investment & Operational Mandate**

* **One-Time Implementation & Testing Fee:** $\[XXXX.XX\]  
* **Mandatory Ongoing Infrastructure & SLA Retainer:** $\[XXXX.XX\] / month (Billed on Tier \[X\] SLA parameters starting immediately upon production deployment).

## **Phase 7: Core Implementation Code & Logic Checkplates**

### **7.1 Technical Walkthrough 1: Inbound Lead Intake & CRM Pipeline**

* **Objective:** Parse parameters from unformatted trade service inquiries, evaluate booking intent, and populate a structured CRM record.

1\. Trigger: \[Custom Webhook Ingestion Node\] (Monitors sales or dispatch inbox).  
2\. Action: \[Crypto Tool\] (Validates webhook cryptographic signature signature).  
3\. Action: \[Data Store \- Get Record\] (Queries calculated hash of payload to check for duplicate entry).  
4\. Filter: \[Idempotency Gate Check\]  
   ├── If Key Found in Cache: Stop scenario execution immediately (Acknowledge 200 OK).  
   └── If Key Not Found: Write hash to cache with 24-Hour TTL; proceed.  
5\. Filter: \[Intent RegEx Gate\] (Verifies string payload contains trade-relevant request parameters).  
   ├── Fails Filter: Halt scenario execution immediately (Cost: 0 Credits).  
   └── Passes Filter: Route to extraction engine.  
6\. Action: \[HTTP \- POST Request to Model API Endpoint\]  
   ├── URL: https://api.provider.com/v1/messages  
   ├── Headers: Authorization Bearer Key, Content-Type: application/json  
   └── Payload: { model: "model-version", system: "Extract customer name, phone, and parts requested. Output strictly as valid JSON.", messages: \[{ role: "user", content: "Email Body String" }\] }  
7\. Action: \[JSON Parser\] (Enforces destination schema validation rules).  
8\. Action: \[CRM App \- Create Lead Record\] (Maps individual JSON keys into field variables in Draft status).  
9\. Action: \[Slack \- Send Operational Update\] (Pushes deep link of CRM record directly to dispatch channel).

### **7.2 Technical Walkthrough 2: Document Extraction & Parts Manifests**

* **Objective:** Automatically extract lines from supplier item confirmation PDFs and bulk upsert parameters into an internal inventory tracking database.

1\. Trigger: \[Google Drive \- Watch Files\] (Monitors a target incoming invoice directory).  
2\. Action: \[HTTP \- Stream File Payload\] (Downloads raw binary file data over encrypted connection)\[cite: 1\].  
3\. Action: \[HTTP \- POST to Vision-Capable Model Endpoint\]  
   ├── Headers: Content-Type: application/json  
   └── Parameters: Max token ceilings configured to prevent unexpected multi-page credit spikes\[cite: 1\].  
4\. Action: \[Data Aggregator\] (Compiles multiple line items returned by the model into a unified array)\[cite: 1\].  
5\. Action: \[Iterator\] (Unpacks the clean array into structured rows)\[cite: 1\].  
6\. Action: \[Database / ERP App \- Upsert Row\] (Executes bulk batch updates into inventory tables)\[cite: 1\].

### **7.3 Technical Walkthrough 3: Automated Delayed Missed-Call Lead Resuscitation**

* **Objective:** Identify unreturned off-hours phone calls from new prospects, cross-reference contact histories, and initiate text-based interaction\[cite: 1\].

1\. Trigger: \[VoIP Provider \- Inbound Webhook\] (Triggers instantly on call status 'Missed' or 'No Answer')\[cite: 1\].  
2\. Action: \[CRM \- Search Records\] (Queries phone number parameter against existing contact database)\[cite: 1\].  
3\. Filter: \[New Account Check\]  
   ├── If Record Found: Halt scenario (Routes to standard account representative dashboard)\[cite: 1\].  
   └── If Record Not Found: Pass to automated response loop\[cite: 1\].  
4\. Action: \[Twilio \- Send SMS\]  
   └── Payload: "Hello, we noticed we just missed your call to our service department. We are currently assisting other field technicians, but what parts or tracking codes can we help you look up right now?"\[cite: 1\].  
5\. Action: \[CRM \- Create Lead Placeholder\] (Logs the outbound SMS timestamp and phone record to preserve historical audit trails)\[cite: 1\].