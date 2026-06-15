import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Retention Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

h1 {
    color: #1E3A5F;
    font-weight: 800;
}

h2, h3 {
    color: #1E3A5F;
}

[data-testid="stMetricValue"] {
    font-size: 32px;
    font-weight: bold;
    color: #1E3A5F;
}

.css-1d391kg {
    background-color: #FFFFFF;
}

div[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("../data/European_Bank.csv")

# ---------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------

df['EngagementScore'] = (
    df['IsActiveMember'] * 40 +
    df['HasCrCard'] * 20 +
    df['NumOfProducts'] * 10 +
    df['Tenure'] * 3
)

df['ProductDepthIndex'] = (
    df['NumOfProducts'] * 25
)

df['RelationshipStrength'] = (
    df['EngagementScore'] +
    df['ProductDepthIndex']
)

df['HighValueDisengaged'] = np.where(
    (df['Balance'] > 100000) &
    (df['IsActiveMember'] == 0),
    1,
    0
)

# ---------------------------------------------------
# CUSTOMER SEGMENTATION
# ---------------------------------------------------

def segment_customer(row):

    if row['IsActiveMember']==1 and row['NumOfProducts'] >= 2:
        return "Highly Engaged"

    elif row['IsActiveMember']==0 and row['Balance'] > 100000:
        return "Silent Risk"

    elif row['NumOfProducts']==1:
        return "Low Product User"

    else:
        return "Moderate"

df['CustomerSegment'] = df.apply(segment_customer, axis=1)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title(" Filters")

geo = st.sidebar.multiselect(
    "Select Geography",
    options=df['Geography'].unique(),
    default=df['Geography'].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

filtered_df = df[
    (df['Geography'].isin(geo)) &
    (df['Gender'].isin(gender))
]

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Customer Engagement & Retention Analytics")

st.markdown("""
Analyze customer engagement, product utilization,
and behavioral churn patterns for retention strategy optimization.
""")

st.markdown("---")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_customers = len(filtered_df)

churn_rate = filtered_df['Exited'].mean() * 100

active_customers = filtered_df['IsActiveMember'].sum()

avg_products = filtered_df['NumOfProducts'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", f"{total_customers}")

with col2:
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

with col3:
    st.metric("Active Customers", f"{active_customers}")

with col4:
    st.metric("Avg Products", f"{avg_products:.2f}")

st.markdown("---")

# ---------------------------------------------------
# ROW 1
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Customer Churn Distribution")

    fig1 = px.histogram(
        filtered_df,
        x='Exited',
        color='Exited',
        color_discrete_sequence=['#4F46E5', '#EF4444']
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.subheader("Engagement vs Churn")

    fig2 = px.histogram(
        filtered_df,
        x='IsActiveMember',
        color='Exited',
        barmode='group',
        color_discrete_sequence=['#10B981', '#EF4444']
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# ROW 2
# ---------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    st.subheader("Product Utilization Analysis")

    fig3 = px.histogram(
        filtered_df,
        x='NumOfProducts',
        color='Exited',
        barmode='group',
        color_discrete_sequence=['#3B82F6', '#EF4444']
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    st.subheader("Balance Distribution")

    fig4 = px.box(
        filtered_df,
        x='Exited',
        y='Balance',
        color='Exited',
        color_discrete_sequence=['#6366F1', '#EF4444']
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------
# CUSTOMER SEGMENTS
# ---------------------------------------------------

st.markdown("---")

col5, col6 = st.columns(2)

with col5:

    st.subheader("Customer Segmentation")

    segment_data = filtered_df['CustomerSegment'].value_counts().reset_index()

    segment_data.columns = ['Segment', 'Count']

    fig5 = px.pie(
        segment_data,
        names='Segment',
        values='Count',
        hole=0.4
    )

    st.plotly_chart(fig5, use_container_width=True)

with col6:

    st.subheader("Relationship Strength Analysis")

    fig6 = px.histogram(
        filtered_df,
        x='RelationshipStrength',
        color='Exited',
        color_discrete_sequence=['#0EA5E9', '#EF4444']
    )

    st.plotly_chart(fig6, use_container_width=True)

# ---------------------------------------------------
# HIGH RISK CUSTOMERS
# ---------------------------------------------------

st.markdown("---")

st.subheader("⚠ High Value Disengaged Customers")

risk_customers = filtered_df[
    filtered_df['HighValueDisengaged'] == 1
]

st.dataframe(risk_customers.head(15))

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.markdown("---")

st.subheader(" Business Insights")

st.success("""
✔ Customers with low engagement show significantly higher churn.

✔ Multi-product customers demonstrate stronger loyalty.

✔ High-balance inactive customers represent premium churn risk.

✔ Relationship strength scores strongly correlate with retention.
""")