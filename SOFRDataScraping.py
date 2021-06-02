import pandas as pd

def fredrequests (series,api,startdate="1776-07-04",enddate="9999-12-31"):
    """Returns a data series from the FRED database using the JSON API. Pass start date and end-date
    in yyyy-mm-dd format. Leaving out start date and end date defaults to full series."""
    name = series
    key = api
    start = startdate
    end = enddate
    url = ("https://api.stlouisfed.org/fred/series/observations?series_id="+name+"&realtime_start="
           +start
           +"&realtime_end="+end
           +"&api_key="+key+"&file_type=json")
    df = pd.read_json (url)
    new_df = df['observations'].apply(pd.Series)
    new_df.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
    new_df.set_index("date")
    return new_df
