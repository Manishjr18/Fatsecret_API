# FatSecret API Integration with FastAPI

## Overview
This project integrates the **FatSecret API** with **FastAPI**, utilizing **OAuth 2.0 authentication** to fetch food data based on search queries. The application securely retrieves an access token and provides an API endpoint for food search. The project includes Swagger UI for testing and is version-controlled using Git.

## Features
- **OAuth 2.0 Authentication**: Securely fetches access tokens.
- **FastAPI Integration**: Implements an endpoint for food search.
- **Swagger UI**: Provides an interactive API documentation.
- **Git Version Control**: Code is maintained and pushed to GitHub.

## Setup Instructions

### Prerequisites
- Python 3.7+
- FatSecret API credentials (Client ID & Client Secret)
- Git installed

### Installation Steps

1. **Clone the Repository**
   ```sh
   git clone <your_github_repo_url>
   cd fatsecret_api
   ```

2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**
   Create a `.env` file and add the following credentials:
   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   TOKEN_URL=https://oauth.fatsecret.com/connect/token
   SEARCH_URL=https://platform.fatsecret.com/rest/server.api
   ```

5. **Run the Application**
   ```sh
   python -m uvicorn main:app --reload
   ```

6. **Test the API**
   Open your browser and visit:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Search API Example**: [http://127.0.0.1:8000/search_food/?query=apple](http://127.0.0.1:8000/search_food/?query=apple)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/search_food/?query=<food_name>` | Searches for food items in FatSecret |

## Deployment
To push the project to GitHub:
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

## License
This project is open-source and available under the MIT License.

---
**Author:** Manish Kumar  
For queries, reach out via [manishjr2507@gmail.com](mailto:manishjr2507@gmail.com)

