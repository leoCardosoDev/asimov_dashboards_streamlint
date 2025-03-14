import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout='wide',
    page_title='Spotify Songs'
)

@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(20) # apenas simula uma requisição muito grande
    return df
    
df = load_data()
st.session_state['df_spotify'] = df
df.set_index('Track', inplace=True)

artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('Artista', artists)
df_filtered_artist = df[df['Artist'] == artist]

albuns = df_filtered_artist['Album'].value_counts().index
album = st.selectbox('Album', albuns)
df_filtered_album = df[df['Album'] == album]

#display = st.checkbox('Mostrar')
#if display:
#    st.bar_chart(df_filtered_album['Stream'])

# col1, col2 = st.columns(2)

col1, col2 = st.columns([0.7, 0.3])
col1.bar_chart(df_filtered_album['Stream'])
col2.line_chart(df_filtered_album['Danceability'])
st.write(artist)
st.sidebar.button('Teste')