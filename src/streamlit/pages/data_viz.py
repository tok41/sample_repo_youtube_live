import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


_ = st.sidebar.slider(
    label="mu",
    min_value=-5.0,
    max_value=5.0,
    value=0.0,
    step=0.01,
    key="mu",
    # on_change=set_val,
)
scale = st.sidebar.slider(
    label="sigma", min_value=0.01, max_value=5.0, value=1.0, step=0.01
)

loc = st.session_state.mu

st.write(
    """
# データの可視化
    """
)

x = np.random.normal(loc=loc, scale=scale, size=500)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.hist(x, bins=50)
ax.set_xlim(-7, 7)
st.pyplot(fig)
