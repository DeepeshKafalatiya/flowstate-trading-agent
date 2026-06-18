from database import add_trading_step, register_interaction, clear_previous_session

def process_trading_strategy(user_prompt):
    """
    Intelligently breaks down trading intent into a strict risk-managed focus sequence.
    Ensures discipline and updates the backend registry instantly.
    """
    clear_previous_session()
    prompt_lower = user_prompt.lower()
    
    # Context-aware structural mapping
    if "nifty" in prompt_lower or "banknifty" in prompt_lower or "breakout" in prompt_lower:
        add_trading_step("Analyze Pre-Market Levels & Open Interest (OI) Data", 1, 15)
        add_trading_step("Wait for Daily Initial Balance / 15-Min Candle Breakout Range", 1, 20)
        add_trading_step("Verify Risk-Reward Ratio (Min 1:2) & Set Rigid Stop-Loss", 2, 10)
        add_trading_step("Execute Ordered Trade Position without Manual Intervention", 2, 45)
        add_trading_step("Log P&L Outcome, Trade Execution Metrics & Emotion Index", 3, 10)
        register_interaction(user_prompt, "Generated Structured Indian Indices Breakout Workflow")
        
    elif "crypto" in prompt_lower or "bitcoin" in prompt_lower or "scalping" in prompt_lower:
        add_trading_step("Check Global Market Sentiment & High Liquidity Blocks", 1, 10)
        add_trading_step("Monitor Order Book Spreads & Volume Anomalies", 1, 15)
        add_trading_step("Execute High-Frequency Scalping Block", 2, 30)
        add_trading_step("Commit Executed Trades Directly to Secure Registry Ledger", 3, 10)
        register_interaction(user_prompt, "Generated Crypto High-Frequency Scalping Sequence")
        
    else:
        # Default disciplined baseline routine for all other standard market scripts
        add_trading_step("Define Daily Loss Limits & Target Risk Parameters", 1, 10)
        add_trading_step("Execute Monitored High-Focus Setup Strategy Block", 1, 45)
        add_trading_step("Review Process Logs and Refresh Workspace", 2, 15)
        register_interaction(user_prompt, "Generated Standard Risk-Managed Guardrail Sequence")
        
    return True