from enum import Enum
import random


class Task(object):
    def __init__(self, name, count, special_task, task_type, task_classification):
        self.name = name
        self.count = count
        self.special_task = special_task
        self.task_type = task_type
        self.task_classification = task_classification

class TaskClassification(Enum):
    Children = 1
    Teenager = 2
    Adult = 3

class TaskDayType(Enum):
    Weekend = 1
    Workday = 2
    CompleteWeek = 3

TaskList = []

TaskCategories = [
        [{"name": "Kleiner Einkauf", "anzahl":6, "special_task": False, "day": TaskDayType.CompleteWeek}, TaskClassification.Children],
        [{"name": "Waschen/Abtrocknen", "anzahl":7, "special_task": False, "day": TaskDayType.CompleteWeek}, TaskClassification.Children],
        [{"name": "kochen", "anzahl":7, "special_task": False, "day": TaskDayType.CompleteWeek}, TaskClassification.Teenager],
        [{"name": "Tischdienst", "anzahl":7, "special_task": False, "day": TaskDayType.CompleteWeek}, TaskClassification.Children],
        [{"name": "Waesche waschen", "anzahl":3, "special_task": False, "day": TaskDayType.CompleteWeek},TaskClassification.Children],
        [{"name": "Herd putzen", "anzahl":3, "special_task": False, "day": TaskDayType.CompleteWeek},TaskClassification.Teenager],
        [{"name": "WC und Waschbecken reinigen", "anzahl":2, "special_task": False, "day": TaskDayType.CompleteWeek}, TaskClassification.Children],
        [{"name": "Kochwaesche waschen", "anzahl":1, "special_task": False, "day": TaskDayType.Weekend}, TaskClassification.Children],
        [{"name": "Papiermuell runterbringen", "anzahl":1, "special_task": True, "day": TaskDayType.CompleteWeek}, TaskClassification.Children],
        [{"name": "Wochenmanager", "anzahl":1, "special_task": True, "day": TaskDayType.CompleteWeek},TaskClassification.Children],
        [{"name": "Bad putzen", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend}, TaskClassification.Children],
        [{"name": "staubsaugen", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend},TaskClassification.Children],
        [{"name": "Kueche putzen", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend},TaskClassification.Teenager],
        [{"name": "Boeden wischen", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend}, TaskClassification.Children],
        [{"name": "Staub wischen", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend}, TaskClassification.Children],
        [{"name": "Grosser Einkauf", "anzahl": 1, "special_task": True, "day": TaskDayType.Weekend}, TaskClassification.Adult],
        [{"name": "Muelldienst", "anzahl":1, "special_task": True, "day": TaskDayType.Weekend},TaskClassification.Children],
        ]

for task in TaskCategories:
    new_task = Task(task[0]["name"], task[0]["anzahl"], task[0]["special_task"], task[0]["day"], task[1])
    TaskList.append(new_task)

ANZAHL_WOCHENAUFGABEN = 0
for task in TaskList:
    ANZAHL_WOCHENAUFGABEN += task.count


class FamilyMember(object):
    def __init__(self, name, taskClassification=None):
        self.taskClassification = taskClassification
        self.name = name
        self.taskList = []
        self.special_task_counter = 0
        self.weekend_tasks = 0

frederick = FamilyMember("Frederick", TaskClassification.Children)
nevio = FamilyMember("Nevio", TaskClassification.Teenager)
barbarella = FamilyMember("Barbarella", TaskClassification.Adult)
kai = FamilyMember("Kai", TaskClassification.Adult)
family_members = [frederick, nevio, barbarella, kai]


TASKS_PER_FAMILY_MEMBER = (ANZAHL_WOCHENAUFGABEN/len(family_members))
MAX_WEEKEND_TASKS = 2

"""
def take_task(family_member):
    taskNumber = random.randint(0,len(TaskCategories)-1)

    if TaskCategories[taskNumber][1].value <= family_member.taskClassification.value and TaskCategories[taskNumber][0]["anzahl"]> 0:
        # es gibt diesen task noch und der task ist fuer das family_member tauglich
        if TaskCategories[taskNumber][0]["day"].value == TaskDayType.Weekend:
            # wochenend tasks werden besonders behandelt
            if family_member.weekend_tasks < MAX_WEEKEND_TASKS:
                # family_member hat noch nicht genuegend wochenend tasks
                TaskCategories[taskNumber][0]["anzahl"] -= 1
                family_member.taskList.append(TaskCategories[taskNumber][0]["name"])
                family_member.weekend_tasks += 1
            else:
                # family_member braucht keine weiteren wochenend tasks. also nochmal take_task
                take_task(family_member)
        else:
            # keine wochenendaufgabe
            TaskCategories[taskNumber][0]["anzahl"] -= 1
            family_member.taskList.append(TaskCategories[taskNumber][0]["name"])
    else:
        take_task(family_member)
"""

def take_task(family_member):
    taskNumber = random.randint(0,len(TaskList)-1)
    if TaskList[taskNumber].task_classification.value <= family_member.taskClassification.value and TaskList[taskNumber].count> 0:
        # es gibt diesen task noch und der task ist fuer das family_member tauglich
        if TaskList[taskNumber].task_type.value == TaskDayType.Weekend:
            # wochenend tasks werden besonders behandelt
            if family_member.weekend_tasks < MAX_WEEKEND_TASKS:
                # family_member hat noch nicht genuegend wochenend tasks
                TaskList[taskNumber].count -= 1
                family_member.taskList.append(TaskList[taskNumber].name)
                family_member.weekend_tasks += 1
            else:
                # family_member braucht keine weiteren wochenend tasks. also nochmal take_task
                take_task(family_member)
        else:
            # keine wochenendaufgabe
            TaskList[taskNumber].count -= 1
            family_member.taskList.append(TaskList[taskNumber].name)
    else:
        take_task(family_member)


def start_for_familymember(family_member):
    for task in range(0, TASKS_PER_FAMILY_MEMBER):
        take_task(family_member)

for family_member in family_members:
    start_for_familymember(family_member)

left_over_tasks = []

for task in TaskList:
    if task.count > 0:
        print "Leftover Task: %s count: %s" % (task.name, task.count)
        left_over_tasks.append(task)

if left_over_tasks:
    print "Asigning leftover tasks"
    for task in left_over_tasks:
        for times in range(0,task.count):
            family_members[random.randint(0,len(family_members)-1)].taskList.append(task.name)

for family_member in family_members:
    print "%s Tasks fuer %s: %s" % ( len(family_member.taskList), family_member.name, family_member.taskList)

"""
left_over_tasks = []
for task in TaskCategories:
    if task[0]["anzahl"]>0:
        left_over_tasks.append(task)

if left_over_tasks:
    print "Asign leftover tasks"
    for task in left_over_tasks:
        family_members[random.randint(0,len(family_members)-1)].taskList.append(task[0]["name"])

for family_member in family_members:
    print "%s Tasks fuer %s: %s" % ( len(family_member.taskList), family_member.name, family_member.taskList)


"""

"""
Woche = [
    {"day": "Montag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Dienstag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Mittwoch", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Donnerstag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Freitag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Samstag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
    {"day": "Sonntag", "taskList": {"Kleiner Einkauf":"" , "Waschen/Abtrocknen": "", "kochen":"", "Tischdienst":""}},
]

def pick_week_task(family_guy, day):
    for task in family_guy.taskList:
        if task in day["taskList"]:
            day["taskList"][task] = family_guy.name
            return

for day in Woche:
    for task in day["taskList"]:
        pick_week_task(family_members[random.randint(0,len(family_members)-1)], day)
print Woche
"""
