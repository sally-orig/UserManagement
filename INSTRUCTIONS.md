## How to run application

1. Clone git repository to your local machine
>>git clone https://github.com/sally-orig/UserManagement.git UserManagementProject
2. Go to UserManagementProject folder:
>>cd UserManagementProject
3. Build docker images (fastapi and mysql)
>>docker compose up --build
4. Copy insert_data.py to container to populate database
>>docker cp UserManagement/insert_data.py fastapi:/app/insert_data.py
5. Go to docker container and execute insert script
>>docker exec -it fastapi bash
>>python insert_data.py