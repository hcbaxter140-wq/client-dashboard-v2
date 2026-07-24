import streamlit as st
import pandas as pd
from master_pipeline import transform_data 

st.set_page_config(page_title="Operations Dashboard", layout="wide")

with st.sidebar:
    st.header("⚙️ Data Control Center")
    st.markdown("Upload your daily export below to update the system.")
    
    uploaded_file = st.file_uploader("Drop CSV Here", type=['csv'])
    run_sync = st.button("🔄 Generate Dashboard", use_container_width=True, type="primary")

st.title("📊 Automated Metrics Dashboard")
st.divider()

if uploaded_file is not None and run_sync:
    
    with st.spinner("Processing data engine..."):
        df_raw = pd.read_csv(uploaded_file)
        df_clean = transform_data(df_raw)
        
    st.success("System updated successfully!")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records Processed", len(df_clean))
    col2.metric("System Status", "Active")
    col3.metric("Last Sync", "Just Now")

    st.divider()
    st.subheader("📈 Performance Trends")
    st.bar_chart(df_clean, x=df_clean.columns[0]) 
    st.divider()
    st.subheader("Raw Data Feed")
    st.dataframe(df_clean, use_container_width=True)
        
elif uploaded_file is not None:
    st.info("File loaded successfully. Click 'Generate Dashboard' in the sidebar to run the math.")
else:
    st.info("👈 Please drop your CSV file into the sidebar to begin.")
