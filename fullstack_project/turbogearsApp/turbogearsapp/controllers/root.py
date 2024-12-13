from tg import expose, redirect, request
from tg.controllers import TGController
from turbogearsapp.model import DBSession, TodoItem


from tg import expose, redirect
from tg.controllers import TGController
from turbogearsapp.model import DBSession, TodoItem

class RootController(TGController):
    @expose('tasks.xhtml')  # Render the tasks.xhtml template
    def index(self):
        tasks = DBSession.query(TodoItem).all()  # Retrieve all tasks
        print("Retrieved tasks:", [(task.id, task.description) for task in tasks])  # Debug: Print tasks
        # Convert tasks into a list of dictionaries
        tasks_data = [{'id': task.id, 'description': task.description} for task in tasks]
        print("Tasks passed to template:", tasks_data)  # Debug: Print converted tasks
        return dict(tasks=tasks_data)  # Pass the data to the template

    @expose()
    def add_task(self, description):
        print("Adding task:", description)  # Debug: Show submitted description
        if description.strip():
            new_task = TodoItem(description=description)
            DBSession.add(new_task)
            DBSession.flush()  # Ensure changes are flushed to the database
            DBSession.commit()  # Commit transaction
        return redirect('/')

    @expose()
    def delete_task(self, task_id):
        print("Deleting task with ID:", task_id)  # Debug: Show task ID
        task = DBSession.query(TodoItem).get(task_id)
        if task:
            DBSession.delete(task)
            DBSession.flush()  # Ensure changes are flushed to the database
            DBSession.commit()
