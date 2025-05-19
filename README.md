# UserManagement

A fastapi application to manage users - includes creating, updating, deleting and viewing of users and their information.

## Current Endpoints

1. GET /users - get all id and email addresses of users
2. GET /users/{user_id} - get user details (email, age, date of birth) given an Id

## Dependency

1. MySQL database

## How to run application

1. Clone git repository to your local machine
    >git clone <https://github.com/sally-orig/UserManagement.git> UserManagementProject
2. Go to UserManagementProject folder:
    >cd UserManagementProject
3. Build docker images (fastapi and mysql)
    >docker compose build
4. Put up container
    >docker compose up -d
