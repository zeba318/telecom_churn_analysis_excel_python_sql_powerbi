# [Project Title]
> Telecom Customer Churn Analysis

---
## ⚙️ Project Type Flags

- [ ] Exploratory Data Analysis (EDA)
- [ ] SQL Analysis / Querying
- [ ] Dashboard / Data Visualization
- [ ] Data Cleaning / Wrangling
- [ ] End-to-End Project


---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Dataset info & Tools](#3-Dataset-info--tools)
4. [Repository Structure](#4-repository-structure)
5. [Project Workflow](#5-Project-workflow)
6. [Datamodel and schema](#6-datamodel-and-schema)
7. [Analysis & Metrics](#7-analysis--metrics)
8. [Key Insights](#8-key-insights)
9. [Recommendations](#9-recommendations)
10. [Future Enhancements](#10-future-enhancements)
11. [Conclusions](#11-Conclusions)
12. [Author](#12-author)

----

## 1. Project Overview

This Project Analyzes a telecom customer churn dataset to identify factors influencing customer attrition and evaluate overall customer retention performance the project includes data cleaning, preprocessing and exploratory data analysis (EDA) using python followed by SQL-based data analysis and an interactive power bi dashboard for business reporting. 

Problem statement: the Telecom Company is Experiencing Customer churn but lack clear insights into why customers are leaving. the Business needs to Analyze customer Demographic, service usage patterns, and billing information to identify factors contributing to churn and improve customer Retention.    

----
## 2. Objectives

the objective is to uncover churn patterns, measures key performance indicators (KPIS) and provide data-driven recommendations to help improve customer retention and support informed business decisions.

---
## 3. Dataset info & Tools

Name: Telecom Customer Churn
Source: Kaggle
No. of Rows: 7000
No. of Columns : 21 
Type: Customers Demographics, Service usage like Subscription, Billing info, Churn Status.
Target Variables: Churn (Yes/No) Indicating Whether a Customer Discontinued the Telecom Service.

### Tools & Technologies 

 Tool(s) Used 
 Excel, Python, SQL, Power BI
   
 Excel: Conducted initial data inspection and verified the dataset before analysis.
 Python: Data cleaning, Preprocessing and Performed (EDA).
 SQL: Data querying, aggregation, Group by and performed business Analysis.
 Power BI: Interactive Dashboard Creation and KPI cards Visualization.
 
----
## 4. Repository Structure

[project-root]/
│
├── data/
│   ├── raw/                  # Original, unmodified source data - never edited 
|   ├── processed/            # cleaned and tranformed data  
|                                       
├── notebooks/                # Jupyter,  notebooks
│
│
├── queries/                  # SQL files 
│   ├── transformation/       # presentation quesries                                             
│
├── reports/                  # Final outputs: PDFs, slide decks, Word docs
│
├── visuals/                  # Exported charts, dashboard screenshots, ERD diagrams
│
└── README.md                 # You are here

 ----
## 5. project  Workflow

  1. Source: "Collected the Telecom churn Dataset from Kaggle "
  2. Ingestion: "Loaded into Python using pandas, NumPy, Seaborn, Matplotlib."
  3. Cleaning: "Preprocessing and performed (EDA) to clean the Dataset."
  4. Transformation: "Created aggregation query ."
  5. Analysis: "Descriptive statistics, regional comparison, return rate
                segmentation by product category."
  6. Output: "Summary report (PDF), annotated notebook, processed csv".

---
## 6. Data Model & Schema

### Dataset / Table: `[name]`

| Field Name | Data Type | Description | Example Value |
|------------|-----------|-------------|---------------|
| [Customer id] | [string / Text] | [Unique identifier assigned to each customer.] | [7590-VHVEU] |
| [gender] | [string / Text] | [gender of the customer.] | [Female] |
| [Senior Citizen] | [int] | [Indicates whether the customer is a senior citizen.1=Yes, 0=No.] | [0] |
| [Partner] | [string / Text] | [Indicates whether the customer has a partner.] | [Yes] |
| [Dependents] | [string / Text] | [Indicates whether the customer has dependents.]  | [No] |
| [tenure] | [integer] | [Number of months the customer has been with the telecom company.] | [1] |
| [Phone Service] | [string / Text] | [indicates whether the customer has phone service.] | [No] |
| [Multiple Lines] | [string / Text] | [indicates whether the customer has multiple phone lines.] | [No phone Service] |
| [Internet Service] | [string / Text] | [Type of internet service used by the customer.] | [DSL] |
| [Online Security] | [string / Text] | [indicates whether the customer has security service.] | [No] |
| [Online Backup] | [string / Text] | [indicates whether the customer has online backup service.] | [Yes] |
| [Device Protection] [string / Text] |[indicates whether the customer has device protection service.] | [No] |
| [Tech Support] | [string / Text] | [indicates whether the customer has technical support service.] | [No] |
| [Streaming TV] | [string / Text] | [indicates whether the customer uses streaming TV service.] | [No] |
| [Streaming Movies] | [string / Text] | [indicates whether the customer uses streaming movie service.] | [No]|
| [Contract] | [string / Text] | [Type of contract selected by the customer.] | [Month-to-Month] |
| [Paperless Billing] | [string / Text] | [indicates whether the customer uses paperless billing] | [Yes] |
| [Payment Method] | [string / Text] | [payment method used by the customer.] | [Electronic check] |
| [Monthly Charges] | [Decimal / Float] | [Monthly amount charged to the customer.] | [29.85] |
| [Total Charges] | [Decimal / Float] | [Total amount charged to the customer during their tenure.] | [29.85] |
| [Churn] | [string / Text] | [indicates whether the customer left the company.] | [No] |


---
## 7. Analysis & Metrics

1.Analyzed the overall customer churn and Retention rate.
2.Analyzed churn patterns across different telecom partners.
3.Analyzed the impact of monthly charges and total charges on customer churn.
4.Analyzed the churn rate among senior citizens.
5.Analyzed the which contract type has a high churn rate.
6.Analyzed the which service type has a higher churn rate.
7.Analyzed the which streaming service has higher churn rate.
8.Analyzed which payment method has highest customer churn rate.
9.Identified Customer segment with higher churn rates and analyzed their characteristics.
10.Developed an interactive Power BI dashboard to monitor churn KPIS, customer segments, and churn trends.

### Key Metrics Defined
 [No. of churn and Retention customers] [Total Customer churn rate] [percentage of customer of Retention rate] [churn rate among seniorcitizen and non seniorcitizen]
 [customer churn rate differ by gender] [which gender has highest total monthly charges among churned customers] [which contract type has highest No. of customers]
 [which contract type has highest No. of churn rate] [which tenure group has highest no. of customers] [How customer tenure differ between churn and retention]
 [which internet service type has the highest customer churn rate] [churn rate among customers with and without multiple lines] 
 [phone service affects the customer churn rate] [online security affects the customer churn] [online backup affects the customer churn]
 [Device protection affects customer churn] [Tech support affects customer churn] [which streaming service has highest customer churn rate]
 [which payment method has highest customer churn rate] 
 
---
## 8. Key Insights
  
Insight 1: [26 % of Customers churned, while 74% were Retained.]
Insight 2: [Customers on month-to-month contracts showed higher churn, indicating that short-term contracts have a higher retention risk.]
Insight 3: [DSL internet service Customer showed higher churn, making this an important customer segment for retention strategies.]
Insight 4 : [Customer with long-term contracts were more likely to remain with the company compared with short-term contract customers.]
Insight 5 : [the analysis identified high-risk customer. segments that require targeted Retention strategies.]
Insight 6 : [Additional services such as online security and online backup can be used as Retention opportunities to increase customer engagement.]
Insight 7 :[the findings indicates that affordable long-term plans and targeted offers could help reduce customer churn.]
Insight 8: [the Power BI dashboard provides a centralized view of churn and Retention patterns, helping management make data-driven decisions.]
 
---
## 9. Recommendations

  1.Introduce 6-month contract plans with attractive pricing and Benefits to encourage customers to move from short-term contracts and reduce churn.
  2.Focus on DSL internet customers by providing targeted offers and improved service packages to increase customer retention.
  3.offer Bundled services such as online security and online backup at discounted prices to increase customer engagement and encourage long-term subscriptions.
  4.Introduce affordable DSL plans to attract new customers and make the service more competitive.
  5.provide targeted retention offers to customers who are at higher risk of churning based on their service usage and contract type.

--- 
## 10. Future Enhancements

- [ ] [Enhancement 1 - create a customer segmentation model based on contract type, services, tenure, and monthly charges.]
- [ ] [Enhancement 2 - Add Real-time Customer data to monitor churn trends continuously.]
- [ ] [Enhancement 3 - Build an automated early-warning system that alerts the business when customers show high risk churn patterns.]
- [ ] [Enhancement 4 - Compare churn and retention performance before and after implementing new 6-months plans and DSL offers.]
- [ ] [Enhancement 5- Analyze customer feedback and complaints using sentiments analysis to identify reasons for dissatisfaction.]
- [ ] [Enhancement 6- integrate data from multiple sources such as customer service, Billing, usage, and complaints for more comprehensive churn analysis.]

----
## 11. Conclusions

The Telecom churn Analysis Project Successfully analyzed customer rate, retention rate, and the services used by customers, including online security, onlinebackup,
Device protection, Tech support, and phone services. the project also focused on predicting customer churn using python, SQL, and Power BI. I cleaned and analyzed the data using EDA in python, performed business analysis using SQL, and created an interactive Power BI Dashboard to Visualize customer churn and identify 
data-driven insights. the insights and recommendations from this project can help improve customer retention, reduce churn, and increase overall customer satisfaction.

--- 
## 12. Author

 [Zeba Hajera]
      [Data Analyst]

- 🔗 [https://www.linkedin.com/in/zeba-hajera-3a437a366?utm_source=share_via&utm_content=profile&utm_medium=member_android] 
- 💼 [https://github.com/zeba318]
- 📧 [zebahajera715@gmail.com]
----


