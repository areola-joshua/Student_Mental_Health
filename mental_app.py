#step 1

import numpy as np
import pandas as pd
import streamlit as st 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns 

#title of the project  smileyes, emojis (css)
st.title(":clap: Student Health Analysis :smile:")
st.markdown('---')

#assignment : about
st.write("""
         :open_mouth: About student gfhfhggfdjhhgfh
         """)
#file upload
st.sidebar.header('upload Dataset')
uploaded_file = st.sidebar.file_uploader('choose a `csv` file')