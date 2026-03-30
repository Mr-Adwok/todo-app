from app.db.session import get_session
from starlette.requests import Request
from app.services.all_services import TodoService
from starlette.responses import JSONResponse
# from app.schemas.schema import  CreateTodo





async def create_task2(request:Request):

	try:
		content = await request.json()

		title = content.get("title")
		description = content.get("description")

		if title is None :
			return JSONResponse({"data":"title empty"})

		if title == "":
			return JSONResponse({"title":"empty string"})

		data = {"title": title, "description": description}
		async for session in get_session():
    		 new_todo = await todo_service.create_todo(data, session)
		todo_dict = {
		    "title": new_todo.title,
		    "description": new_todo.description,
		    "created_at": new_todo.created_at.isoformat(),
		    "uid": str(new_todo.uid)
		}

		return JSONResponse(todo_dict, status_code=201)

	except Exception as e:
         return JSONResponse({"detail": str(e)}, status_code=400)




# async def create_task2(request:Request):

# 	try:
# 		content = await request.json()

# 		title = content.get("title")
# 		description = content.get("description")

# 		if title is None :
# 			return JSONResponse({"data":"title empty"})

# 		if title == "":
# 			return JSONResponse({"title":"empty string"})

# 		data = {
# 			"title":title
# 			"content":content

# 		}
# 		async for session in get_session():
#             # Create the Todo in DB
#             new_todo = await todo_service.create_todo(data, session)



















# Existence validation
# Type validation
# Format validation
# Constraint validation











# Yes, exactly. Programming usually follows a **clear pattern (or flow)** to solve a problem. When you remove **Pydantic**, the pattern still exists — you just perform validation **manually**.

# I’ll show you the **conceptual pattern**, not code.

# ---

# # Pattern of Writing an API Without Pydantic

# Think of it like a pipeline:

# ```
# Client → Router → Parse Request → Manual Validation → Service Logic → ORM/Database → Serialization → Response
# ```

# Now let’s break the pattern step-by-step.

# ---

# # 1. Receive the Request

# The server receives an HTTP request from the client.

# Purpose:

# * accept the request
# * identify the endpoint
# * pass the request object to your handler

# Example concept:

# ```
# POST /tasks
# ```

# Frameworks like **Starlette** route this to the correct function.

# ---

# # 2. Parse the Request Data

# Extract the data sent by the client.

# Possible sources:

# * JSON body
# * query parameters
# * path parameters
# * headers

# Goal:

# ```
# Request body → native Python structure
# ```

# Usually this becomes a **dictionary-like structure**.

# ---

# # 3. Manual Validation

# Since you removed **Pydantic**, you must check everything yourself.

# Typical checks:

# Validation categories:

# ```
# Existence validation
# Type validation
# Format validation
# Constraint validation
# ```

# Examples conceptually:

# ```
# Field exists?
# Correct type?
# Correct format?
# Meets business rules?
# ```

# Example rules:

# ```
# title must exist
# title must be string
# description optional
# length constraints
# ```

# If validation fails:

# ```
# Return HTTP error response
# Stop execution
# ```

# ---

# # 4. Normalize / Prepare Data

# After validation, you prepare the data so the rest of the system can use it.

# Examples:

# ```
# convert types
# remove extra fields
# structure the data
# ```

# Goal:

# ```
# validated input → clean internal data structure
# ```

# ---

# # 5. Call the Service Layer

# The router should not contain business logic.

# Instead it calls a **service**.

# Pattern:

# ```
# Router → Service
# ```

# The service handles:

# ```
# business rules
# application logic
# workflow
# ```

# Example logic:

# ```
# create task
# calculate something
# trigger other processes
# ```

# ---

# # 6. Interact With the Database

# The service communicates with the database through an ORM like **SQLAlchemy**.

# Typical steps:

# ```
# create model object
# add to session
# commit transaction
# refresh object
# ```

# Goal:

# ```
# store data persistently
# ```

# ---

# # 7. Serialize the Data

# Database objects are not directly JSON.

# So you convert them to a **JSON-friendly structure**.

# Typical transformations:

# ```
# UUID → string
# datetime → ISO string
# ORM object → dictionary
# ```

# This process is called:

# ```
# serialization
# ```

# ---

# # 8. Build the Response

# The final step is creating the HTTP response.

# This includes:

# ```
# response body
# status code
# headers
# ```

# Example concept:

# ```
# 201 Created
# JSON response
# ```

# Frameworks like **Starlette** send it back to the client.

# ---

# # The Full Mental Model

# When writing APIs **without Pydantic**, your mental model becomes:

# ```
# 1 Receive request
# 2 Parse request data
# 3 Validate manually
# 4 Prepare/normalize data
# 5 Execute service logic
# 6 Interact with database
# 7 Serialize output
# 8 Send HTTP response
# ```

# ---

# # The Big Insight

# When using **Pydantic**, steps **3 and 4** become automated.

# So the flow becomes:

# ```
# Request
#  ↓
# Pydantic validation
#  ↓
# Service logic
#  ↓
# Database
#  ↓
# Response
# ```

# But understanding the **manual pattern first** makes you a **much stronger backend developer**.

# ---

# If you want, I can also show you something **very powerful backend engineers learn**:

# **the 6 architectural layers of an API**, which is the deeper structure behind the pattern you’re learning.
