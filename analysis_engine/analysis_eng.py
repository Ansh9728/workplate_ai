# from sklearn.cluster import KMeans
# from sklearn.ensemble import IsolationForest
# from sklearn.decomposition import PCA
# import pandas as pd
# from transformers import pipeline
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Descriptive statics
# def generate_summary(df):
#     summary = {
#         "shape": df.shape,
#         "missing_values": df.isnull().sum(),
#         "description": df.describe()
#     }
#     return summary


# def generate_visualizations(df):
    
#     sns.pairplot(df)
#     plt.show()

#     sns.heatmap(df.corr(), annot=True)
#     plt.show()


# # ML model
# def clustering_analysis(df, n_clusters=3):
#     # Select only numeric columns
#     numeric_df = df.select_dtypes(include=['float64', 'int64'])

#     if numeric_df.empty:
#         raise ValueError("No numeric data available for clustering.")

#     kmeans = KMeans(n_clusters=n_clusters)
    
#     # Check if there are enough data points for clustering
#     if len(numeric_df) < n_clusters:
#         raise ValueError(f"Not enough data points ({len(numeric_df)}) for {n_clusters} clusters.")
    
#     df['Cluster'] = kmeans.fit_predict(numeric_df)
#     return df['Cluster']


# def anomaly_detection(df):
#     iso_forest = IsolationForest(contamination=0.1)
#     df['Anomaly'] = iso_forest.fit_predict(df.select_dtypes(include=['float64', 'int64']))
#     return df['Anomaly']


# def dimensionality_reduction(df, n_components=2):
#     pca = PCA(n_components=n_components)
#     reduced_df = pca.fit_transform(df.select_dtypes(include=['float64', 'int64']))
#     return pd.DataFrame(reduced_df, columns=[f'PC{i+1}' for i in range(n_components)])


# def summarize_results(eda_summary, clustering_result, anomaly_result):
#     summarizer = pipeline("text-generation", model="openai-community/gpt2")
#     report = f"Data Summary: {eda_summary}\nClustering Result: {clustering_result}\nAnomaly Detection Result: {anomaly_result}"
#     return summarizer(report, max_length=500, min_length=50, do_sample=False)[0]['summary_text']


# class AnalysisEngine:
#     def __init__(self, files):
#         self.data_frames = files

#     def run_analysis(self):
#         results = {}
#         for name, df in self.data_frames.items():
#             summary = generate_summary(df)
#             clusters = clustering_analysis(df)
#             anomalies = anomaly_detection(df)
#             pca_result = dimensionality_reduction(df)

#             results[name] = {
#                 "summary": summary,
#                 "clusters": clusters,
#                 "anomalies": anomalies,
#                 "pca": pca_result
#             }
#         return results
    
#     def generate_report(self, analysis_results):
#         for name, result in analysis_results.items():
#             report = summarize_results(result['summary'], result['clusters'], result['anomalies'])
#             st.write(f"Report for {name}:")
#             st.write(report)

import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


class AnalysisEngine:

    def __init__(self, files):
        self.files = files

    
    def run_analysis(self):
        for name, file in self.files.items():
            st.info(name)
            profile = ProfileReport(file, title="Pandas Profiling Report")
            # st_profile_report(profile)
            return profile
        
    def generate_report(self, analysis_result):
        st_profile_report(analysis_result)

        

            