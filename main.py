from termcolor import colored
import random
import task
import person

class Task_manager:
    def __init__(self, tasks, people):
        self.tasks = tasks
        self.people = people
    
    #1 Посмотреть все текущие задачи
    def view_tasks(self):
        if len(self.tasks) == 0:
            print(colored('На данный момент нет ни одной задачи\n', color='light_cyan'))
        else:
            task_info = '\n'.join([task.introduce() for task in self.tasks.values()])
            s = f'{colored('Текущие задачи:', color='yellow')}\n{colored(task_info, color='light_blue')}'
            print(s)
    
    #2 Посмотреть информацию о конкретной задаче
    def specific_task(self):
        ident = input(colored('Введите id задачи, информацию о которй хотите получить: ', color='light_cyan'))
        if ident in self.tasks:
            print()
            print(colored(self.tasks[ident].show_full_info(), color='light_blue'))
        else:
            print(colored('Задачи с таким id не существует\n', color='light_red'))
    
    #3 Удалить(Выполнить) задачу
    def remove_task(self):
        ident = input(colored('Введите id задачи, которую хотите отметить выполненной и удалить: ', color='light_cyan'))
        if ident in self.tasks:
            del self.tasks[ident]
            print(colored('Задача удалена\n', color='green'))
        else:
            print(colored('Задачи с таким id не существует\n', color='light_red'))

    #4 Создать новую задачу
    def add_task(self):
        ident = str(random.randint(0, 999)).zfill(3)
        name = input(colored('Введите название новой задачи: ', color='light_cyan')).strip()
        description = input(colored('Введите её описание: ', color='light_cyan')).strip()
        people_idents = input(colored('Введите id сотрудников: ', color='light_cyan')).strip().split(' ')
        while not(self.check_idents(people_idents)):
            people_idents = input(colored('Введите id сотрудников: ', color='light_cyan')).strip().split(' ')
        people_idents = [ident.zfill(3) for ident in people_idents]
        deadline = input(colored('Введите срок выполнения задачи в днях: ', color='light_cyan')).strip()
        while not deadline.isnumeric():
            print(colored('Срок выполнения указывается в днях\n', color='light_red'))
            deadline = input(colored('Введите срок выполнения задачи в днях: ', color='light_cyan')).strip()

        self.tasks[ident] = task.create_task(ident, name, description, people_idents, deadline)
        print(colored('Новая задача добавлена!\n', color='green'))

    def id_check(self, ident):
        return ident.isnumeric()
    
    def check_idents(self, idents):
        for ident in idents:
            if not self.id_check(ident):
                print(colored(f'#{ident} - недопустимый id\n id должен состоять только из цифр\n', color='light_red'))
                return False
        return True


def show_information():
    s = 'Выберите одно из действий:\n'
    s += '1) Посмотреть текущие задачи\n'
    s += '2) Посмотреть задачу по её id\n'
    s += '3) Выполнить задачу\n'
    s += '4) Создать новую задачу\n'
    print(s)

def do_action(command):
    if command == '1':
        return manager.view_tasks()
    elif command == '2':
        return manager.specific_task()
    elif command == '3':
        return manager.remove_task()
    elif command == '4':
        return manager.add_task()

def get_input():
    num = input().strip()
    print()
    return num

def checker(num):
    return num in '1234' and len(num) == 1
    
def main():
    while True:
        show_information()
        command = get_input()
        while not(checker(command)):
            print(colored('Вам необходимо ввести одну цифру. Например: 1\n', color='light_red'))
            show_information()
            command = get_input()
        do_action(command)
        print()
        

manager = Task_manager({}, {})
main()
