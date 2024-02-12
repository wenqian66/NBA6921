#suppose threshold x %in% seq(0,1,by = 0.1) c(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
#if score>=x,reject(LOAN_AMOUNT=0);if score<x,approve(LOAN_AMOUNT=loan_amount)
#rm score >=x
#in the remain if DID_CONSUMER_DEFAULT?=1, add (-LOAN_AMOUNT);if DID_CONSUMER_DEFAULT?=0,add (LOAN_AMOUNT*3%)
#sum (-LOAN_AMOUNT) as cost;sum (LOAN_AMOUNT*3%) as benefits
import numpy as np
import pandas as pd
df = pd.read_csv("~/Desktop/M1A_ Mortgage Risk Score Dataset.csv")

def net_benefits_calculate(df):
    for x in np.arange(0.1,1.1,0.1):
        x_total_cost = 0
        x_total_benefit = 0

        for index,row in df.iterrows():
            AI_RISK_SCORE = row['AI_RISK_SCORE']
            LOAN_AMOUNT = row['LOAN_AMOUNT']
            DID_CONSUMER_DEFAULT = row['DID_CONSUMER_DEFAULT?']
            
            if AI_RISK_SCORE<x:
                    if DID_CONSUMER_DEFAULT == 1:
                        x_total_cost -= LOAN_AMOUNT
                    else:
                        x_total_benefit += LOAN_AMOUNT*0.03
            x_net_benefits = x_total_benefit + x_total_cost

        print(f"Threshold: {x:.1f}, Total Cost: {x_total_cost}, Total Benefit: {x_total_benefit}, Total Benefits: {x_net_benefits}")

net_benefits_calculate(df)
