import streamlit as st
import requests
import json
import time
from define import APIcall, getCredit
import random

def getUserPages(access_token):
    url = "https://graph.facebook.com/v11.0/me/accounts"
    endpoint = {
        "access_token" : access_token
    }
    
    content = requests.get(url, endpoint).content
    
    return json.loads(content)["data"]

def getPageIG(fb_page_id, access_token):
    url = "https://graph.facebook.com/v11.0/" + fb_page_id
    endpoint = {
        "fields" : ["instagram_business_account"],
        "access_token" : access_token
    }
    
    content = requests.get(url, endpoint).content
    js = json.loads(content)
    # out = []
    # for ID in js["instagram_business_account"].values():
    #     out.append(ID)

    return js

def getIGMedia(ig_user_id, access_token):
    url = "https://graph.facebook.com/v11.0/" + ig_user_id + "/media"
    endpoint = {
        "access_token" : access_token
    }
    
    content = requests.get(url, endpoint).content
    js = json.loads(content)
    out = []
    for ID in js["data"]:
        out.append(ID["id"])

    return out

def getComment(media_id, access_token):
    url = "https://graph.facebook.com/v11.0/" + media_id + "/comments"
    endpoint = {
        "access_token" : access_token
    }
    content = requests.get(url, endpoint).content
    js = json.loads(content)
    out = []
    for cm in js["data"]:
        out.append(cm["id"])
    return out

def repComment(comment_id, message, access_token):
    url = "https://graph.facebook.com/v11.0/" + comment_id + "/replies"
    endpoint = {
        "message" : message,
        "access_token" : access_token
    }
    content = requests.post(url, endpoint).content
    return json.loads(content)

creds = getCredit()
access_token = creds["access_token"]


fb_page_id = creds["fb_page_id"]
ig_user_id = creds["ig_user_id"]

# print(getPageIG(fb_page_id, access_token))
media = getIGMedia(ig_user_id, access_token)




st.title("Instagram Commenting bot")

numOfComments = st.slider('comments per hour:', 0, 60, 55)

postNum = st.number_input('which post to comment (number):', value= 1)
# commentTxt = st.text_input("text of comment to reply:")
media_id = media[postNum - 1]
comments = getComment(media_id, access_token)



try:
    commentID = comments[0]
except:
    st.write("no comments found!")
    
tagIDstxt = st.text_area('IDs to tag:', height=200)
tagIDs = tagIDstxt.split("\n")

btnStart = st.button("start")





if btnStart:
    c1 = 0
    c2 = 0
    c3 = 0
    s = ""
    
    for ID in tagIDs:
        c1 += 1
        commentID = random.choice(comments)
        s += "@" + ID + " "
        if c1 == 10:
            tmp = repComment(commentID, s, access_token)
            s = ""
            c1 = 0
            c2 += 1
            # if tmp["id"].isdigit():
            #     comments.append(tmp)
            st.write(tmp)
            
        if c2 == numOfComments:
            time.sleep(3600)
            c2 = 0
        
        
    repComment(commentID, s, access_token)





st.write("\n\nmade by A2K @amirkian_kaveh")
