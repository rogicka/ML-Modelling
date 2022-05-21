# Capstone Project Modul 3: Machine Learning

## Customer Analytics: Churn Prediction Using Machine Learning
Yosafat Rogika P S (JCDS JKT)

## Context
A telecommunications provider, Telco, is concerned about the number of customers who are switching from their company to competitor. They need to know who is leaving and why they are leaving. We will look at all relevant customer data and provide insights to the marketing department so they may create targeted customer retention strategies.

## Problem Statement :
**Churn** refers to customers or users who leave the services or migrate to a competitor in the industry. It is critical for any corporation to retain present customers while also attracting new ones; if one of them fails, the business suffers. Customer retention is several times less expensive than acquiring new consumers. Furthermore, even a small improvement in client retention raises sales and profits dramatically. 

## Goals :
As a result, the company wants to be able to predict whether or not a customer will / wants to leave the company. understanding which customers are more likely to switch to competitors and what variables contribute to this is critical for Telco. The company will be able to optimize its customer retention campaigns using this data.

![Confusion Matrix](https://user-images.githubusercontent.com/99156054/169649507-679d463a-d115-4f8e-b2e0-0a334979b41d.png)

Type 1 error : **False Positive**  
**consequence** : wasted retention costs, time and resources.

Type 2 error : **False Negative**  
**consequence** : lose the customer and will have to pay all the costs of acquiring a replacement customer, including foregone revenue, advertising costs, administrative costs, etc.

Given the consequences, what we will do as much as possible is build a model that reduces customer loss because it costs much less to retain an existing customer than it is to acquire a new customer, maintaining a healthy customer base is critical. for the success of any business.

So we will focus on the FN value, by obtaining a high recall value. But we also don't want to ignore the results of small precision. Therefore, we need to balance the recall value and its precision. So the main metric that we will use is the f1-score for the model whose data is still imbalanced, and when we do oversampling (SMOTE) we will use the default(accuracy)&/ roc_auc metric. Where the results of the two will be compared to get the most optimal model for this case.

## Attributes Information
There are **4930 rows** of data in this dataset, with **11** columns containing information about customer data that uses telecommunications services.
### Prediction column:
1. `Churn`: Whether the customer churned or not (Yes or No)
### Two numerical columns:
2. `Tenure`: Number of months the customer has stayed with the company
3. `MonthlyCharges`: The amount charged to the customer monthly
### Eight categorical columns:
4. `Dependents`: Whether the customer has dependents or not (Yes, No)
5. `OnlineSecurity`: Whether the customer has online security or not (Yes, No, No internet service)
6. `OnlineBackup`: Whether the customer has an online backup or not (Yes, No, No internet service)
7. `InternetService`: Customer’s internet service provider (DSL, Fiber optic, No)
8. `DeviceProtection`: Whether the customer has device protection or not (Yes, No, No internet service)
9. `TechSupport`: Whether the customer has tech support or not (Yes, No, No internet service)
10. `Contract`: The contract term of the customer (Month-to-month, One year, Two years)
11. `PaperlessBilling`: Whether the customer has paperless billing or not (Yes, No)

![image](https://user-images.githubusercontent.com/99156054/169649544-0b0bae83-963d-4eb8-acb3-b0df2e809fc2.png)

![image](https://user-images.githubusercontent.com/99156054/169649563-1c0a50c2-000b-4340-9c5d-112876057e6e.png)

![image](https://user-images.githubusercontent.com/99156054/169649598-8c67172a-d851-4500-9d3f-2cc628628f8c.png)
![image](https://user-images.githubusercontent.com/99156054/169649626-49d804e3-73bb-4400-992e-40e31032f09a.png)


### Base Modelling Evaluation Matrix
![image](https://user-images.githubusercontent.com/99156054/169649651-d9bb7d31-e155-4671-918d-f83178c6ca80.png)

### Oversampling Data Modelling Evaluation Matrix
![image](https://user-images.githubusercontent.com/99156054/169649689-e0856cd3-4fd2-4dcb-a5aa-2e4147071ce2.png)

#### Logistic Regression Hyperparameter Tuning report and confusion matrix
![image](https://user-images.githubusercontent.com/99156054/169649726-f13ea8d3-3ff3-4845-a735-5de9f8f980d2.png)

#### XGboost Hyperparameter Tuning Report and confusion matrix
![image](https://user-images.githubusercontent.com/99156054/169649762-36f96381-fe93-4687-976f-a66fde17086b.png)

## Model Evaluation & Cost Evaluation
We assume the cost of acquiring new customers is up to **5 times higher** than the cost of retaining them. 

So, I made the following cost assumptions to explore the cost implications of implementing the model.
- I assigned the **true negatives the cost 0 cost**. 
- False negatives were the most damaging, as they predicted falsely that a churning consumer would stay. I will lose the customer and will be responsible for any costs associated with finding a replacement, including lost revenue, advertising costs, administrative fees, and so on. **I will assume 5 * cost. This is the cost of false negatives.**
- Finally, for customers that my model identifies as churning (True Positives & False Positives), **I will assume 1 * cost(TP & FP)**

So, we will have an equation to describe the cost. Our goals is to minimize the cost :

\begin{equation}
Cost(c) = 5*(c)*FN + 1*(c)*(TP + FP) + 0*(c)*TN 
\end{equation}

## Cost Comparison
![image](https://user-images.githubusercontent.com/99156054/169649820-64c7f22f-f542-43db-8160-fea5a445ba41.png)

## Conclusion & Recommendation
# Conclusion & Recommendation
- Conclusion:
    1. From the analysis that has been described, the appropriate model for this case is **Logistic Regression** which has been performed with **hyperparameter tuning.**
    2. The best Hyperparameter values are as follows: 
        **{'C': 0.1, 
        'penalty': 'l2'}**
    3. **Recall** and **Precision** values respectively (based on the recall class(+)) are **81%** and **52%**.
    4. For the scenarios that have been made, the model is **able to save costs up to 50% of the total cost** if the model is not implemented.
    

- Recommendation:
    1. The implementation of the Model is limited to cases when the resulting cost for customer churn is approximately 5 times greater than the retention cost. Outside of this case the confidence of the model used will be different (low p-value), because the ability of the model will depend on the evaluation matrix that will be used in the cost formula.
    2. Adding features in feature selection such as the payment method used, streaming services, or other matters related to the telecommunication service domain.
    3. Try a combination of feature engineering and modelling other Machine Learning algorithms.
    4. Conduct a more in-depth data analysis for data that was mispredicted by the model (FP & TP) in order to know its characteristics. 
    



