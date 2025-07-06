
Step 1: Open your Command Prompt (Windows) or Terminal (Mac/Linux)
Navigate to your project folder : 

cd C:\Users\Yousef\MyProject
Make sure inside this folder you have:

subnet_analyzer.py
requirements.txt
Dockerfile
ip_data.xlsx



Step 2: Build the Docker box

docker build -t subnet-analyzer .
This tells Docker: “Make me a box named subnet-analyzer using the Dockerfile here.”



Step 3 : Run your program inside the Docker box

docker run --rm subnet-analyzer
This runs your Python program inside the box.

It will create your CSV and image inside the Docker container.




Step 4 : Get your output files
To save the output files in your project folder on your computer, run this command instead:

docker run --rm -v %cd%:/app subnet-analyzer
(On Mac/Linux replace %cd% with $(pwd))

