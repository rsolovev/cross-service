# Cross-Service
An online platform where various service providers can reach and offer their services to potential customers requiring those services. The general customers are also able to make requests for particular services to best meet their needs.

# How to launch 
1. Install latest version of django framework
    `pip3 install django`
2. `cd `to project directory and run following commands:
 
    Create database:
    
    `python3 manage.py makemigrations` 
    
    `python3 manage.py makemigrations crosservice`
    
    `python3 manage.py migrate`
    
    Run server:
    `python3 manage.py runserver`
3. By default it will open on `localhost:8000`


# Database Backup
1. `cd` to your project root directory
2. `python3 manage.py dbbackup`
3. Your backup will save in the same directory as `default-hostname-YYYY-MM-DD-TTTTTT.dump`
