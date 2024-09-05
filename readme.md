
## Prerequisites

Make sure you have Python 3.x installed on your machine. It's also recommended to use a virtual environment.

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ansh9728/workplate_ai.git
    cd workplate_assignment
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```bash
    
    python3 run.py
    ```

    This will start the app in your default browser where you can upload your data files and analyze them.

## Project Overview

1. **Data Processing:**
   - Upload files via the Streamlit app (.csv, .xlsx, .json)
   - The system will validate and clean the data before passing it to the analysis engine.

2. **Analysis Engine:**
   - Identifies key trends and patterns in the data 
   - Works for different types of datasets.

3. **Report Generation:**
   - The system generates detailed summaries, including missing values, central tendencies, and any identified patterns.
   - Reports are shown in the UI and can be exported.

