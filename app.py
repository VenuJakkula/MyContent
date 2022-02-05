import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('venu.jpg')


st.title('Welcome World!')

# My Image
st.image(image, caption='This is me in building the project')

st.subheader('My Home Map')
my_loc = pd.DataFrame({"lat":[17.50609218738898], "lon": [78.408759753968]})

st.map(my_loc)


st.header('Electricity Bill Essentials')

#st.text("[Pay Electricity Bill](https://paytm.com/electricity-bill-payment/telangana/telangana-state-southern-power-distribution-company-ltd-tsspdcl)")

url = "https://paytm.com/electricity-bill-payment/telangana/telangana-state-southern-power-distribution-company-ltd-tsspdcl"

option_usc = st.selectbox(
     'Select The Floor and Copy the USC Number to pay the Electricity Bill on Paytm',
     ('Ground Floor', 'First Floor', 'Second Floor', 'Third Floor'))

usc_no = {'Ground Floor':'TBD', 'First Floor':'112595405', 'Second Floor':'113095576', 'Third Floor':'111305145'}
st.write('Copy this %s USC Number and '%usc_no[option_usc])

#st.write("[Pay Electricity Bill here](%s)" % url)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
