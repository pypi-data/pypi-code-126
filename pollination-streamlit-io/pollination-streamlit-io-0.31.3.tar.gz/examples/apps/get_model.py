import os
import json
import streamlit.components.v1 as components

from pollination_streamlit_io import (get_hbjson, get_host)

import streamlit as st

st.header("Get Model")

host = get_host()

st.header("Host: " + (host or 'undefined'))

st.subheader('Get hbjson')


def callback_once(arg1='Default01', arg2='Default02'):
    if 'hbjson' in st.session_state['get-hbjson']:
        st.session_state['we-did-it'] = st.session_state['get-hbjson']['hbjson']


hbjson = get_hbjson('get-hbjson', on_change=callback_once)

if 'we-did-it' in st.session_state:
    st.json(st.session_state['we-did-it'], expanded=False)
