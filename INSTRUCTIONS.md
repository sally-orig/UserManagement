## How to run application

1. Clone git repository to your local machine
    >git clone https://github.com/sally-orig/UserManagement.git UserManagementProject
2. Go to UserManagementProject folder:
    >cd UserManagementProject
3. Build docker images (fastapi and mysql)
    >docker compose up --build
4. Copy insert_data.py to container to populate database
    >docker cp insert_data.py fastapi:/app/insert_data.py
5. Open bash terminal in docker container
    >docker exec -it fastapi bash
6. Execute script
    >python insert_data.py