import subprocess
import psutil
import random
import time
import os

FNULL = open(os.devnull, 'w')

bench_thresh = 0.2
period_max = 30
bench_processes = []
other_processes = []
path = "/home/odroid/hw1_files/parsec_files/"
inputs = [path + 'sequenceB_261/', path + 'in_10M_blackscholes.txt']
cmd = 'taskset --all-tasks ' + '{} {}'

benchmarks = [ path + 'bodytrack', path + 'blackscholes' ]

random.seed()
while True:
	for i in range(len(bench_processes)-1, -1, -1):
		if bench_processes[i].poll() is not None:
			del bench_processes[i]
	# Roll a die:
	d = random.random()
	if d >= bench_thresh and len(bench_processes) == 0:
		print("starting new run")
		# launch a new benchmark
		affinity_l = 0#random.randint(0, 15)
		affinity_b = random.randint(1, 15)
		affinity = affinity_l | (affinity_b << 4)
		affinity_string = hex(affinity)
		num_threads = bin(affinity).count("1")#random.randint(1, bin(affinity).count("1"))
		bm_index = 1#random.randint(0,1)
		if bm_index == 0: # bodytrack
			cmd_bm_args = ' {} 4 260 3000 8 3 {} 0'.format(inputs[bm_index], num_threads)
			#cmd_f = cmd.format(affinity_string, cmd_bm)
		elif bm_index == 1: # Blackscholes
			cmd_bm_args = ' {} {} /dev/null'.format(num_threads, inputs[bm_index])
			#cmd_f = cmd.format(affinity_string, cmd_bm)
		#print(cmd_f.split(' '))
		bench_processes.append(subprocess.Popen(['/bin/sh', './parsec.sh', affinity_string, benchmarks[bm_index], \
				cmd_bm_args]))#, stdout=FNULL ))


	time.sleep(random.randint(0, period_max))

