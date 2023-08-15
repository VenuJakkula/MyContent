import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import webbrowser
import base64
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av

image = Image.open('venu.jpg')


st.title('Welcome World!')

# My Image
st.image(image, caption='This is me in building the project')

st.subheader('My Home Map')
my_loc = pd.DataFrame({"lat":[17.50609218738898], "lon": [78.408759753968]})

st.map(my_loc)


st.header('Electricity Bill Essentials')

#st.text("[Pay Electricity Bill](https://paytm.com/electricity-bill-payment/telangana/telangana-state-southern-power-distribution-company-ltd-tsspdcl)")

url = "https://www.google.com/"

option_usc = st.selectbox(
     'Select The Floor and Copy the USC Number to pay the Electricity Bill on Paytm',
     ('Ground Floor', 'First Floor', 'Second Floor', 'Third Floor','Shop'))

usc_no = {'Ground Floor':'113095577', 'First Floor':'112595405', 'Second Floor':'113095576', 'Third Floor':'111305145','Shop':'107922449'}
st.write('Copy this USC Number: **%s**  and [Pay Electricity Bill here](%s)'%(usc_no[option_usc],url))

#st.write("[Pay Electricity Bill here](%s)" % url)
st.code ('%s'%usc_no[option_usc])
if st.button('Pay Electricity Bill'):
    webbrowser.open_new_tab(url)


link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")
		#faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)
		#for x,y,w,h in faces:
		#	cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)
		#cv2.putText(img=frm, text='Hello', org=(150, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)
