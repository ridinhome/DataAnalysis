import pandas as pd

def fredrequests(series,api):
    name = series
    key = api
    url = ("https://api.stlouisfed.org/fred/series/observations?series_id="+name+"&realtime_end=9999-12-31&api_key="+key+"&file_type=json")
    df = pd.read_json (url)
    new_df = df['observations'].apply(pd.Series)
    new_df.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
    new_df.set_index("date")
    return new_df
