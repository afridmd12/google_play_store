# Google Play Store Data Analysis

This project analyzes Google Play Store app data to derive insights such as top categories, ratings, installs, and other app-related statistics. The application is built using Flask and Python, providing an interactive interface for data visualization.

## Features

* Data visualization of app categories, ratings, installs, and reviews
* Filtering apps by rating ranges (1-2, 2-3, 3-4, 4-5)
* Sorting apps by name, rating, year, and other attributes
* Interactive dashboard for exploring dataset

## Project Process

1. **Data Collection**

   * Collected the dataset of Google Play Store apps with multiple attributes such as category, rating, reviews, size, installs, price, and more.

2. **Data Cleaning & Preparation**

   * Removed missing values and cleaned columns.
   * Converted numeric and categorical columns for analysis.
   * Handled inconsistent formatting in ratings, installs, and prices.

3. **Data Analysis**

   * Explored distributions of categories, ratings, and installs.
   * Identified top-performing apps and categories.
   * Analyzed trends over years using the Last Updated column.

4. **Visualization**

   * Created charts and interactive dashboards using Python libraries.
   * Implemented filters and sorting for better user experience.

5. **Deployment (Local)**

   * Flask app runs locally at port `1920`.
   * Users can interact with the dashboard to explore app insights.

## Tools Used

* Python 3.10+
* Flask
* Pandas
* NumPy
* Matplotlib / Seaborn (for plotting, if used)
* Jupyter Notebook (for exploratory analysis)

## Software Used

* VS Code / PyCharm / Any IDE for Python development
* Git & GitHub for version control
* Web browser to view the Flask dashboard locally

## Installation

1. Clone the repository:

```bash
git clone https://github.com/afridmd12/google_play_store.git
cd google_play_store
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open the app in your browser:

```
http://127.0.0.1:1920/
```

## Dataset

The dataset contains the following columns:

* App
* Category
* Rating
* Reviews
* Size
* Installs
* Type
* Price
* Content Rating
* Genres
* Last Updated
* Current Version
* Android Version

## Contribution

Feel free to fork the repository and make improvements. Pull requests are welcome.
