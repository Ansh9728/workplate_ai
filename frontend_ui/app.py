import streamlit as st
from data_Processing.data_ingestion import DataIngestion
from analysis_engine.analysis_eng import AnalysisEngine

def main():

    st.title('Workplate Ai Assignment')
    uploaded_files = st.file_uploader(
        "Upload Your File",
        type=['xlsx', 'csv', 'json'],
        accept_multiple_files=True,
    )

    if st.button('SUBMIT'):

        processor = DataIngestion(uploaded_files)
        cleaned_data = processor.clean_data()

        engine = AnalysisEngine(cleaned_data)
        analysis_results = engine.run_analysis()
        engine.generate_report(analysis_results)

        
main()