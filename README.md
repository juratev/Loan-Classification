# Loan-Classification
Classifying loans into accepted or rejected, predicting loan grade.

Project completed on **May 12, 2023.**

### About the dataset
The dataset consists of loan data from LendingClub. It is obtained from a publicly accessible source and includes two separate datasets. <br>
<a href="https://storage.googleapis.com/335-lending-club/lending-club.zip"> the link to the dataset </a>  <br> 
The dataset for accepted loans contains 2.2 million records and encompasses 151 features. <br>
The dataset for rejected loans contains 27.6 million records and includes 9 features.

### Project goal
The goal of this project is to explore and analyze the loan data from LendingClub and use the insights to accomplish three main tasks:
* Classification of loans into accepted or rejected
* Classification of loan grades
* Predict the interest rate (regression task)

### Project Outline

#### Pre-processing data using PySpark. 
Removing some features and faulty records, inputting missing values, and transforming the data for EDA and prediction. <br>
Ultimately, I produce two datasets - smaller for loan status prediction and bigger for loan grade and interest rate prediction.

#### EDA of loan status dataset.
Exploring categoric and numeric variables and their relation with loan status feature. <br>
Performing a z-test on numeric variables to determine which of them have predictive value.

#### EDA of loan grade dataset.
Exploring categoric and numeric variables and their relation with grade feature. <br>
Performing $\chi^2$ test to determine if there is a relationship between grade and categorical features. <br>
I am performing the Anova-F test to find the most important numeric features.

#### Modeling
*   Loan status prediction
*   Loan grade prediction
*   Loan interest rate prediction
