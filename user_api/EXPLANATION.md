# Explanation of My Work

This is a simple user management API built using FastAPI and PostgreSQL. It includes basic endpoints for user registration, login, and profile management.

## How It Works

The `/register` endpoint accepts user details, hashes the password using `bcrypt`, and stores them in the database. The `/login` endpoint checks user credentials and returns a JWT if authentication is successful.

The `/profile/{id}` endpoint is protected with JWT. It checks the token before allowing access to user data. The `/profile/{id}` PUT route updates a user’s profile after verifying the token.

## Database

I used PostgreSQL with SQLAlchemy ORM. The DB connection string is stored in a `.env` file, and models are defined using declarative base.

## Challenges

One challenge was setting up JWT properly and making sure the `Authorization` header was parsed securely. Also, I had to test error handling for cases like duplicate email, invalid login, and unauthorized access.

Overall, the project helped me solidify my understanding of FastAPI and secure authentication practices.
