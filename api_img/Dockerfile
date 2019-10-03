FROM ubuntu
run apt update
run apt install -y python3 python3-pip
run pip3 install flask
add ./api /home/api
cmd ["python3","/home/api/app.py"]

