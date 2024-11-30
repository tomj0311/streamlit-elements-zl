import streamlit as st
from streamlit_elements import elements, mui

# Debug section at the top
st.write("### Testing Elements Component")

with elements("key1"):
    with mui.CardMedia(sx={"padding": "36px", "border": "1px solid #f0f0f0"}):
        mui.TextField(
            label="Input 1",
            variant="outlined",
            fullWidth=True,
            sx={"marginBottom": "16px"},
            key="input1",
        )
        mui.TextField(
            label="Input 2",
            variant="outlined",
            fullWidth=True,
            key="input2",
        )

# Access the input values from st.session_state and assign to variables
a = st.session_state.get("key1", "")

# Now you can use the variables 'a' and 'b' as needed
st.write("Input 1:", a)



