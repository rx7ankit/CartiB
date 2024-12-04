# CartiB

CartiB is a price comparison web app that helps users find the best prices for products from different online stores like Blinkit, Swiggy Instamart, Ondoor, and Bigbasket.

## Features

- Price comparison from multiple stores.
- Fast and easy product price searching.
- Select your location and preferred stores.
  
## Installation

Follow the steps below to set up the project locally.

### 1. Clone the Repository

Clone the CartiB repository to your local machine:

```bash
git clone https://github.com/your-username/cartiB.git
```

### 2. Navigate to the Project Directory

```bash
cd cartiB
```

### 3. Create and Activate a Virtual Environment

**For macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

After activation, your terminal should show `(venv)` indicating that you're in the virtual environment.

### 4. Install Dependencies from `requirements.txt`

Once the virtual environment is activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install all the dependencies listed in `requirements.txt` for your project.

## Running the Application

1. Run the application using `uvicorn`:

   ```bash
   uvicorn main:app --reload
   ```

2. The app will be accessible in your browser at:

   ```bash
   http://127.0.0.1:8000
   ```