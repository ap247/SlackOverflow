# SlackOverflow - A Comments API
This is a backend API with the ability to read, upload, and delete comments. 

## How to Run
Ensure you have Docker Desktop installed and running on your computer. Also, ensure you have Postman or some API testing software on your computer

Clone this repo into your local machine and change directory to the repo in your terminal.

Follow the commands below:

```docker compose up -d db```

```docker compose build```

```docker compose up```

Now you can use localhost:8000 to test out the following routes:

### GET: localhost:8000/comments
Returns list of comments

### GET: localhost:8000/comments/read/{comment_id}
Returns a specific comment
- comment_id is the id of the comment you'd like to retrieve

### POST: localhost:8000/comments/create
Creates a comment with the details of JSON body and returns the comment with its associated id
- comment_id is the id of the comment you'd like to retrieve
Example:
```
{
    "author": "Adam",
    "text": "I enjoy using Jinja2 and YAML files to create modifiable templates for making reports",
    "date": "2015-09-01T13:15:00Z",
    "likes": 2,
    "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg"
}
```
Ensure that you have all the fields listed above

### PUT: localhost:8000/comments/update/{comment_id}
Updates a comment with the details of JSON body and specified id
Returns the details sent in JSON body:
- comment_id is the id of the comment you'd like to retrieve
Example with updated likes:
```
{
    "author": "Adam",
    "text": "I enjoy using Jinja2 and YAML files to create modifiable templates for making reports",
    "date": "2015-09-01T13:15:00Z",
    "likes": 3,
    "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg"
}
```
Ensure that you have all the fields listed above whether they gave updated values or not

### DELETE: localhost:8000/comments/delete/{comment_id}
Deletes a comment at the specified id:
- comment_id is the id of the comment you'd like to delete

## Ideas to continue the project
I would first relegate the entire django portion of the project to a backend folder and create a frontend folder with React components to manage user interaction. Then, I'd move docker-compose back into the root of the project to run all three parts (database, backend, and frontend) simulataneously.

## Sources Used 
dev.to/francescoxx, chat.openai.com, stackoverflow.com

