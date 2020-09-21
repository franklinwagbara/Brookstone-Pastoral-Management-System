import concurrent.futures
import threading
import time

def sendMail(st):

    time.sleep(2)
    print("printing ...{}".format(st))
    return "Done {}".format(st)

student = ['student1', 'student2', 'student3', 'student4']
st = ['stud1', 'stud2', 'stud3', 'stud4']

def test1():
    message = "Email failed!"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(sendMail, st) for st in student]

def test2():

    for s in student:
        x = threading.Thread(target=sendMail, args=(s,))
        print(x.start())
        print(x.join())
        x.

def test3():
    x2 = threading.Thread(target=sendMail, args=(st,))

    x2.start()

test2()
test3()
print("first")