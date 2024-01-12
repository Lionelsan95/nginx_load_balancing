# Nginx Load Balancing

## Introduction
Implementing app load balancing with nginx and Flask

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker installed on your system
- Docker Compose installed on your system

## Installation & Usage
To get this project up and running on your machine, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone git@github.com:Lionelsan95/nginx_load_balancing.git
   cd nginx_load_balancing
   ```

2. **Starting the Application:**
   - To start the application in detached mode:
     ```sh
     make up
     ```
   - To build the containers before starting the application:
     ```sh
     make up-build
     ```
   - To view logs while starting the application:
     ```sh
     make up-log
     ```

3. **Stopping the Application:**
   - To stop the running containers:
     ```sh
     make down
     ```

4. **Viewing Running Containers:**
   - To list the current running containers:
     ```sh
     make list
     ```

## Contributing
Contributions to this project are welcome. Here's how you can do it:
1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a Pull Request.

## License
MIT

## Contact
Lionel Owono - lionel.owono@esperluet.xyz
Project Link: https://github.com/Lionelsan95/nginx_load_balancing