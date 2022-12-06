from sklearn.model_selection import cross_val_score,GridSearchCV
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score
import pandas as pd

def grid_search(parameters,classifier,algorithmName,X_train,y_train):
    
    # add the parameters to the grid_search
    grid_search = GridSearchCV(
    estimator=classifier,
    param_grid=parameters,
    scoring='accuracy',
    cv=10,
    n_jobs = -1 #optional
    )
    
    # fit the gird_search
    grid_search.fit(X_train,y_train)

    # calculate scores
    best_accuracy = grid_search.best_score_
    best_parameters = grid_search.best_params_

    # print scores
    print(algorithmName.center(50,'_'))
    print(f'Best Parameters: {best_parameters}\n\n')   
    
    
    
def calculate_scores(classifier,algorithmName,df_result,index,X_train,y_train,X_test,y_test):
    
    y_pred = classifier.predict(X_test)
    
    acc = round(accuracy_score(y_test,y_pred),3)
    precision = round(precision_score(y_test,y_pred),3)
    recall = round(recall_score(y_test,y_pred),3)
    
    cvs = cross_val_score(estimator=classifier,X = X_train, y = y_train,cv = 5)
    cvs_mean = round(cvs.mean(),3)
    cvs_std = round(cvs.std() *100,3)
    
    tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()
    
    d = {'Algorithm':algorithmName,'Accuracy':acc,'Precision':precision,'Recall':recall,'cvs mean':cvs_mean,
         'cvs std (%)':cvs_std,'TP':tp,'TN':tn,'FP':fp,'FN':fn}
    
    new_df = pd.DataFrame(data = d,index = [index])
    df_result = pd.concat([df_result,new_df])
    index += 1
    return df_result,index