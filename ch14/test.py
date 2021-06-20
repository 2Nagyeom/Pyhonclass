import pyrebase

config = {
 "apiKey": "AIzaSyDOE4MiQr4TqQ4EtT8R7LN1E90zT7theuc",
"authDomain" : "test-d3492.firebaseapp.com",
"databaseURL": "https://test-d3492-default-rtdb.firebaseio.com",
 "projectId" : "test-d3492",
"storageBucket" : "test-d3492.appspot.com",
 "messagingSenderId" : "383303281710",
 "measurementId" : "G-301RKGEJJN"
};

firebase = pyrebase.initialize_app(config)
# DB생성하기
db = firebase.database()


