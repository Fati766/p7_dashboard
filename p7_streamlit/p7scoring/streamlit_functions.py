import streamlit as st


def st_buttons(id):
    with st.sidebar:
        btn_global_importance = st.button("Global features importance")
        btn_local_importance = st.button("Decision details: id " + str(id))
        btn_distribution = st.button("Distribution comparaison id " + str(id))
        n_features = st.slider('Number of features:', min_value=1, max_value=31, value=15, step=1)
    return btn_global_importance, btn_local_importance, btn_distribution, n_features
