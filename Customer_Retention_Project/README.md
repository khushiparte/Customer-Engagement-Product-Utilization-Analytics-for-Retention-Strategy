# Customer Engagement & Product Utilization Analytics for Retention Strategy

## Overview

This project analyzes customer engagement, product utilization, and behavioral patterns to identify factors affecting customer retention and churn.

The solution combines exploratory data analysis, feature engineering, customer segmentation, machine learning, and dashboard visualization to support customer retention strategies.

---

## Business Problem

Banks often focus on financial indicators such as account balance and salary when evaluating customer value.

However, many customers churn despite having:

- High balances
- Good credit scores
- Long relationships

The project investigates how engagement and product usage influence customer retention.

---

## Objectives

- Analyze engagement-driven churn behavior
- Measure retention impact of product utilization
- Identify high-value disengaged customers
- Create customer segments
- Build churn prediction models
- Develop an interactive analytics dashboard

---

## Dataset

**Dataset:** European Bank Customer Dataset

Features include:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Ownership
- Active Membership
- Estimated Salary
- Churn Status (Exited)

Dataset Size:

- 10,000 Customers
- 14 Features

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## Methodology

### 1. Data Preprocessing

- Missing value validation
- Duplicate checking
- Feature selection
- Data cleaning

### 2. Exploratory Data Analysis

Analysis performed on:

- Churn distribution
- Engagement vs churn
- Product utilization vs churn
- Balance vs churn
- Geography vs churn
- Gender vs churn

### 3. Feature Engineering

Created custom features:

#### Engagement Score

Based on:

- Active Membership
- Credit Card Ownership
- Product Usage
- Tenure

#### Product Depth Index

Measures product adoption depth.

#### Relationship Strength Score

Combines:

- Engagement Score
- Product Depth Index

#### High Value Disengaged Flag

Identifies customers with:

- Balance > 100,000
- Low engagement

### 4. Customer Segmentation

Customers classified into:

- Highly Engaged
- Silent Risk
- Low Product User
- Moderate

### 5. Machine Learning

Model Used:

- Random Forest Classifier

---

## Results

### Key Metrics

| Metric | Value |
|----------|----------|
| Total Customers | 10,000 |
| Churn Rate | 20.37% |
| Active Customers | 5,151 |
| Average Products | 1.53 |

---

### Customer Segmentation

| Segment | Customers |
|----------|----------|
| Low Product User | 3,507 |
| Highly Engaged | 2,588 |
| Silent Risk | 2,356 |
| Moderate | 1,549 |

---

### High Value Customer Analysis

| Metric | Value |
|----------|----------|
| High Value Disengaged Customers | 1,211 |

---

### Machine Learning Performance

| Metric | Value |
|----------|----------|
| Accuracy | 86.95% |

#### Classification Report

| Class | Precision | Recall | F1-Score |
|----------|----------|----------|----------|
| Retained | 0.89 | 0.96 | 0.92 |
| Churned | 0.76 | 0.49 | 0.60 |

---

## Important Insights

- Inactive customers exhibit significantly higher churn.
- Multi-product customers show stronger loyalty.
- High account balances do not guarantee retention.
- Relationship strength positively influences retention.
- Customer engagement is a major predictor of churn.

---

## Dashboard Features

### KPI Dashboard

- Total Customers
- Churn Rate
- Active Customers
- Average Products

### Customer Analytics

- Churn Distribution
- Engagement vs Churn
- Product Utilization Analysis
- Balance Distribution

### Customer Segmentation

- Segment Distribution
- Relationship Strength Analysis

### High Value Customer Detection

- High-value disengaged customer table

### Interactive Filters

- Geography
- Gender

---

## Business Impact

- Improved customer retention strategy
- Better customer segmentation
- Early identification of churn risk
- Targeted engagement campaigns
- Enhanced customer lifetime value

---

## Future Enhancements

- Deep Learning Models
- Real-Time Churn Prediction
- Personalized Recommendation Engine
- CRM Integration
- Automated Retention Campaigns
- Cloud Deployment

---

## Author

Khushi Parte

M.Sc. Data Science
