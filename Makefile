NUM_GRAPHS ?= 2
NUM_NODES ?= 5

gen:
	python gen.py $(NUM_GRAPHS) $(NUM_NODES)

clean:
	git clean -xf
