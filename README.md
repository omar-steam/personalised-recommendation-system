# Personalised Recommendation System Using AWS
A simple-to-use Stream-lit application that recommends AWS learning resources based on user interests.

## Features
- Interactive web interface built with Streamlit
- Content-based recommendation system using TF-IDF
- Mock S3 integration for development and testing
- Customizable learning resource database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/omar-steam/personalised-recommendation-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage
1. Enter your learning interests in the text input field
2. Click "Get Recommendations" to receive personalized learning path suggestions
3. View the top 3 recommended AWS learning resources

## Testing
Run the tests using pytest:
```bash
pytest tests/
```

## Requirements
See requirements.txt for full list of dependencies.

---

# File: requirements.txt
```bash
streamlit==1.31.0
boto3==1.34.0
scikit-learn==1.3.0
moto==4.2.0
pytest==7.4.0
```
---

# File: .gitignore
```bash
__pycache__/
*.py[cod]
*$py.class
.env
.venv
env/
venv/
ENV/
.pytest_cache/
.coverage
.DS_Store
```
---
