class Task:
    def __init__(self, ident, name, description, people_idents, deadline):
        self.ident = ident
        self.name = name
        self.description = description
        self.people_idents = people_idents
        self.deadline = deadline
    
    def introduce(self):
        s = f'#id:{self.ident} / {self.name}'
        return s
    
    def show_full_info(self):
        s = f'#id:{self.ident} / {self.name}\n'
        s += f'Описание: {self.description}\n'
        s += f'Идентификаторы сотрудников: {' '.join(['#' + str(person_ident) for person_ident in self.people_idents])}\n'
        s += f'Срок выполнения (в днях): {self.deadline}'
        return s

def create_task(ident, name, description, people_idents, deadline):
    return Task(ident, name, description, people_idents, deadline)