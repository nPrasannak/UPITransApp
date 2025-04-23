import streamlit as st
import requests
import calendar
from API.post_values_api import post_call as postcall

st.title("UPI Trans Predict Check App")

Bankoptions = {
    "axis": 0,
    "hdfcbank": 1,
    "icici": 2,
    "sbi": 3,
    "ybl": 4
}

Amount = st.number_input("Enter an Amount", min_value=0, step=1)
month_names = {calendar.month_name[i]: i for i in range(1, 13)}
selected_month = st.selectbox("Select Month", list(month_names.keys()))
selected_day = st.selectbox("Select Day", list(range(1, 32)))
selected_hour = st.selectbox("Select Hour (24-Hour Format)", list(range(0, 24)))
Received_Bank = st.selectbox("Select Bank", list(Bankoptions.keys()), key="received_bank")
Sender_Bank = st.selectbox("Select Bank", list(Bankoptions.keys()), key="sender_bank")

data = [Amount,
        month_names[selected_month],
        selected_day,
        selected_hour,
        Bankoptions[Received_Bank],
        Bankoptions[Sender_Bank],
        ]

if st.button("Submit"):
    res = postcall(data)
    Value = res.predictions[0]
    if Value == 1.0:
        st.toast('Transaction is successful!!', icon='🎉')
    else:
        st.toast("Transaction is not successful")
