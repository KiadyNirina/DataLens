# 📊 DataLens

> Interactive data visualization tool to easily explore, analyze and understand complex information.

DataLens is a web-based data visualization application built with Python and Dash. It allows users to upload CSV or JSON files, explore their data through an interactive table, and visualize it using different types of charts.

## ✨ Features

- 📂 Upload CSV and JSON files
- 🔤 Automatic character encoding detection for CSV files
- 📊 Interactive data visualization
- 📈 Multiple chart types:
  - Line charts
  - Bar charts
  - Pie charts
  - Scatter plots
- 📋 Interactive data table
- 🔍 Native data filtering
- ↕️ Native data sorting
- 💾 Local storage of uploaded data during the session
- ⚡ Real-time visualization updates when changing the chart type
- 🎨 Responsive interface using Tailwind CSS

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Dash | Web application framework |
| Pandas | Data processing and manipulation |
| Plotly | Interactive data visualization |
| Chardet | CSV encoding detection |
| Dash DataTable | Interactive data table |
| Tailwind CSS | User interface styling |

The project's dependencies are defined in `requirements.txt`.

## 📁 Project Structure

```text
DataLens/
│
├── assets/
├── app.py
├── callbacks.py
├── figures.py
├── layouts.py
├── parsers.py
├── requirements.txt
└── .gitignore
```

### `app.py`

Application entry point. It initializes the Dash application, creates the layout, and registers the callbacks.

### `layouts.py`

Contains the application's user interface, including:

- File upload area
- Visualization type selector
- Data storage components
- Results area
- Footer

The interface currently supports CSV and JSON uploads with a displayed 10 MB maximum file size.

### `callbacks.py`

Handles the application's interactions:

- Processing uploaded files
- Storing parsed data
- Updating visualizations
- Updating the data table
- Switching between visualization types

The data table supports native filtering and sorting with 10 rows displayed per page.

### `parsers.py`

Responsible for parsing uploaded files.

Supported formats:

- CSV
- JSON

CSV files are automatically decoded using the encoding detected by Chardet before being loaded with Pandas.

### `figures.py`

Responsible for generating Plotly figures from uploaded datasets.

Supported visualizations:

- Line
- Bar
- Pie
- Scatter

The application uses the first column as the X-axis for line, bar, and scatter visualizations. Pie charts require exactly two columns: labels and values.

## 🚀 Installation

### Prerequisites

Make sure you have installed:

- Python 3.9+
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/KiadyNirina/DataLens.git
cd DataLens
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start DataLens with:

```bash
python app.py
```

The Dash development server will then start locally.

By default, Dash runs the application at:

<http://127.0.0.1:8050>

## 📂 Using DataLens

### 1. Upload a dataset

Click the upload area or drag and drop a file.

Supported formats:

- `.csv`
- `.json`

### 2. Choose a visualization

Select one of the available visualization types:

- **Line** — visualize trends and changes
- **Bar** — compare values between categories
- **Pie** — visualize proportions
- **Scatter** — explore relationships between two variables

### 3. Explore the data

After uploading a dataset, DataLens displays:

- An interactive Plotly visualization
- An interactive data table

The table allows you to filter and sort the displayed data.

## 📊 Visualization Examples

### Line Chart

Useful for observing trends over time or across ordered values.

### Bar Chart

Useful for comparing values between different categories.

### Pie Chart

Useful for displaying proportions. DataLens expects exactly two columns for this visualization: one for labels and one for values.

### Scatter Plot

Useful for exploring relationships between two variables.

## 🧩 Architecture

DataLens follows a simple modular architecture:

```text
                ┌─────────────────┐
                │     User        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Dash UI       │
                │  layouts.py     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Callbacks     │
                │  callbacks.py   │
                └───────┬─┬───────┘
                        │ │
              ┌─────────┘ └─────────┐
              ▼                     ▼
      ┌───────────────┐     ┌───────────────┐
      │    Parser     │     │   Figures     │
      │  parsers.py   │     │  figures.py   │
      └───────┬───────┘     └───────┬───────┘
              │                     │
              ▼                     ▼
        ┌───────────┐         ┌───────────┐
        │  Pandas   │         │  Plotly   │
        └───────────┘         └───────────┘
```

## 🔄 Data Flow

```text
CSV / JSON
    │
    ▼
File Upload
    │
    ▼
Base64 Decoding
    │
    ▼
File Parser
    │
    ├── CSV → Encoding Detection → Pandas
    │
    └── JSON → Pandas
    │
    ▼
DataFrame
    │
    ├───────────────┐
    ▼               ▼
Data Table      Plotly Figure
    │               │
    ├─ Filter       ├─ Line
    └─ Sort         ├─ Bar
                    ├─ Pie
                    └─ Scatter
```

## 🔮 Future Improvements

Possible improvements for future versions:

- [ ] Support additional file formats such as Excel
- [ ] Advanced statistical analysis
- [ ] More visualization types
- [ ] Custom chart configuration
- [ ] Data cleaning tools
- [ ] Export generated charts
- [ ] Export processed datasets
- [ ] Dashboard customization
- [ ] Improved error messages
- [ ] Dataset statistics and summaries
- [ ] Deployment configuration

## 👨‍💻 Author

**Kiady Nirina**  
Full-Stack Developer & SaaS Builder

- GitHub: [@KiadyNirina](https://github.com/KiadyNirina)
- Portfolio: [kiadynirina.netlify.app](https://kiadynirina.netlify.app/)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## ⭐ Support

If you find DataLens useful, consider giving the repository a ⭐ on GitHub.

[View the repository](https://github.com/KiadyNirina/DataLens)
