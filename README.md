# Dynamic Profile Endpoint

A FastAPI application that serves a dynamic user profile with random cat facts.

## Features

- RESTful API built with FastAPI
- Pydantic models for data validation
- Integration with external Cat Facts API
- Timestamped responses
- Type-safe email validation

## Requirements

```
fastapi
requests
pydantic[email]
uvicorn
```

## Installation

1. Clone the repository or save the code to a file (e.g., `main.py`)

2. Install dependencies:
```bash
pip install fastapi requests pydantic[email] uvicorn
```

## Usage

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Root Endpoint
```
GET /
```

Returns a welcome message.

**Response:**
```json
{
  "message": "Dynamic Profile Endpoint"
}
```

### Profile Endpoint
```
GET /me
```

Returns user profile information along with a random cat fact.

**Response:**
```json
{
  "status": "success",
  "user": {
    "email": "itsemekaeze903@gmail.com",
    "name": "Emmanuel Eze",
    "stack": "Python/Fastapi"
  },
  "timestamp": "2025-10-16T12:34:56.789012",
  "fact": "A cat's hearing is better than a dog's."
}
```

## Data Models

### UserInfo
- `email` (EmailStr): User's email address
- `name` (str): User's full name
- `stack` (str): Technology stack

### Profile
- `status` (str): Response status (default: "success")
- `user` (UserInfo): User information object
- `timestamp` (datetime): UTC timestamp of the response
- `fact` (str): Random cat fact from external API

## External API

The application fetches random cat facts from:
```
https://catfact.ninja/fact
```

## Interactive Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`

## Error Handling

The cat fact fetcher includes error handling:
- 5-second timeout for API requests
- Graceful fallback message if the external API is unavailable

## Customization

To customize the profile information, modify the `UserInfo` instantiation in the `profile()` function:

```python
user = UserInfo(
    email="your.email@example.com",
    name="Your Name",
    stack="Your/Stack"
)
```

## License

This project is open source and available for educational purposes.

## Author

*Emmanuel Eze*