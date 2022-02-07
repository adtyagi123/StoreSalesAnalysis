#Libraries to run the app
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


#Creating single source data for the app
#Reference: https://www.iea.org/articles/global-ev-data-explorer


data = pd.read_csv('RawData.csv')
data.columns = [c.replace(' ', '_') for c in data.columns]


#Header and description for the app
st.title('Super Market Data Analysis')

st.markdown("""
This app provides insights on 3 branches of a supermarket.
* **Python libraries: ** pandas, plotly, streamlit
* **Datasource: ** [Kaggle Supermarket Sales Data](https://www.kaggle.com/aungpyaeap/supermarket-sales)
""")




st.subheader('Category against gender')
st.markdown("""
Bar chart Analysis of different categories against gender.
""")
input_parameter = st.selectbox('Category', ['Branch', 'Product_line', 'Payment', 'Customer_type'])

df_gender = data.groupby(by=[input_parameter, "Gender"]).size().reset_index(name="counts")
fig_gender = px.bar(df_gender, y=input_parameter, x='counts', color = 'Gender', barmode = 'group', text = 'Gender')
st.plotly_chart(fig_gender, use_container_width = True)


#Sales related Analysis
st.subheader('Sales Analysis')
st.markdown("""
Sales and Ratings Analysis for the branches.
""")
data['Hour'] = pd.to_datetime(data['Time']).dt.hour
fig = plt.figure(figsize=(8, 6))
sns.lineplot(x="Hour",  y = 'Quantity',data =data).set_title("Product Sales per Hour")
st.pyplot(fig)

st.markdown("""
Branch based sales and rating analysis for member VS normal customers
""")
input_boxPlot = st.selectbox('Sales Analysis', ['Rating', 'gross_income', 'Total'])

fig_boxPlot = px.box(data, x="Branch", y=input_boxPlot, color = 'Customer_type')
st.plotly_chart(fig_boxPlot, use_container_width = True)


# if st.button('Show EV Charger Analysis'):
