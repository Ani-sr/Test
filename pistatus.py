from __future__ import division
import dweepy
from subprocess import PIPE, Popen
import psutil
import time
import os

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


try:
	while True: 
		ostemp = os.popen('vcgencmd measure_temp').readline()
		temp = (ostemp.replace("temp=", " ").replace("'C\n", " "))
		
	

    
		ram = psutil.phymem_usage()
		ram_total = ram.total / 2**20      
		ram_used = ram.used / 2**20
		ram_free = ram.free / 2**20
		ram_percent_used = ram.percent
    
		disk = psutil.disk_usage('/')
		disk_total = disk.total / 2**30   
		disk_used = disk.used / 2**30
		disk_free = disk.free / 2**30
		disk_percent_used = disk.percent
     
		processes = sorted(
			((p.get_memory_info().vms, p) for p in psutil.process_iter()),
			reverse=True
			)
		for virtual_memory, process in processes[:5]:
			print virtual_memory // 2**20, process.pid, process.name

	
		ra=str(ram_percent_used)+'%'
		dis=str(disk_percent_used)+'%'

		dweepy.dweet_for('SDN_Hack_RPi7', {"Temperature":temp,"RAM":ra,"Disk":dis } )
		time.sleep(15)
except KeyboardInterrupt:
	exit()
	




