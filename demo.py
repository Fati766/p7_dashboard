import json
import requests
import streamlit as st

from p7scoring.streamlit_functions import st_buttons

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/"

    st.title("Dashboard crédit client")

    ids_url = url + 'ids/'
    response = requests.get(ids_url)
    content = json.loads(response.content.decode('utf-8')).values()
    id = st.selectbox(label='Client id', options=content)

    score_url = url + "predict/?id_client=" + str(id)
    response = requests.get(score_url)
    score = json.loads(response.content.decode('utf-8'))['score']
    if score == 0:
        st.write(':green[Credit accordé]')
    elif score == 1:
        st.write(':red[Credit refusé]')
    else:
        st.write(':red[Client inconnu]')

    st.write("Information client")
    client_url = url + "id_data/?id=" + str(id)
    response = requests.get(client_url)
    content = json.loads(response.content.decode('utf-8'))['data']
    # st.table(content)
    # print(content)
    st.dataframe(content)

    btn_global_importance, btn_local_importance, btn_distribution, n_features = st_buttons(id)

    if btn_global_importance:
        st.write("Global feature importance")
        global_url = url + "global/?n=" + str(n_features)
        content = requests.get(global_url).text
        st.components.v1.html(content, width=800, height=800, scrolling=True)

    if btn_distribution :
        st.write("Distribution features")
        dists_url = url + "dists/?n=" + str(n_features) + "&id=" + str(id)
        content = requests.get(dists_url).text
        st.components.v1.html(content, width=800, height=800, scrolling=True)

    if btn_local_importance:
        st.write("Local feature importance")
        local_url = url + "lime_local/?id=" + str(id) + "&n=" + str(n_features)
        content = requests.get(local_url).text
        st.components.v1.html(content, width=800, height=800, scrolling=True)

