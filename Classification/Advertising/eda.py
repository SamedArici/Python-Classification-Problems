import matplotlib.pyplot as plt
import seaborn as sns

def boxPlot(df):

    plt.figure(figsize = (15,8))

    numerical_cols= ['daily time spent on site','daily internet usage','area income','age']   
    
    for i,col in enumerate(numerical_cols,start=1):
        plt.subplot(2,2,i)
        sns.boxplot(x = 'clicked on ad', y = col, data = df, palette = 'coolwarm_r')
    plt.subplots_adjust(left = 0.1,right=0.9,wspace=0.4,hspace=0.4)
    
    
def cal(df):
    numerical_cols= ['daily time spent on site','daily internet usage','area income','age']   
    print('Clicked on Ad Rates'.center(50,'_'))
    
    for col in numerical_cols:
        print('\n')
        print(f'{col} <= mean - std: {round(df[df[col] <= df[col].mean() - df[col].std()]["clicked on ad"].mean()*100,2)}%')
        print(f'{col} <= mean: {round(df[df[col] <= df[col].mean()]["clicked on ad"].mean()*100,2)}%')
        print(f'{col} >= mean: {round(df[df[col] >= df[col].mean()]["clicked on ad"].mean()*100,2)}%')
        print(f'{col} >= mean + std: {round(df[df[col] >= df[col].mean() + df[col].std()]["clicked on ad"].mean()*100,2)}%')
        

def linePlot(df):
    plt.figure(figsize = (15,8))
    
    df['months'] = df['timestamp'].apply(lambda x: x.month)
    df['days'] = df['timestamp'].apply(lambda x: x.day)
    df['hours'] = df['timestamp'].apply(lambda x: x.hour) 
    
    date_columns = ['months','hours','days']
    
    for i,col in enumerate(date_columns,start=1):
        plt.subplot(2,2,i)
        sns.lineplot(df.groupby(col)['clicked on ad'].sum())
        plt.xlabel(col,size = 14)
        plt.ylabel('clicked on ad',size = 14)
        plt.xticks(size = 12)
        plt.yticks(size = 12)
    
    plt.suptitle('Sum of Clicked on Ad',size = 16)
    plt.subplots_adjust(left = 0.1,right=0.9,wspace=0.4,hspace=0.4)