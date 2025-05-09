
import pandas as pd
import plotly.express as px
import preswald


df = pd.read_csv("data/sample1.csv")


Filter_df = df[df["avg_rainfall"] > 2000]


fig = px.scatter(
    Filter_df,
    x="avg_rainfall",
    y="max_temperature",
    text="area",
    color="max_temperature",
    size="avg_rainfall",
    title="Avg Rainfall vs Max Temperature (Filtered)",
    labels={"avg_rainfall": "Average Rainfall", "max_temperature": "Max Temperature"},
)

fig.update_traces(textposition="top center", marker=dict(opacity=0.7))
fig.update_layout(template="plotly_white")


preswald.text("Agricultural_Analysis")
preswald.text("This graphical demonstrates shows the correlation between the highest temperature as well as the average rainfall in several Bangladeshi regions.")


top = Filter_df.loc[Filter_df["avg_rainfall"].idxmax()]
preswald.text(f"*Highest Rainfall Area:* {top['area']} with average rainfall {top['avg_rainfall']} mm and max temperature {top['max_temperature']}°C")


preswald.plotly(fig)
preswald.table(Filter_df, title="Filtered Dataset (avg_rainfall > 2000 mm)")
