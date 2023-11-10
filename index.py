import streamlit as st
import time

st.set_page_config(page_title='controls', page_icon=None, layout="centered")
st.title('_Dehumidifier_ Controller 🎛')

status = 1
#while True:
    # loop and check if TinyZero replies, if no it's off, if yes its on
    # if no reply , display "Device has no power", delay(1000) then continue loop
    # if device returns off, display "Device is off" ,delay(1000) then continue loop
    # If on, display 3 option (High,Low, Off)
    # If high or low, display option to adjust swivelling action
with st.status("Attempting to connect...", expanded=True) as status:
    st.write("Searching for Dehumidifier TinyZero(Master)...")
    time.sleep(2)
    st.write("Found Dehumidifier.")
    time.sleep(1)
    st.write("Establishing connection...")
    time.sleep(1)
    status.u