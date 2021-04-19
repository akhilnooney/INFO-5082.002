import pandas as pd
import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
df=pd.read_csv("C:\Windows\System32\Intern\sentiment_data.csv")
df2=pd.read_csv("C:\Windows\System32\Intern\Sentiment_Emotions (1).csv")

#A@st.cache(suppress_st_warning=True)
def main():
    st.title("Medicine Recommendation")
    activities=["Drug_Recommendation","About_Drug"]
    choice=st.sidebar.selectbox("Select Activity",activities)
    if choice=="Drug_Recommendation":
        condition_list=list(df["condition"].unique())
        #condition_list[0:0] = ["option"]
        result=st.selectbox("Select your condition",condition_list)
        st.write(f"Condition you choosen : {result}")
        input_condition = result
        cond_filtered = df[df['condition'] == input_condition]
        cond_filtered = cond_filtered.groupby(['condition','drugName']).agg('mean').sort_values(['Sentiment'],ascending=False)
        cond_filtered=cond_filtered.reset_index()
        cond_filtered["drugName"].head(5)
        st.write(cond_filtered["drugName"].head(5))
        fig,ax= plt.subplots(figsize=(10,5))
        sns.barplot(cond_filtered["drugName"].head(5),cond_filtered["Sentiment"].head(5))
        st.pyplot(fig)
    if choice=="About_Drug":
        Drug_list=list(df2["drugName"].unique())
        result_drug=st.selectbox("Select Drug",Drug_list)
        result=df2[df2["drugName"]==result_drug].sort_values(by="usefulCount", ascending=False).iloc[0,15:25]
        fig,ax= plt.subplots(figsize=(10,5))
        sns.barplot(result.index,result.values)
        st.pyplot(fig)



if __name__=='__main__':
    main()
