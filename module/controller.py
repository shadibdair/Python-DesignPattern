from model import Person
import view

def showAll():
    #people_in_db = Person.getAll()
    return Person.getAll()

view.showAllView(showAll())

def start():
    view.startView()
    myinput = input()
    if myinput == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "main":
    start()