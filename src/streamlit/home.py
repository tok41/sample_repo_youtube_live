import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

st.write(
    """
# Streamlit Sample @ YouTube Live 

こんにちは。

## データ可視化の例
    """
)

st.sidebar.write(
    """
ここはサイドバーです
    """
)

a = st.sidebar.slider(
    label="alpha",
    min_value=0.01,
    max_value=10.0,
    value=1.0,
    step=0.01,
)

# a = 1.0
x = np.linspace(-3, 5, 100)
y = np.sin(a * x)

st.write(
    """
    ### matplotlibのオブジェクトを表示
    """
)

fig, ax = plt.subplots(1, 1, figsize=(15, 5))
ax.plot(x, y, label="sin")
ax.legend()
st.pyplot(fig)

st.write(
    """
    ### streamlit linechartオブジェクトを表示
    """
)

df = pd.DataFrame({"x": x, "y": y})
st.line_chart(data=df, x="x", y="y")

st.write(
    """
    ### データを表示
    """
)

st.dataframe(df)
# st.table(df)
