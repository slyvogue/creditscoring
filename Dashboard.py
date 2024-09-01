import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats

def calculate_low_credit_rate(df):
    low_credit_rate = len(df[df['Credit_Score'] < 600]) / len(df) * 100
    return f"{low_credit_rate:.2f}%"

def app(df, st):
    # Ensure Credit_Score is numeric
    df['Credit_Score'] = pd.to_numeric(df['Credit_Score'], errors='coerce')

    # Metrics
    st.title("Credit Score Analytics Dashboard")


    # Show Sample Data
    if st.button("Show Sample Data"):
        st.dataframe(df.sample(5))

    # Bar Plots
    st.header("Counts and Distributions")
    c1, c2 = st.columns(2)
    selected = c1.selectbox('Select Feature to Display', ['Occupation', 'Payment_Behaviour', 'Credit_Mix', 
                                                        'Monthly_Balance', 'Annual_Income'])
    colored = c2.selectbox('Color By', ['Payment_Behaviour'])

    # Check if selected feature and colored feature are the same
    if selected == colored:
        st.warning("Visualization Error: The selected feature and color feature must be different. Please select distinct features for accurate visualization.")
    else:
        subData = df.groupby([selected, colored])['Age'].count().reset_index(name='Counts')
        fig = px.bar(subData, x=selected, y="Counts", color=colored, template='plotly_dark',
                        title=f"{selected} Distribution Colored by {colored}")
        fig.update_layout(xaxis_title=selected, yaxis_title='Counts')
        st.plotly_chart(fig, use_container_width=True)


    # Box Plots
    st.header("Credit Score Distribution Across Features")
    cc1, cc2, cc3 = st.columns(3)

    Numerical = cc1.selectbox('Numerical Feature', ['Annual_Income', 'Monthly_Balance'])
    Category = cc2.selectbox('Categorical Feature', ['Occupation', 'Payment_Behaviour', 'Credit_Mix'])
    By = cc3.selectbox('Group By', [None, 'Occupation', 'Payment_Behaviour'])

    fig = px.box(df, x=Category, y=Numerical, color=By, template='plotly_dark',
                 title=f"{Numerical} Distribution by {Category}")
    fig.update_layout(xaxis_title=Category, yaxis_title=Numerical)
    st.plotly_chart(fig, use_container_width=True)


    # Pie Plots
    st.header("Distribution of Selected Feature")

    # Add a selectbox for the user to choose the feature
    feature = st.selectbox('Select Feature to Display', ['Occupation', 'Payment_Behaviour'])

    # Prepare the data for the pie chart based on the selected feature
    pie_data = df.groupby(feature).size().reset_index(name='Count')

    # Create a pie chart
    fig = go.Figure(data=[go.Pie(
        labels=pie_data[feature],
        values=pie_data['Count'],
        pull=[0, 0.1, 0.2, 0.3, 0.4]  
    )])

    # Update layout
    fig.update_layout(
        template='ggplot2',
        showlegend=True,
        legend_title_text=feature,
        title_text=f"{feature} Distribution"
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)


    # Scatter Plot with Correlation
    st.header("Correlation Between Numerical Features")
    ccc1, ccc2, ccc3, ccc4 = st.columns(4)

    Numerical1 = ccc1.selectbox('Feature 1', options=['Monthly_Balance', 'Annual_Income'])
    Numerical2 = ccc2.selectbox('Feature 2', options=['Annual_Income', 'Monthly_Balance'])
    By2 = ccc3.selectbox('Color By', options=[None, 'Occupation', 'Payment_Behaviour'])

    # Ensure numeric types and handle missing values
    df[Numerical1] = pd.to_numeric(df[Numerical1], errors='coerce')
    df[Numerical2] = pd.to_numeric(df[Numerical2], errors='coerce')

    # Drop rows with NaN values for correlation calculation
    df_clean = df.dropna(subset=[Numerical1, Numerical2])

    # Check if the DataFrame is not empty
    if len(df_clean) > 0:
        corr_value = round(stats.pearsonr(df_clean[Numerical1], df_clean[Numerical2]).statistic, 4)
    else:
        corr_value = 'N/A'

    ccc4.metric("Correlation", corr_value)

    fig = px.scatter(df_clean, x=Numerical1, y=Numerical2, color=By2, trendline='ols',
                     opacity=0.5, template='seaborn',
                     title=f'Correlation between {Numerical1} and {Numerical2}')
    fig.update_layout(xaxis_title=Numerical1, yaxis_title=Numerical2)
    st.plotly_chart(fig, use_container_width=True)