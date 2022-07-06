import os
import json
import streamlit.components.v1 as components

from pollination_streamlit_io import (get_hbjson, get_host)

import streamlit as st

st.header("Get Model")

host = get_host()

if host is not None:
    st.header("Host: " + host)
else:
    st.header("Host: undefined")

st.subheader('Get hbjson')


def callback_once(arg1, arg2):
    st.session_state['we-did-it'] = arg1 + ' ' + arg2


hbjson = get_hbjson('get-hbjson', on_change=callback_once,
                    args=['Hello'], kwargs={'arg2': 'World'})

if 'we-did-it' in st.session_state:
    st.write(st.session_state['we-did-it'])
