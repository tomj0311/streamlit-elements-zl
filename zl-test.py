import streamlit as st
from streamlit_elements import elements, mui
from threading import Thread

# Debug section at the top
st.write("### Testing Elements Component")

# Receive data from frontend
if "key1" in st.session_state:
    st.write("Data received from frontend:", st.session_state["key1"])
else:
    st.write("No data received yet.")

with elements("key1"):
    with mui.CardMedia(sx={"padding": "36px", "border": "1px solid #f0f0f0"}):
        # TextField
        mui.TextField(
            label="Input 1",
            variant="outlined",
            fullWidth=True,
            sx={"marginBottom": "16px"},
            id="input1",
        )
        mui.TextField(
            label="Input 2",
            variant="outlined",
            fullWidth=True,
            id="input2",
        )
        
        # RadioGroup
        mui.RadioGroup(
            row=True,
            sx={"marginBottom": "16px"},
            children=[
                mui.FormControlLabel(value="option1", control=mui.Radio(), label="Option 1", key="radio1"),
                mui.FormControlLabel(value="option2", control=mui.Radio(), label="Option 2", key="radio2"),
            ],
        )
        
        # Switch
        mui.FormControlLabel(
            control=mui.Switch(),
            label="Toggle",
            sx={"marginBottom": "16px"},
            id="toggle",
            key="toggle",
        )
        
        # Checkbox
        mui.FormControlLabel(
            control=mui.Checkbox(),
            label="Check Box",
            sx={"marginBottom": "16px"},
            id="checkbox",
            key="checkbox",
        )
        
        # Select
        mui.Select(
            variant="outlined",
            fullWidth=True,
            sx={"marginBottom": "16px"},
            key="select",
            children=[
                mui.MenuItem(value="option1", children="Option 1", key="select-option1"),
                mui.MenuItem(value="option2", children="Option 2", key="select-option2"),
            ],
        )
        
        # Multi Select
        mui.Select(
            label="Multi Select",
            multiple=True,
            fullWidth=True,
            sx={"marginBottom": "16px"},
            value=[],  # Ensure value is an array
            key="multi-select",
            children=[
                mui.MenuItem(value="option1", children="Option 1", key="multi-select-option1"),
                mui.MenuItem(value="option2", children="Option 2", key="multi-select-option2"),
                mui.MenuItem(value="option3", children="Option 3", key="multi-select-option3"),
            ],
        )
        
        # Slider
        mui.Slider(
            defaultValue=30,
            sx={"marginBottom": "16px"},
            key="slider",
        )
        
        # Button
        mui.Button(
            "Button",
            variant="contained",
            sx={"marginBottom": "16px"},
            key="button",
        )
        
        # Autocomplete
        # mui.Autocomplete(
        #     options=["Option 1", "Option 2"],
        #     renderInput=lambda params: mui.TextField(
        #         {...params, label="Autocomplete", variant="outlined", fullWidth=True}
        #     ),
        #     sx={"marginBottom": "16px"},
        #     key="autocomplete",
        # )
        
        # DatePicker
        # mui.DatePicker(
        #     label="Date Picker",
        #     renderInput=lambda params: mui.TextField(
        #         {...params, variant="outlined", fullWidth=True}
        #     ),
        #     sx={"marginBottom": "16px"},
        #     key="datepicker",
        # )
        
        # # TimePicker
        # mui.TimePicker(
        #     label="Time Picker",
        #     renderInput=lambda params: mui.TextField(
        #         {...params, variant="outlined", fullWidth=True}
        #     ),
        #     sx={"marginBottom": "16px"},
        #     key="timepicker",
        # )
        
        # # DateTimePicker
        # mui.DateTimePicker(
        #     label="DateTime Picker",
        #     renderInput=lambda params: mui.TextField(
        #         {...params, variant="outlined", fullWidth=True}
        #     ),
        #     sx={"marginBottom": "16px"},
        #     key="datetimepicker",
        # )
        
        # Rating
        mui.Rating(
            defaultValue=2,
            sx={"marginBottom": "16px"},
            key="rating",
        )
        
        # ToggleButtonGroup
        # mui.ToggleButtonGroup(
        #     value="left",
        #     exclusive=True,
        #     sx={"marginBottom": "16px"},
        #     key="togglebuttongroup",
        #     children=[
        #         mui.ToggleButton(value="left", children="Left", key="togglebutton-left"),
        #         mui.ToggleButton(value="center", children="Center", key="togglebutton-center"),
        #         mui.ToggleButton(value="right", children="Right", key="togglebutton-right"),
        #     ],
        # )
        
        # Input
        mui.Input(
            placeholder="Basic input",
            sx={"marginBottom": "16px"},
            key="input",
        )
        
        # TextareaAutosize
        # mui.Textarea(
        #     minRows=3,
        #     placeholder="Auto-resizing textarea",
        #     style={"width": "100%", "marginBottom": "16px"},
        #     key="textareaautosize",
        # )
        
        # FormControl
        mui.FormControl(
            sx={"marginBottom": "16px"},
            key="formcontrol",
            children=[
                mui.FormLabel(children="Form Label", key="formlabel"),
                mui.FormHelperText(children="Helper text", key="formhelpertext"),
            ],
        )

st.write(st.session_state.get("tom"))
