import os
import sqlite3
import shutil
import getpass
import pathlib

extrct = sqlite3.connect('db.sqlite3')
db = extrct.cursor()

def get_answers(quiz_id_no):
    db.execute(
        "SELECT answer_key FROM tsms_messagesreceiver WHERE msg_id =="+str(msg_id_no))
    results = db.fetchall()
    return results


def get_correct_answers(msg_id_no):
    db.execute(
        "SELECT answer_key FROM courses_quizsent WHERE quiz_id =="+str(quiz_id_no))
    results = db.fetchall()
    return results



def check_ans(quiz_id_no,msg_id_no):
    student_answers = get_answers(msg_id_no)
    get_correct_answers = get_correct_answers(quiz_id_no)
    
    size = len(student_answers)
    marks = 0
    for i in range(0,size):
        if(student_answers[i]==get_correct_answers[i]):
            marks = marks+1
    return marks


def marks_obtained(quiz_id_no, msg_id_no):
    return check_ans(quiz_id_no,msg_id_no)

