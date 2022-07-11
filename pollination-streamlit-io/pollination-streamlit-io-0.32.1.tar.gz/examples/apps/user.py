import os
import json
import streamlit.components.v1 as components

from pollination_streamlit.selectors import get_api_client

from pollination_streamlit_io import (auth_user)

import streamlit as st

api_client = get_api_client()

st.header("Auth User")

auth_user('auth-user', accessToken=api_client.jwt_token)
st.write(api_client.jwt_token)
