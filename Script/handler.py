import json
import requests

def handler(context, inputs):
    #Input Veriable Declaration
    vraurl = inputs["vRealizeApplianceURL"]
    vrauser = inputs["codestreamUserName"]
    vrapass = inputs["codestreamPassword"]
    pipeline = inputs["pipelineUUID"]

    #Get Access Token for vRA
    requestUrl = vraurl+"/csp/gateway/am/api/login?access_token"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"username":vrauser,"password":vrapass}
    response = requests.post(requestUrl, data=json.dumps(data), headers=headers, verify = False)
    print('Access Token Request response code is: ' + str(response.status_code))
    jsonResponse = response.json()
    #authtoken = jsonResponse.get('access_token') #Extract Token from json(remove after testing)
    #print(authtoken)

    #Get Bearer Token for vRA
    requestUrl = vraurl+"/iaas/api/login"
    authtoken = jsonResponse.get('refresh_token') 
    data = {"refreshToken":authtoken}
    response = requests.post(requestUrl, data=json.dumps(data), headers=headers, verify = False)
    print('Bearer Token Request response code is: ' + str(response.status_code))
    jsonResponse = response.json()
    bearertoken = jsonResponse.get('token') #Extract Token from json
    #print(bearertoken)

    #Run Image Pipeline
    requestUrl = vraurl+"/codestream/api/pipelines/"+pipeline+"/executions"
    data = {}
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization":"Bearer "+bearertoken}
    response = requests.post(requestUrl, data=json.dumps(data), headers=headers, verify = False)
    print('Pipeline Start Request response code is: ' + str(response.status_code))

    outputs = {
      "status": "done"
    }

    return outputs