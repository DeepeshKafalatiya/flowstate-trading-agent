def process_trading_strategy(prompt: str):
    """
    Stable Agent Logic: Generates strict disciplined protocols for trading setup.
    """
    p = prompt.lower().strip()
    steps = []
    
    # Pre-market level tracking
    if "nifty" in p or "banknifty" in p or "option" in p:
        steps.append({"step_name": "🔍 Audit Pre-Market Global Indices & Local Sentiment", "priority": 1, "allocated_time": 15, "status": "active"})
    else:
        steps.append({"step_name": "🔍 Scan Market Structure & Identify Core Trend", "priority": 1, "allocated_time": 10, "status": "active"})
        
    # Breakout or scalp tracking
    if "breakout" in p or "break" in p:
        steps.append({"step_name": "⏱️ Wait for 15-Min Candle Closure Outside Key Range", "priority": 2, "allocated_time": 20, "status": "pending"})
    elif "scalp" in p:
        steps.append({"step_name": "⚡ Identify Quick Momentum Spikes on 1-Min/3-Min Chart", "priority": 2, "allocated_time": 5, "status": "pending"})
    else:
        steps.append({"step_name": "📈 Identify Dynamic Support/Resistance Levels", "priority": 2, "allocated_time": 15, "status": "pending"})

    # Risk Management Guardrails
    if "risk" in p or "ratio" in p or "stop" in p or "loss" in p:
        steps.append({"step_name": "🛡️ Hardcode Stop-Loss & Fix Maximum 1:2 Risk-Reward Matrix", "priority": 1, "allocated_time": 5, "status": "pending"})
    else:
        steps.append({"step_name": "🛡️ Enforce Default Trailing Stop-Loss Protection Guardrail", "priority": 2, "allocated_time": 10, "status": "pending"})

    steps.append({"step_name": "🚀 Execute Trade on Terminal with Institutional Discipline", "priority": 3, "allocated_time": 30, "status": "pending"})
    steps.append({"step_name": "📝 Post-Trade Audit: Log Emotional State & Registry Metrics", "priority": 3, "allocated_time": 10, "status": "pending"})

    return steps