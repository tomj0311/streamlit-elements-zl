from streamlit_elements import mui, elements
import streamlit as st

with elements("key2"):

    # Card container for the form
    with mui.Card(variant="outlined", sx={"padding": "10px", "maxWidth": "600px", "margin": "0 auto"}):
        
        # Form title using Typography
        mui.Typography("User Registration Form", variant="h4", gutterBottom=True)

        # Alert for instructions
        mui.Alert("Please fill out the form carefully and review the details before submitting.", 
                  severity="info", variant="outlined", sx={"marginBottom": "20px"})

        # Profile Avatar
        mui.Avatar("A", sx={"width": 80, "height": 80, "marginBottom": "20px"})

        # Input fields for registration
        mui.TextField(label="First Name", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
        mui.TextField(label="Last Name", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
        mui.TextField(label="Email", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
        mui.TextField(label="Phone Number", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
        mui.TextField(label="Address", variant="outlined", fullWidth=True, multiline=True, rows=3, sx={"marginBottom": "10px"})

        # Role selection using Chips
        mui.Typography("Select Role:", variant="subtitle1", sx={"marginBottom": "10px"})
        mui.Chip(label="User", variant="outlined", color="primary", sx={"marginRight": "10px"})
        mui.Chip(label="Admin", variant="outlined", color="secondary", sx={"marginRight": "10px"})
        mui.Chip(label="Moderator", variant="outlined", color="success", sx={"marginRight": "10px"})

        # Additional fields using Paper for organization
        with mui.Paper(variant="outlined", sx={"padding": "10px", "marginTop": "20px", "marginBottom": "10px"}):
            mui.Typography("Additional Information", variant="h6", gutterBottom=True)
            mui.TextField(label="Company", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
            mui.TextField(label="Position", variant="outlined", fullWidth=True, sx={"marginBottom": "10px"})
        
        # Display agreement notice with IconButton
        with mui.Stack(direction="row", alignItems="center"):
            mui.IconButton(icon="check_circle", color="success")
            mui.Typography("I agree to the terms and conditions", variant="body2")

        # Submit button
        mui.Button("Submit", id="submit", variant="contained", color="primary", sx={"marginTop": "20px", "marginBottom": "10px", "float": "right"})

if st.session_state.get("id"):
    st.write(st.session_state.get("id"))