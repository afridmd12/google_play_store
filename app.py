from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# === Load dataset ===
df = pd.read_csv("D:\google_play_store\googleplaystore.csv")

# === Data Cleaning ===
# Convert Size column to MB
def convert_size(size):
    if isinstance(size, str):
        size = size.strip()
        if size.endswith("M"):
            return float(size.replace("M", ""))
        elif size.endswith("k"):
            return round(float(size.replace("k", "")) / 1024, 2)
        elif size == "Varies with device":
            return None
    return None

df["Size_MB"] = df["Size"].apply(convert_size)

# Convert Installs to numeric
df["Installs"] = df["Installs"].astype(str).str.replace("[+,]", "", regex=True)
df["Installs"] = pd.to_numeric(df["Installs"], errors="coerce")

# Convert Price to numeric
df["Price"] = df["Price"].astype(str).str.replace("$", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Fix Rating
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Year as integer
df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")
df["Year"] = df["Last Updated"].dt.year.astype("Int64")

# Categories and years
categories = sorted(df["Category"].dropna().unique())
years = sorted(df["Year"].dropna().unique(), reverse=True)


# === Routes ===
@app.route("/")
def index():
    return render_template("index.html", categories=categories, years=years)


@app.route("/apps", methods=["GET"])
def apps():
    filtered = df.copy()

    # Get filters
    category = request.args.get("category")
    rating_range = request.args.get("rating")
    year = request.args.get("year")
    search = request.args.get("search")

    # Apply filters
    if category and category != "All":
        filtered = filtered[filtered["Category"] == category]

    if rating_range and rating_range != "All":
        try:
            low, high = map(float, rating_range.split("-"))
            filtered = filtered[(filtered["Rating"] >= low) & (filtered["Rating"] <= high)]
        except:
            pass

    if year and year != "All":
        try:
            year = int(year)
            filtered = filtered[filtered["Year"] == year]
        except:
            pass

    if search:
        filtered = filtered[filtered["App"].str.contains(search, case=False, na=False)]

    # Only show necessary columns for cards
    apps_list = filtered[["App", "Category", "Rating", "Reviews", "Installs", "Year"]].dropna().to_dict(orient="records")

    return render_template("apps.html", apps=apps_list, categories=categories, years=years)


@app.route("/app/<string:app_name>")
def app_detail(app_name):
    app_data = df[df["App"] == app_name].iloc[0].to_dict()
    return render_template("app_detail.html", app=app_data)


if __name__ == "__main__":
    app.run(debug=True, port=1914)
