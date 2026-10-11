# Export the pickles to the published csv.gz files (run in the study-2 work dir)
import pandas as pd
d=pd.read_pickle('players.pkl')
for s,x in d.groupby('season'): x.to_csv(f'player_week_{s}.csv.gz',index=False)
P=pd.read_pickle('pairs.pkl')
for s,x in P.groupby('season'): x.to_csv(f'close_pairs_{s}.csv.gz',index=False)
