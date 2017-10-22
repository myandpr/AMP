from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import random
from django.http import JsonResponse

import time

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


def index(request):
	cpu = random.randrange(1,68)
	
	temp = get_cluster()
	
	#return render(request, 'home.html', {'temp':temp})
	
	return render(request, 'home.html', {'cpu_html': json.dumps(cpu)})


"""
def index(request):
	if request.method == 'POST':
		if request.is_ajax():
			ip = request.POST.get('ip')
			#print(ip)
			dump = random.randrange(1, 68)
			disk_usage = random.randrange(1,56)
			cpu_load = random.randrange(1,56)
			cpu_rate = random.randrange(1,56)
			memory_usage = random.randrange(1,56)
			
			ret = {"dump":dump, "disk_usage":disk_usage,"cpu_load":cpu_load,"cpu_rate":cpu_rate,"memory_usage":memory_usage}
			return JsonResponse(ret)
	return render(request, 'home.html')
"""	


def ajax_cluster(request):
	if request.method == 'POST':
		if request.is_ajax():
			ip = request.POST.get('ip')
			#print(ip)
			dump = random.randrange(1, 68)
			disk_usage = random.randrange(1,56)
			cpu_load = random.randrange(1,56)
			cpu_rate = random.randrange(1,56)
			memory_usage = random.randrange(1,56)
			print(dump,disk_usage)
			ret = {"dump":dump, "disk_usage":disk_usage,"cpu_load":cpu_load,"cpu_rate":cpu_rate,"memory_usage":memory_usage}
			return JsonResponse(ret)
	return render(request, 'home.html')	





def j_index(request):
	#if request.method == 'POST':
		#name = request.POST.get('name')
		#status = 0
		#result = "error!!!"
		result = random.randrange(1,68)
		
		
		ret = {'status':1, 'cpu':23.9}
		ret['status'] = 1
		ret['cpu'] = result
		j_ret = json.dumps(ret)
		#print ret['cpu']
		return HttpResponse(j_ret)
		#return render(request, 'home.html',{ccc:j_ret})
		#return HttpResponse(json.dumps({"result":result}))


def ajax_index(request):
	if request.method == 'POST':
		if request.is_ajax():
			ip = request.POST.get('ip')
			#print(ip)
			result = random.randrange(1, 68)
			time1 = time.strftime("%H:%M:%S")
			
			#get the real_time datas from the perform_live table
			state = get_live(ip)
			
			ret = {"disk_usage":state[0], "cpu_load":state[1], "cpu_rate":state[2], "memory_usage":state[3]}
			
			
			
			
			#ret = {"cpu":result, "time":time1}
			return JsonResponse(ret)
	return render(request, 'home.html')		
			


"""
def index(request):
	cpus = random.randrange(1,56)
	time = 4
	cpu = {'cpus':33.6,'time':22}
	#return HttpResponse(json.dumps(cpu),content_type='application/json')
	#return JsonResponse(cpu)
	return render(request, 'home.html',{'cpu':json.dumps(cpus)})
	#return JsonResponse(cpu)
"""




#from django.shortcuts import render

# Create your views here.
import json
#from django.http import HttpResponse
import MySQLdb




def get_live(ip):
	db = MySQLdb.connect(ip,"root","root","yunwei")
	cursor = db.cursor()
	sql = "select * from perform_live"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			disk_usage = row[1]
			cpu_load = row[2]
			cpu_rate = row[3]
			memory_usage = row[4]
	except:
		print "Error:unable to fecth real_time datas!"
	db.close()
	
	state = [disk_usage,cpu_load,cpu_rate,memory_usage]
	return state




def get_cluster():
	db = MySQLdb.connect("192.168.69.144","root","root","yunwei")
	cursor = db.cursor()
	sql = "select * from cluster_statistics"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			dump = row[1]
			disk = row[2]
			cpu_load = row[3]
			cpu_rate = row[4]
			memory = row[5]
	except:
		print "Error:unable to fecth cluster statistics!"
	db.close()
	
	state = [dump,disk,cpu_load,cpu_rate,memory]
	return state
	
	

def cluster_index(request):
	#temp = [23.2,43.5,21.7,23.6,17.9]
	temp = get_cluster()
	#data = jason.dumps([temp])
	#return HttpResponse(content=data, content_type='application/json')
	return render(request, 'home.html', {'temp':temp})
#data: [49.9, 71.5, 10.4, 29.2, 44.0]
