import streamlit as st
import pandas as pd
import pickle

# Method to load the clustered dataframe
def load_clustered_data():
    clustered_df = pd.read_csv('combined_data.csv')
    return clustered_df

# Streamlit app function
def main():

    st.title("NEWS ARTICLE CLUSTERING")
    st.markdown("---")
    st.markdown("---")

    # Load the clustered dataframe
    data = load_clustered_data()

    # Displaying clusters and related stories
    categories = ['Business', 'Politics', 'Sports', 'Entertainment']

    selected_category = st.sidebar.selectbox("Select a Category", categories)

    st.header(f"{selected_category} Articles")

    category_cluster_mapping = {'Business': 0, 'Politics': 1, 'Sports': 2, 'Entertainment': 3}
    selected_cluster = category_cluster_mapping[selected_category]

    cluster_articles = data[data['Cluster'] == selected_cluster]

    for idx, row in cluster_articles.iterrows():
        st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'><b>Title:</b> {row['Title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'><b>Category:</b> {row['Category']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'><b>Source:</b> {row['Source']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'><b>Summary:</b> {row['Content']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:5px;'><a href='{row['Link']}' target='_blank'>Read more</a></div>", unsafe_allow_html=True)
        st.markdown("---")

# Running the app
if __name__ == "__main__":
    main()
