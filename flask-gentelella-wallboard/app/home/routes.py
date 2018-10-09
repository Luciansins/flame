from app.home import blueprint
from flask import render_template
from flask import jsonify
from flask_login import login_required
#Segmento Hindi
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
	requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
	pass

@blueprint.route('/banner_form')
@login_required
def banner_form():
	return render_template('banner_form.html')

@blueprint.route('/csq_chart')
@login_required
def csq_chart():
#segmento Hindi
    url_general = requests.get('https://10.246.146.15:9443/realtime/VoiceIAQStats', verify=False)
    url_csq = requests.get('https://10.246.146.15:9443/realtime/VoiceCSQDetailsStats', verify=False)
    data = url_general.json()
    data_csq = url_csq.json()
    total_llamadas = []
    llamadas_en_cola = []
    total_manejadas = []
    total_abandonadas = []
    total_activas_cola1 = 0
    total_activas_cola2 = 0
    total_activas_cola3 = 0
    total_activas_cola4 = 0
    for item in data_csq:
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_INTERNAL )':
            total_activas_cola1+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CRITICAL )':
            total_activas_cola2+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_EXTERNAL )':
            total_activas_cola3+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_SIT )':
            total_activas_cola4+=1

    for item in data:
        llamadas_en_cola.append(item['VoiceIAQStats']['nWaitingContacts'])
        total_llamadas.append(item['VoiceIAQStats']['nTotalContacts'])
        total_manejadas.append(item['VoiceIAQStats']['nHandledContacts'])
        total_abandonadas.append(item['VoiceIAQStats']['nAbandonedContacts'])

    general_data = {
	"agentes_conectados" : data[1]['VoiceIAQStats']['nResourcesLoggedIn'],
	"agentes_disponibles" : data[1]['VoiceIAQStats']['nAvailResources'],
	"agentes_working" : data[1]['VoiceIAQStats']['nWorkResources'],
	"agentes_talking" : data[1]['VoiceIAQStats']['nInSessionResources'],
	"llamadas_en_cola" : sum(llamadas_en_cola),
	"total_llamadas" : sum(total_llamadas),
    "total_manejadas" : sum(total_manejadas),
    "total_abandonadas" : sum(total_abandonadas)
	}

    return jsonify(general_data)

@blueprint.route('/global_data')
@login_required
def global_data():
#segmento Hindi
    url_general = requests.get('https://10.246.146.15:9443/realtime/VoiceIAQStats', verify=False)
    url_csq = requests.get('https://10.246.146.15:9443/realtime/VoiceCSQDetailsStats', verify=False)
    data = url_general.json()
    data_csq = url_csq.json()
    total_llamadas = []
    llamadas_en_cola = []
    total_manejadas = []
    total_abandonadas = []
    total_activas_cola1 = 0
    total_activas_cola2 = 0
    total_activas_cola3 = 0
    total_activas_cola4 = 0
    for item in data_csq:
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_INTERNAL )':
            total_activas_cola1+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CRITICAL )':
            total_activas_cola2+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_EXTERNAL )':
            total_activas_cola3+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_SIT )':
            total_activas_cola4+=1

    for item in data:
        llamadas_en_cola.append(item['VoiceIAQStats']['nWaitingContacts'])
        total_llamadas.append(item['VoiceIAQStats']['nTotalContacts'])
        total_manejadas.append(item['VoiceIAQStats']['nHandledContacts'])
        total_abandonadas.append(item['VoiceIAQStats']['nAbandonedContacts'])

    general_data = {
	"agentes_conectados" : data[1]['VoiceIAQStats']['nResourcesLoggedIn'],
	"agentes_disponibles" : data[1]['VoiceIAQStats']['nAvailResources'],
	"agentes_working" : data[1]['VoiceIAQStats']['nWorkResources'],
	"agentes_talking" : data[1]['VoiceIAQStats']['nInSessionResources'],
	"llamadas_en_cola" : sum(llamadas_en_cola),
	"total_llamadas" : sum(total_llamadas),
    "total_manejadas" : sum(total_manejadas),
    "total_abandonadas" : sum(total_abandonadas)
	}

    return render_template('global_data.html',general_data=general_data)


@blueprint.route('/csq_detail')
@login_required
def csq_detail():
#segmento Hindi
    url_general = requests.get('https://10.246.146.15:9443/realtime/VoiceIAQStats', verify=False)
    url_csq = requests.get('https://10.246.146.15:9443/realtime/VoiceCSQDetailsStats', verify=False)
    data = url_general.json()
    data_csq = url_csq.json()
    total_llamadas = []
    llamadas_en_cola = []
    total_manejadas = []
    total_abandonadas = []
    total_activas_cola1 = 0
    total_activas_cola2 = 0
    total_activas_cola3 = 0
    total_activas_cola4 = 0
    for item in data_csq:
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_INTERNAL )':
            total_activas_cola1+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CRITICAL )':
            total_activas_cola2+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_EXTERNAL )':
            total_activas_cola3+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_SIT )':
            total_activas_cola4+=1

    for item in data:
        llamadas_en_cola.append(item['VoiceIAQStats']['nWaitingContacts'])
        total_llamadas.append(item['VoiceIAQStats']['nTotalContacts'])
        total_manejadas.append(item['VoiceIAQStats']['nHandledContacts'])
        total_abandonadas.append(item['VoiceIAQStats']['nAbandonedContacts'])

    general_data = {
	"agentes_conectados" : data[1]['VoiceIAQStats']['nResourcesLoggedIn'],
	"agentes_disponibles" : data[1]['VoiceIAQStats']['nAvailResources'],
	"agentes_working" : data[1]['VoiceIAQStats']['nWorkResources'],
	"agentes_talking" : data[1]['VoiceIAQStats']['nInSessionResources'],
	"llamadas_en_cola" : sum(llamadas_en_cola),
	"total_llamadas" : sum(total_llamadas),
    "total_manejadas" : sum(total_manejadas),
    "total_abandonadas" : sum(total_abandonadas)
	}

    data_cola1 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_INTERNAL',
	"llamadas_activas" : total_activas_cola1,
	"llamadas_manejadas" : data[0]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[0]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[0]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[0]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[0]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[0]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[0]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola2 = {
	"nombre_cola" : 'CSQ_REQ_INC_CRITICAL',
	"llamadas_activas" : total_activas_cola2,
	"llamadas_manejadas" : data[1]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[1]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[1]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[1]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[1]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[1]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[1]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola3 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_EXTERNAL',
	"llamadas_activas" : total_activas_cola3,
	"llamadas_manejadas" : data[2]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[2]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[2]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[2]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[2]['VoiceIAQStats']['longestCurrentlyWaitingDuration']/1000),
    "tiempo_de_espera_mas_largo" : int(data[2]['VoiceIAQStats']['longestWaitDuration']/1000),
    "total_de_llamadas" : data[2]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola4 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_SIT',
	"llamadas_activas" : total_activas_cola4,
	"llamadas_manejadas" : data[3]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[3]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[3]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[3]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[3]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[3]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[3]['VoiceIAQStats']['nTotalContacts']
	}

    return render_template('csq_detail.html',general_data=general_data, data_cola1=data_cola1, data_cola2 = data_cola2, data_cola3 = data_cola3, data_cola4 = data_cola4)

@blueprint.route('/index')
@login_required
def index():
#segmento Hindi
    url_general = requests.get('https://10.246.146.15:9443/realtime/VoiceIAQStats', verify=False)
    url_csq = requests.get('https://10.246.146.15:9443/realtime/VoiceCSQDetailsStats', verify=False)
    data = url_general.json()
    data_csq = url_csq.json()
    total_llamadas = []
    llamadas_en_cola = []
    total_manejadas = []
    total_abandonadas = []
    total_activas_cola1 = 0
    total_activas_cola2 = 0
    total_activas_cola3 = 0
    total_activas_cola4 = 0
    for item in data_csq:
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_INTERNAL )':
            total_activas_cola1+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CRITICAL )':
            total_activas_cola2+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_EXTERNAL )':
            total_activas_cola3+=1
        if item['VoiceCSQDetailsStats']['agentState'] == 'Talking ( from CSQ: CSQ_REQ_INC_CON_SIT )':
            total_activas_cola4+=1

    for item in data:
        llamadas_en_cola.append(item['VoiceIAQStats']['nWaitingContacts'])
        total_llamadas.append(item['VoiceIAQStats']['nTotalContacts'])
        total_manejadas.append(item['VoiceIAQStats']['nHandledContacts'])
        total_abandonadas.append(item['VoiceIAQStats']['nAbandonedContacts'])

    general_data = {
	"agentes_conectados" : data[1]['VoiceIAQStats']['nResourcesLoggedIn'],
	"agentes_disponibles" : data[1]['VoiceIAQStats']['nAvailResources'],
	"agentes_working" : data[1]['VoiceIAQStats']['nWorkResources'],
	"agentes_talking" : data[1]['VoiceIAQStats']['nInSessionResources'],
	"llamadas_en_cola" : sum(llamadas_en_cola),
	"total_llamadas" : sum(total_llamadas),
    "total_manejadas" : sum(total_manejadas),
    "total_abandonadas" : sum(total_abandonadas)
	}

    data_cola1 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_INTERNAL',
	"llamadas_activas" : total_activas_cola1,
	"llamadas_manejadas" : data[0]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[0]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[0]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[0]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[0]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[0]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[0]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola2 = {
	"nombre_cola" : 'CSQ_REQ_INC_CRITICAL',
	"llamadas_activas" : total_activas_cola2,
	"llamadas_manejadas" : data[1]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[1]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[1]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[1]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[1]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[1]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[1]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola3 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_EXTERNAL',
	"llamadas_activas" : total_activas_cola3,
	"llamadas_manejadas" : data[2]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[2]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[2]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[2]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[2]['VoiceIAQStats']['longestCurrentlyWaitingDuration']/1000),
    "tiempo_de_espera_mas_largo" : int(data[2]['VoiceIAQStats']['longestWaitDuration']/1000),
    "total_de_llamadas" : data[2]['VoiceIAQStats']['nTotalContacts']
	}

    data_cola4 = {
	"nombre_cola" : 'CSQ_REQ_INC_CON_SIT',
	"llamadas_activas" : total_activas_cola4,
	"llamadas_manejadas" : data[3]['VoiceIAQStats']['nHandledContacts'],
	"llamadas_en_cola" : data[3]['VoiceIAQStats']['nWaitingContacts'],
    "voice_mail" : data[3]['VoiceIAQStats']['nDequeuedContacts'],
	"llamadas_abandonadas" : data[3]['VoiceIAQStats']['nAbandonedContacts'],
	"tiempo_de_espera_actual" : int(data[3]['VoiceIAQStats']['longestCurrentlyWaitingDuration'] / 1000),
    "tiempo_de_espera_mas_largo" : int(data[3]['VoiceIAQStats']['longestWaitDuration'] / 1000),
    "total_de_llamadas" : data[3]['VoiceIAQStats']['nTotalContacts']
	}

    print(data_cola1)
#Fin Segmento Hindi
    return render_template('index.html',general_data=general_data, data_cola1=data_cola1, data_cola2 = data_cola2, data_cola3 = data_cola3, data_cola4 = data_cola4)

@blueprint.route('/<template>')
@login_required
def route_template(template):
	return render_template(template + '.html')
