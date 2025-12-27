import pandas as pd
import plotly.express as px

# -------------------------------
# 1. Define the data (GDP per capita and population estimates for 2024/2025)
# -------------------------------
data = {
    "Country": [
        "Qatar", "United Arab Emirates", "Kuwait", "Saudi Arabia", "Bahrain", "Oman",
        "Libya", "Iraq", "Algeria", "Jordan", "Egypt", "Tunisia", "Morocco",
        "Lebanon", "Mauritania", "Djibouti", "Palestine", "Sudan", "Yemen",
        "Somalia", "Comoros", "Syria"
    ],
    "GDP_per_capita_USD": [
        71653, 49498, 45000, 30099, 28000, 25000,
        10000, 13000, 13000, 5000, 4000, 4000, 4000,
        3000, 2000, 3000, 3000, 1000, 417,
        800, 500, 600
    ],
    "Population_millions": [
        2.7, 10.2, 4.5, 36.0, 1.8, 4.6,
        7.0, 44.0, 45.0, 11.0, 110.0, 12.0, 37.0,
        5.5, 4.8, 1.0, 5.3, 48.0, 34.0,
        17.0, 0.9, 22.0
    ]
}

# -------------------------------
# 2. Create DataFrame and sort
# -------------------------------
df = pd.DataFrame(data).sort_values("GDP_per_capita_USD", ascending=True)

# -------------------------------
# 3. Highlight top 5 richest countries
# -------------------------------
top_5 = df.sort_values("GDP_per_capita_USD", ascending=False).head(5)["Country"].tolist()
df["Highlight"] = df["Country"].apply(lambda x: "Top 5" if x in top_5 else "Others")

# -------------------------------
# 4. Interactive horizontal bar chart (GDP per capita)
# -------------------------------
fig_bar = px.bar(
    df,
    x="GDP_per_capita_USD",
    y="Country",
    orientation="h",
    color="Highlight",
    color_discrete_map={"Top 5": "gold", "Others": "steelblue"},
    text="GDP_per_capita_USD",
    title="GDP per Capita in Arab Countries (2024/2025 Estimates)",
)

fig_bar.update_traces(texttemplate="$%{text:,}", textposition="outside")
fig_bar.update_layout(
    xaxis_title="GDP per Capita (US$)",
    yaxis_title="Country",
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridcolor="lightgrey"),
    height=800
)

# -------------------------------
# 5. Interactive bubble chart (GDP vs Population)
# -------------------------------
fig_bubble = px.scatter(
    df,
    x="Population_millions",
    y="GDP_per_capita_USD",
    size="Population_millions",
    color="Highlight",
    hover_name="Country",
    color_discrete_map={"Top 5": "gold", "Others": "steelblue"},
    title="GDP per Capita vs Population (Bubble Size = Population)",
    labels={"Population_millions": "Population (millions)", "GDP_per_capita_USD": "GDP per Capita (US$)"},
)

fig_bubble.update_layout(
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridcolor="lightgrey"),
    yaxis=dict(showgrid=True, gridcolor="lightgrey"),
    height=700
)

# -------------------------------
# 6. Show charts (or export to HTML for headless environments)
# -------------------------------
fig_bar.show()
fig_bubble.show()

# For headless environments, save as HTML:
# fig_bar.write_html("arab_gdp_bar.html")
# fig_bubble.write_html("arab_gdp_bubble.html")
# print("✅ Interactive charts saved as arab_gdp_bar.html and arab_gdp_bubble.html")
