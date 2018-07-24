sample_bets=pd.read_csv("sample_bets.csv")
sample_bets['Line']=sample_bets['Line']+100
sample_bets['Total']=sample_bets['Total']+100

class Kelly_Criterion():
    def __init__(self):
        pass
    #positive line bets 
    def kelly_criterion_underdog(self,df):
        #convert odds to decimal odds
        B=(df['Total']/100)+1
        P=1-df['P']
        Q=1-P 
        BP=B*P
        return (BP-Q)/B 
    #negative line bets 
    def kelly_criterion_favorite(self,df):
        #convert odds to decimal odds
        B=(100/df['Line'])+1
        P=df['P']
        Q=1-P 
        BP=B*P
        return (BP-Q)/B 

kelly_criterion=Kelly_Criterion()
underdog=kelly_criterion.kelly_criterion_underdog(sample_bets)
favorite=kelly_criterion.kelly_criterion_favorite(sample_bets)