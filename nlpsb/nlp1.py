# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vuNNgWlMoZJSHSrw1xRI5uyCDA4ffZBe
"""


{"intents": [
    {"tag": "messup",
        "patterns": ["aaa","aaaaa","ssssas","sssss'","weeeeya", "yippie", "wharrrrrr", "halllaaaa", "kya hua", "wheee"],
        "responses": ["Please follow the proper pattern of asking questions. It saves time at both ends."],
        "context_set": ""
       },
    {"tag": "welcome",
     "patterns": ["Hi","yo","How you doin'","Heya", "How are you", "Is anyone there?", "Hello", "Good day", "Whats up"],
     "responses": ["Hello!", "Welcome dear user!", "Hi there, how can I serve you?", "Welcome to the power of customized backend dev", "Users are what make us worthy, thank you for joining the circle"],
     "context_set": ""
    },
    {"tag": "goodbye",
     "patterns": ["Thank you for working with us", "Look forward to us serving you soon", "Let us meet you soon", "Look forward to working with you.", "Our software a day gives you sleep and your manager happy ;)"],
     "responses": ["Sad to see you go :(", "Talk to you later", "Goodbye!"],
     "context_set": ""
    },
    {"tag": "about",
     "patterns": ["what is this about?", "what is the software about", "Why use this software", "backend", "difficulty with saving account?"],
     "responses": ["Hey, I am ShounuShek bot. I am built on python and django and I support and work on developing mysql commands."],
     "context_set": ""
    },
    
    {"tag": "information",
        "patterns": ["what is this about?", "what is the software about", "Why use this software", "backend", "difficulty with saving account?"],
        "responses": ["Hey, I am ShounuShek bot. I am built on python and django and I support and work on developing mysql commands."],
        "context_set": ""
    },

{"tag": "actions",
     "patterns": ["Manual", "help", "I have a doubt", "guidelines", "Steps"],
     "responses": ["Enter the model. Specifically say START A NEW PROJECT or START A PROJECT PREFERABLY IN SMALL. Now you can choose an option of adding a new model. Type Add a new model or create a new table or add table. Next you can insert the respective fields for this model under this command. Now you can use different routes and perform respective crud operations insert, read, update and delete. "],
     "context_set": ""
    },
    {"tag": "name",
     "patterns": ["what is your name", "what should I call you", "whats your name?"],
     "responses": ["You can call me Bhatta and kushwaha bot with roll number 18BCE0548 and 18BCE0492, Shounak Bhattacharya and Abhishek Kushwaha", "I'm your webdev expert helper bot!"],
     "context_set": ""
    },
    {"tag": "intro",
     "patterns": ["About the software", "what is the software about"],
     "responses": ["Hey, I am ShounuShek bot. I am built on python and django and I support and work on developing mysql commands."],
     "context_set": ""
    },
    {"tag": "contact",
     "patterns": ["Your contact number", "Were can we find you", "how to reach you", "are you on social media"],
     "responses": ["contact me on 8779174053 and 7980674536","Email your requests across to thecrazycoderabhi@gmail.com and shounak2922k@gmail.com"],
     "context_set": ""
    },
    {"tag": "motto",
     "patterns": ["what are the webdev and chatbot goals", "what are our dreams and ambition", "where will our generation will rise"],
     "responses": ["Decision Making in the face of Uncertainty. Attacking Every Challenge and Growing from it is my way to live life whether business or in General. Thats the Ultimate Goal - KAIZEN WAY"],
     "context_set": ""
    }
]
}
import os
import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('random.json') as json_file:     
  data = json.load(json_file)

from sklearn.preprocessing import LabelEncoder

training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
#labels

enc = LabelEncoder()
enc.fit(training_labels)
training_labels = enc.transform(training_labels)

#training_labels

vocab_size = 10000
embedding_dim = 16
max_len = 20
trunc_type = 'post'
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index
print(word_index)
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, truncating=trunc_type, maxlen=max_len)
print(sequences[0])
print(padded[0])

classes = len(labels)

model = tf.keras.models.Sequential()
model.add(keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(classes, activation='softmax'))

model.summary()

EPOCHS = 1000
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(padded, training_labels, epochs=EPOCHS)

from script_for_starting_project import (
  create_new_project,
  create_new_app,
  configuration_for_setting_up_apis,
  add_url_to_urlpatterns,
  add_views_initial_config_to_views
)

from script_for_making_crud import (
  making_create_route,
  making_read_route,
  making_update_route,
  making_delete_route
)

from script_for_virtualenv import (
  make_virtualenv,
  install_requirements
)

from script_for_making_model import (
  add_model_temp_fix
)

import numpy

project = False
model1 = False
routes = False
ts = False
module_name = ''
b=[]
c=[]
a=['add a new model', 'create a new table', 'create a new database model', 'add model', 'new table']
routeways =['insert','read', 'update', 'delete']
def check():
    global project
    global model
    global model1
    global routes
    global ts
    global module_name
    print('start talking with bot, Enter quit to exit. Random input will greet you')
    while True:
        string = input('Enter: ')
        if string == 'quit': break
        if ((string.lower() == 'start a new project') or (string.lower() == 'start a project')):
          if (project == False):
            string1 = input('Enter your project name: ')
            #calling abhishek function
            make_virtualenv()
            install_requirements()
            create_new_project(string1)
            create_new_app(string1, 'api')
            configuration_for_setting_up_apis(string1, 'api')
            add_url_to_urlpatterns(os.path.join(os.getcwd(), string1, string1, 'urls.py'), '\tpath("api/", include("api.urls")')
            add_views_initial_config_to_views(string1, 'api')
            project=string1
            print("Project created successfully in chatbot!")
            continue
          else:
            print("Project exists already")   
            continue
        if string.lower() in a:
            if not project:
              print("Please create a new project before proceeding")
            else:
              string2 = input('Enter table name: ')
              print("Enter the fields. Press done to leave entering the fields")
              while True:
                  string3 = input()
                  if(string3=="done"):
                    break
                  if(string3=="timestamp"):
                    ts=True#abhishekts
                  b.append(string3)
                  #abhishek function2
              add_model_temp_fix(project, 'api', string2, b)

            model1 = True
            module_name = string2
            continue    
        if string.lower() in routeways:
          if not project:
            print("Please set project and model name!")
            continue
          else:
            if string == routeways[0]:
              #abhishek insert
              url = input("Enter the endpoint: ")
              print(project, module_name, url)
              making_create_route(os.getcwd(),project, 'api', 'User', url)
              print("noprobs")
              continue
            if string == routeways[1]:
              url = input("Enter the endpoint: ")
              making_read_route(os.getcwd(), project, 'api', 'User', url)
              #abhishek read
              print("noprobs")
              continue
            if string == routeways[2]:
              url = input("Enter the endpoint: ")
              making_update_route(os.getcwd(), project, 'api', 'User', url)
              #abhishek update
              print("noprobs")
              continue
            if string == routeways[3]:
              url = input("Enter the endpoint: ")
              making_delete_route(os.getcwd(), project, 'api', 'User', url)
              #abhishek delete
              print("noprobs")
              continue    
        result = model.predict(pad_sequences(tokenizer.texts_to_sequences([string]),
                                             truncating=trunc_type, maxlen=max_len))
        category = enc.inverse_transform([np.argmax(result)]) # labels[np.argmax(result)]
      

        for i in data['intents']:
            print(category)
            if i['tag'] == category:
                
                print(np.random.choice(i['responses']))
                
                break



check()

