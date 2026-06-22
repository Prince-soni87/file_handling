import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello Streamlit")

import streamlit as st
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display DataFrame
st.write("Here is the dataframe")
st.write(df)

# Create chart data
chart_data = pd.DataFrame({
    'Sales': [10, 20, 30, 40],
    'Profit': [2, 5, 8, 12]
})

# Display line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)