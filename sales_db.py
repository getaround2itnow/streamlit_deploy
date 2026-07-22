import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
 
# Sample dataset (replace with real sales data)
 
@st.cache_data
def load_data():
    url = "https://powerbidocs.com/wp-content/uploads/2019/11/Global-Superstore.csv"
    df = pd.read_csv(url, encoding='latin1')
    return df

df = load_data()
    
# Convert 'Order Date' to datetime (specify format)
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%m/%d/%Y", errors='coerce')
df = df.dropna(subset=['Order Date'])

# Extract Year for Sidebar
df['Year'] = df['Order Date'].dt.year.astype(str)

# Sidebar filters
st.sidebar.header("Filters")
year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
region = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())

# Filter Data
filtered_df = df[(df['Year'] == year) & (df['Region'].isin(region))]

# KPIs
total_sales = int(filtered_df["Sales"].sum())
total_profit = int(filtered_df["Profit"].sum())
total_customers = filtered_df["Customer ID"].nunique()

st.title("Sales Dashboard")    
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Sales", f"${total_sales:,.2f}")
kpi2.metric("Total Profit", f"${total_profit:,.2f}")
kpi3.metric("Unique Customers", total_customers)

st.markdown("--------------------")

col1, col2 = st.columns([2, 1])

with col1:
    sales_trend = (
        filtered_df.groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )
    sales_trend['Order Date'] = sales_trend['Order Date'].dt.to_timestamp()
    fig = px.line(sales_trend, x='Order Date', y="Sales", title="Monthly Sales Trend")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    top_products = (
        filtered_df.groupby("Product Name")["Sales"]
        .sum()
        .nlargest(5)
        .reset_index()
    )
    
    fig2 = px.bar(top_products, x="Sales", y="Product Name", orientation="h", title="Top 5 Products")
    st.plotly_chart(fig2, use_container_width=True)