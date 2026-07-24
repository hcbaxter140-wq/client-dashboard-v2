import streamlit as st
import pandas as pd
from master_pipeline import transform_data 

# 1. Page Configuration
st.set_page_config(page_title="Client Operations Dashboard", layout="wide")

# 2. Header
st.title("📊 Automated Metrics Dashboard")
st.divider()

# 3. The Uploader
uploaded_file = st.file_uploader("Upload Today's Raw Data Export (CSV)", type=['csv'])

# 4. The Trigger Engine
if uploaded_file is not None:
    # Read the file directly from the browser
    df_raw = pd.read_csv(uploaded_file)
    
    # Run your math
    with st.spinner("Processing data..."):
        df_clean = transform_data(df_raw)
        
    st.success("Pipeline executed successfully!")
    
    # 5. Display Top Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records Processed", len(df_clean))
    col2.metric("Key Metric 2", "---")
    col3.metric("Key Metric 3", "---")

    st.divider()
    
    # 6. Display Data
    st.subheader("Data Overview")
    st.dataframe(df_clean, use_container_width=True)
else:
    st.info("Please upload a CSV file to generate your dashboard.")
