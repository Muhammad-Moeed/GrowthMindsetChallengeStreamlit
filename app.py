import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io  

# ****************Page Configuration*******************

st.set_page_config(page_title="📊 Data Visualization Dashboard", layout="wide")
st.markdown("""
   <style>
    .title { 
        text-align: center; 
        font-size: 40px !important;  
        font-weight: bold; 
        color:rgb(194, 0, 0);  
        font-family: 'Poppins', sans-serif;  
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.6);  
        margin-bottom: 10px;
    }
    .subtitle { 
        text-align: center; 
        font-size: 20px !important; 
        color: #AAB7B8;  
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }
    .upload-box { 
        border: 2px dashed #3498DB;  
        padding: 20px; 
        border-radius: 10px; 
        text-align: center; 
        background-color: #222831;  
        color: white;
    }
    .footer { 
        text-align: center; 
        font-size: 14px; 
        color: #AAB7B8; 
        margin-top: 50px;  
        padding: 10px;  
        border-top: 1px solid #555;  
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">📊 Data Visualization Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your CSV or Excel file to generate interactive charts.</p>', unsafe_allow_html=True)
st.markdown('<div class="upload-box">📂 Upload your CSV or Excel file</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # File Reading

        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
    else:
        st.success("✅ File uploaded successfully!")
        st.write("### 📄 Data Preview")
        st.dataframe(df.head())

        # Data Cleaning Options

        st.write("### 🛠 Data Cleaning Options")
        if st.checkbox("Remove Duplicates"):
            df = df.drop_duplicates()
        if st.checkbox("Remove Missing Values"):
            df = df.dropna()
        st.write("### 📊 Select Columns for Visualization")
        selected_columns = st.multiselect("Choose columns", df.columns)

        if selected_columns:
            df_selected = df[selected_columns]
            df_numeric = df_selected.select_dtypes(include=['number'])

            st.write("### 📊 Choose Chart Type")
            chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

            if chart_type == "Line Chart":
                if df_numeric.empty:
                    st.warning("⚠️ Selected columns do not contain numeric data.")
                else:
                    fig = px.line(df_numeric, markers=True, title="📈 Line Chart")  
                    fig.update_layout(transition_duration=700)
                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Bar Chart":
                if df_numeric.empty:
                    st.warning("⚠️ Selected columns do not contain numeric data.")
                else:
                    fig = px.bar(df_numeric, barmode="group", title="📊 Bar Chart")
                    fig.update_layout(transition_duration=700)
                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Scatter Plot":
                if len(df_numeric.columns) >= 2:
                    fig = px.scatter(df_numeric, 
                                     x=df_numeric.columns[0], 
                                     y=df_numeric.columns[1], 
                                     title="🔵 Scatter Plot", 
                                     color=df_numeric.columns[0], 
                                     size=df_numeric.columns[1])
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("⚠️ Select at least 2 numeric columns for a scatter plot.")

        st.write("### 🔄 Convert File")
        output_format = st.selectbox("Select format", ["CSV", "Excel"])

        if st.button("Convert & Download", key="convert_button"):
            try:
                if output_format == "CSV":
                    converted_file = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download CSV",
                        data=converted_file,
                        file_name="converted_file.csv",
                        mime="text/csv"
                    )
                else:
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False)
                    output.seek(0)

                    st.download_button(
                        label="📥 Download Excel",
                        data=output,
                        file_name="converted_file.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                st.success("✅ File converted successfully!")
            except Exception as e:
                st.error(f" Error during file conversion: {e}")
else:
    st.info("📌 Please upload a file to get started.")

# ********** Footer **********
st.markdown('<p class="footer">© 2025 Data Visualization Dashboard | Developed by Muhammad Moeed</p>', unsafe_allow_html=True)
