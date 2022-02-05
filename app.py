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
st.text("[Pay Electricity Bill](https://paytm.com/electricity-bill-payment/telangana/telangana-state-southern-power-distribution-company-ltd-tsspdcl)")
