import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))
results = spotify.artist_top_tracks(lz_uri)

canciones=[]
popularidad=[]
duracion=[]



for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    canciones.append(track['name'])
    popularidad.append(track['popularity'])
    duracion.append(track['duration_ms']/(1000*60)%60)

df=pd.DataFrame()

df['Canciones']=pd.DataFrame(canciones)
df['Popularidad']=pd.DataFrame(popularidad)
df['Duracion']=pd.DataFrame(duracion)
df.index +=1

print(df)

scatter = sns.scatterplot(data = df, x = "Popularidad", y = "Duracion")
fig = scatter.get_figure()
fig.savefig("scatter_plot.png")

print('No hay relacion entre la duracion y la popularidad. Tal como se ve en el scatter, las dos canciones mas populares tienen una duracion muy distinta')

    
