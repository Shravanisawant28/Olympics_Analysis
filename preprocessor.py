import pandas as pd

def preprocess(df,region_df):
    
    df=df[df['Season']=='Summer'] #keep only summer data no winter
    df=df.merge(region_df,on='NOC',how='left')#merge both datasest
    df.drop_duplicates(inplace=True)#remove duplicate data
    df=pd.concat([df,pd.get_dummies(df['Medal']).astype(int)],axis=1)

    return df
