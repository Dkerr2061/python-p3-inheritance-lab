#!/usr/bin/env python

from user import User

class Student(User):

    knowledge = []

    def __init__(self, first_name, last_name, knowledge= knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, new_knowledge):
        if(type(new_knowledge) is str):
            self.knowledge.append(new_knowledge)
        