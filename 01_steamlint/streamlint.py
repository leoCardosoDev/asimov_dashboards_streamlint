import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify songs'
)

df = pd.read_csv("01 Spotify.csv")
df.set_index('Track', inplace=True)
artists = df['Artist'].value_counts().index
artist = st.selectbox('Artista', artists)
df_filterd = df[df['Artist'] == artist]

st.bar_chart(df_filterd['Stream'])
st.write(artist)