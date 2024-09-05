import streamlit as st
import pandas as pd
import json
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report


def validate_file_type(uploaded_file):

    file_name = uploaded_file.name

    if file_name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)

    elif file_name.endswith('.xlsx'):
        data = pd.read_excel(uploaded_file)

    elif file_name.endswith('.json'):
        byte_file = uploaded_file.read()
        json_data = json.loads(byte_file.decode('utf-8'))
        
        if isinstance(json_data, dict):
            data = pd.DataFrame([json_data])
        else:
            data = pd.DataFrame(json_data)     
    else:
        raise("Unsupported Files Format")

    return file_name, data


class DataIngestion:

    def __init__(self, uploaded_files):
        self.uploaded_files = uploaded_files

    def clean_data(self):

        cleaned_data = {}
        
        for uploaded_file in self.uploaded_files:

            file_name, data = validate_file_type(uploaded_file)

            data = data.drop_duplicates()
            cleaned_data[file_name] = data

        return cleaned_data 
            
