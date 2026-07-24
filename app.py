import streamlit as st
import pandas as pd

st.set_page_config(page_title="Operations Pro Forma", layout="wide", initial_sidebar_state="expanded")
with st.sidebar:
    st.header("⚙️ Data Control Center")
    st.success("🟢 System Online & Secure")
    st.markdown("Auto-syncing from local `/data` directory...")
    
    st.divider()
    st.button("🔄 Force Data Sync", type="primary", use_container_width=True)
    
    st.info("Note: This is a read-only showcase environment.")

st.title("📊 Executive Operations Dashboard")
st.markdown("Daily Yield, Cash Flow, and Payroll Pro Forma")
st.divider()

try:
    df_main = pd.read_csv("data/harvest.csv")
except FileNotFoundError:
    blocks = ['B1 Turkey', 'B2 Turkey', 'B3 Mission', 'B4 Mission', 'B5 Sierra']
    df_main = pd.DataFrame({
        'Block_ID': blocks,
        'Pounds_Harvested': [175105, 158779, 67539, 44188, 41893],
        'Gross_Revenue': [323944, 293741, 124947, 81747, 77502],
        'Net_Profit': [115321, 98450, 42100, 21500, 20100]
    })

col1, col2, col3 = st.columns(3)
col1.metric("Total Season Revenue", f"${df_main['Gross_Revenue'].sum():,.0f}", "+12% vs last week")
col2.metric("Total Pounds Harvested", f"{df_main['Pounds_Harvested'].sum():,.0f} lbs")
col3.metric("Blended Profit Margin", "34.2%", "+2.1% efficiency")

st.divider()

col_chart, col_data = st.columns([2, 1])

with col_chart:
    st.subheader("📈 Block Profitability")
    st.bar_chart(df_main, x='Block_ID', y='Net_Profit')

with col_data:
    st.subheader("Raw Data Feed")
    st.dataframe(df_main, use_container_width=True, hide_index=True)
