import os, json
import streamlit.components.v1 as components

from pollination_streamlit_io import (get_geometry, get_hbjson, send_geometry, send_hbjson, get_host, send_results)

import streamlit as st

st.header("Get Model")

host = get_host()

if host is not None:
  st.header("Host: " + host)
else :
  st.header("Host: undefined")

st.subheader('Get hbjson')

def callback_once(*, callback_args, callback_kwargs):
    st.session_state['we-did-it-once'] = ' '.join(callback_args) + ' ' + ' '.join(list(callback_kwargs.values()))

hbjson = get_hbjson('get-hbjson-once', on_change=callback_once, args=['Hello'], kwargs={'arg2': 'World'})

def callback_twice(*, callback_args, callback_kwargs):
    st.session_state['we-did-it-twice'] = ' '.join(callback_args) + ' ' + ' '.join(list(callback_kwargs.values()))

hbjson = get_hbjson('get-hbjson-twice', on_change=callback_once, args=['Again'], kwargs={'arg2': 'Once Again'})

if 'we-did-it-once' in st.session_state :
    st.write(st.session_state['we-did-it-once'])

if 'we-did-it-twice' in st.session_state :
    st.write(st.session_state['we-did-it-twice'])