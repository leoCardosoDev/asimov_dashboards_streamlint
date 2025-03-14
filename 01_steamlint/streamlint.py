import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify Songs'
)

df = pd.read_csv("01 Spotify.csv")
df.set_index('Track', inplace=True)

artists = df['Artist'].value_counts().index
artist = st.selectbox('Artista', artists)
df_filtered_artist = df[df['Artist'] == artist]

albuns = df_filtered_artist['Album'].value_counts().index
album = st.selectbox('Album', albuns)
df_filtered_album = df[df['Album'] == album]

display = st.checkbox('Mostrar')
if display:
    st.bar_chart(df_filtered_album['Stream'])

st.write(artist)