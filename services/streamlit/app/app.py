import streamlit as st
import pandas as pd
import numpy as np
from data import get_data


st.map(get_data())
