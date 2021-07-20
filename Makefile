docker: 
	docker run -p 6379:6379 -d redis:5

iot-client: IoT_Client/main.py
	python3 IoT_Client/main.py

server: manage.py
	python3 manage.py runserver

