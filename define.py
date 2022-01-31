import requests
import json


def  getCredit():
    creds = {
        "access_token" : " your access_token",
        "client_id" : "your client_id",
        "client_secret" : "your client_secret",
        "graph_domain" : "https://graph.facebook.com/",
        "graph_version" : 'v11.0' ,
	    "endpoint_base" : "https://graph.facebook.com/v11.0/",
        "debug" : "no",
        "fb_page_id" : "your facebook page_id",
        "ig_user_id" : "your instagram user_id",
    }

    return creds

def APIcall( url, endpointParams, debug = "no"):
    data = requests.get(url, endpointParams)

    response = {
        "url" : url,
        "ednpoint_params" : endpointParams,
        "endpoint_params_pretty" : json.dumps(endpointParams, indent= 4),
        "json_data" : json.loads(data.content),
        "json_data_pretty" : json.dumps(json.loads(data.content), indent= 4),
    }

    if (debug == "yes"):
        displayAPICallData(response)
    
    return response

def displayAPICallData(response):
    print("\nURL:{}\nEndpoint Params:{}\nResponse:{}".format(
        response["url"],
        response["endpoint_params_pretty"],
        response["json_data_pretty"]
    ))
