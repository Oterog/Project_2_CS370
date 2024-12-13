from tg import expose, redirect
from tg.controllers import TGController
from turbogearsapp.model import DBSession, TodoItem

class RootController(TGController):
    @expose('kajiki:tasks.xhtml')
    def index(self):
        # Retrieve tasks from the database
        tasks = DBSession.query(TodoItem).all()
        tasks_data = [{'id': task.id, 'description': task.description} for task in tasks]
        print("Formatted tasks for template:", tasks_data)  # Debugging
        return dict(tasks=tasks_data)

    @expose()
    def add_task(self, description):
        if description.strip():
            new_task = TodoItem(description=description)
            DBSession.add(new_task)
            DBSession.flush()  # Push to database
            DBSession.commit()  # Commit transaction
        return redirect('/')

    @expose()
    def delete_task(self, task_id):
        task = DBSession.query(TodoItem).get(task_id)
        if task:
            DBSession.delete(task)
            DBSession.flush()  # Push to database
            DBSession.commit()  # Commit transaction
        return redirect('/')

    @expose()
    def edit_task(self, task_id, description):
        task = DBSession.query(TodoItem).get(task_id)
        if task and description.strip():
            task.description = description
            DBSession.flush()  # Push changes
            DBSession.commit()  # Commit transaction
        return redirect('/')
