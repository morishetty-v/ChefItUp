# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 2 docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the `webapp` user. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## For setting up a Conda Web-Dev environment:

1. `conda create -n webdev python=3.9`
1. `conda activate webdev`
1. `pip install flask flask-mysql flask-restful cryptography flask-login`





Chef Pages UI 

<img width="1408" alt="Screen Shot 2022-12-13 at 9 18 39 PM" src="https://user-images.githubusercontent.com/120275888/207489413-7a4b5c0b-83dd-4b59-91cf-994551bb7c66.png">


Athlete Pages UI

<img width="1408" alt="Screen Shot 2022-12-13 at 9 18 48 PM" src="https://user-images.githubusercontent.com/120275888/207489608-7c0e27b3-6d1b-454f-8949-02078a4b098c.png">

Student Pages UI

<img width="1408" alt="Screen Shot 2022-12-13 at 9 19 11 PM" src="https://user-images.githubusercontent.com/120275888/207489663-ddc43333-034e-4de2-b2b9-0ddb0c310639.png">

<img width="1408" alt="Screen Shot 2022-12-13 at 9 19 21 PM" src="https://user-images.githubusercontent.com/120275888/207489680-5fe98d3b-46b7-4873-af0d-4640a971b290.png">


User UI

<img width="618" alt="Screen Shot 2022-12-13 at 9 19 39 PM" src="https://user-images.githubusercontent.com/120275888/207489703-2a07dc54-af80-4819-ab61-699807e707a7.png">
