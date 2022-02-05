import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('venu.jpg')


st.title('Welcome World!')

# My Image
st.image(image, caption='This is me in building the project')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data = load_data(10000)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Map')
my_loc = pd.DataFrame({"Latitude":[17.50609218738898],"Longitude": [78.408759753968]})
#st.map(my_loc)

st.text(data)
