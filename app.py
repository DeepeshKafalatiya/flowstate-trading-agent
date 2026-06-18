import streamlit as st
import time
from database import init_db, get_active_workflow
from agent import process_trading_strategy

st.set_page_config(page_title="FlowState Trader Platform", page_icon="📈", layout="wide")
init_db()

st.title("📈 FlowState: Autonomous Trading Discipline Agent")
st.subheader("Lock in peak cognitive execution. Neutralize erratic emotional impulses.")

with st.sidebar:
    st.header("Strategic Configuration")
    user_strategy = st.text_area("Enter your planned trade setups/focus scope:", 
                                 placeholder="e.g., Trading Nifty morning session setups using standard breakout guidelines.")
    if st.button("Configure Engine Matrix"):
        if user_strategy:
            with st.spinner("Processing architectural modules..."):
                process_trading_strategy(user_strategy)
                st.success("Execution Matrix Synchronized!")
                time.sleep(1)
                st.rerun()
        else:
            st.warning("Please supply a valid strategy prompt first.")

# Main Interface Monitor
active_steps = get_active_workflow()
if active_steps:
    st.write("### 📅 Programmed Disciplined Sequence")
    
    for step in active_steps:
        st.info(f"⚡ **Protocol:** {step[1]} | **Priority Hierarchy:** Tier-{step[2]} | **Duration Window:** {step[3]} Minutes")
        
    st.write("---")
    st.write("### ⏱️ Direct Session Controller")
    current_active = active_steps[0]
    st.warning(f"**Current Action Metric:** {current_active[1]}")
    
    timer_slot = st.empty()
    countdown_seconds = current_active[3] * 60
    
    if st.button("Authorize Execution Protocol"):
        while countdown_seconds:
            minutes, seconds = divmod(countdown_seconds, 60)
            timer_slot.metric(label="Remaining Secure Window Time", value=f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)
            countdown_seconds -= 1
        st.balloons()
        st.success("Target protocol cycle reached. Proceeding to audit logs.")
else:
    st.write("Trading sequence monitor is offline. Feed your daily trading vision parameters into the sidebar engine to boot.")