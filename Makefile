develop:
	rm -rf venv
	/usr/bin/python3 -m venv venv/elevator_simulator
	venv/elevator_simulator/bin/pip3 install -q -r requirements.txt
	venv/elevator_simulator/bin/pip3 install -e .
	venv/elevator_simulator/bin/pre-commit install
	/bin/ln -sfT /venv/elevator_simulator/bin/activate activate
