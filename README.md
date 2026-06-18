# 📈 FlowState: Autonomous Trading Discipline Agent
### 🚀 Open Innovation Track | Hackathon Project Portfolio

**FlowState Agent** is an AI-powered workflow automation and cognitive discipline system engineered for financial traders. Built under the **Open Innovation Track**, this system addresses a critical real-world problem: **emotional over-trading and lack of execution discipline**. 

Instead of generic alerts, FlowState acts as an autonomous guardrail system that intercepts trading intent, decomposes it into structured, risk-managed operational protocols, and strictly logs interaction metrics into a secure registry database. This ensures traders stay in their optimal "Flow State" without falling prey to impulsive market moves.

---

## 🛠️ System Architecture & Workflow

The architecture is built completely decoupled via a modular design, enabling seamless plug-and-play integrations with both **Mobile Applications (React Native/Flutter)** and **Web Portals (React/Next.js)** using secure asynchronous REST APIs.

1. **Frontend Interface (Streamlit Dashboard):** Serves as the immediate execution desk where traders register their strategic focus rules or daily session prompts.
2. **Backend Engine (FastAPI Rest API):** Acts as the high-performance core broker handling data packages, request validation, and cross-platform syncing.
3. **Agentic Processor (`agent.py`):** The logical core that parses user strings to enforce strict risk-reward thresholds, stop-loss setups, and dynamic time blocks.
4. **Data Ledger Layer (SQLite Core):** Functions as the local secure registry database tracking trading session blocks and auditing interactions.

---

## 📂 Project Directory Structure

```text
flowstate_trading_agent/
│
├── config.py          # Environment settings & credentials router
├── database.py        # SQLite Local Engine & Trade Session Registry
├── agent.py           # Core Intelligent Financial Protocol & Logic Matcher
├── main.py            # FastAPI REST API Backend (Brain for Mobile/Web Expansion)
├── app.py             # Streamlit Interactive Execution Desk UI
└── README.md          # Comprehensive Technical System Documentation

## ⚡ API Endpoint Schema (FastAPI Backend Server)

The backend provides complete endpoint transparency through auto-generated Swagger UI routing, ideal for multi-device client integrations:

* **`POST /api/v1/initialize-workflow`** Accepts a raw financial strategy string (JSON body), passes it to the algorithmic parser, clears overlapping stale context data, and initializes the target rules matrix inside the secure ledger.
  
* **`GET /api/v1/current-workflow`** Queries the database layer and returns a clean, structured array of target operational steps, allotted durations, and step priorities directly to web browsers or mobile device engines.

---

## 🚀 Installation & Local Environment Setup

Follow these precise steps to deploy and test the entire multi-process suite locally on your computer:

### 1. Clone & Navigate to Workspace
```bash
git clone [https://github.com/DeepeshKafalatiya/flowstate-trading-agent.git](https://github.com/DeepeshKafalatiya/flowstate-trading-agent.git)
cd flowstate-trading-agent

2. Install Core Production Dependencies
Ensure you have Python 3.8+ installed, then run:

Bash
pip install fastapi uvicorn streamlit pydantic python-dotenv
3. Launch the FastAPI Rest Server (For Mobile/Web App Connectivity)
Run the asynchronous production-ready server gateway:

Bash
uvicorn main:app --reload
Once initialized, navigate to the local documentation gateway to audit or test raw API calls:
👉 Interactive Swagger Testing Desk: http://127.0.0.1:8000/docs

4. Boot the Interactive Trader Interface Panel
In a new concurrent terminal terminal window, run the application dashboard:

Bash
streamlit run app.py
This launches your local engine control window instantly at: http://localhost:8501

💎 Hackathon Core Validation Metrics
Real-World Impact: Resolves structural psychology failures in active day trading by automating sequence guardrails.

Open Innovation Scalability: The production-ready FastAPI endpoints make it instantly ready to connect with Android/iOS integration packages or Next-gen cloud spaces.

Autonomous Transparency: Replaces fragile temporary caches with robust SQLite data structures to maintain precise logging verification.
