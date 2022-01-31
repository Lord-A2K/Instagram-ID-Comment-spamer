# instagram	ID spamer in comment for AD, with graph API
## by A2K

1. 
```
pip install -r requirements.txt
```

2. make a profile and a app in facebook developer site.
3. make an facebook app and get access token with simple premissions and comment premission.
4. import your access token and other information of your fb App in define.py.
5. print your facebook page id with **getUserPages** function using your access token and copy it.
6. print your instagram user id with **getPageIG** function using facebook page id and access token.
7. put one comment on the post you wanna spam comment, in instagram app.
8. run 

```
streamlit run main.py
```

9. the select the post you wanna spam comment on and fill the id section with gathered id's (you can use https://github.com/Lord-A2K/instagram-user-collector)

note: it may action block you if you use it alot.
