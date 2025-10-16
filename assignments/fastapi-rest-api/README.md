# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. Students will create endpoints, handle requests and responses, and explore basic validation and error handling.

## 📝 Tasks

### 🛠️  Create a Simple FastAPI Server

#### Description
Set up a FastAPI application with at least two endpoints. One endpoint should return a welcome message, and another should return a list of items (e.g., books, products, etc.).

#### Requirements
Completed program should:
- Use FastAPI to create a web server
- Include a root endpoint (`/`) that returns a welcome message
- Include an endpoint (e.g., `/items`) that returns a list of items in JSON format
- Run locally and be accessible via browser or API client

### 🛠️  Add Item Creation Endpoint

#### Description
Extend your API to allow users to add new items using a POST request. Validate the input and return the newly created item.

#### Requirements
Completed program should:
- Accept POST requests to add a new item
- Validate required fields (e.g., name, description)
- Return the created item in the response
- Handle errors gracefully (e.g., missing fields)

### 🛠️  Bonus: API Documentation & Error Handling

#### Description
Explore FastAPI's automatic documentation and improve error handling for invalid requests.

#### Requirements
Completed program should:
- Use FastAPI's built-in docs (Swagger UI)
- Return helpful error messages for invalid input
- Document endpoints with docstrings or comments
