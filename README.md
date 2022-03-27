# Room Reservation System

## Introduction
Welcome to my project for a room reservation system. This project is a simple room reservation system, allowing users to choose from two cabins to reserve from. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The user will be able create, read, update and delete their user profile and table booking.

A live website can be found [here](https://)

![Website Preview](assets/images-readme/)

# 1. UX

I have always loved to travel, explore and to experience new places. When I do this I enjoy looking at travel websites to find accomodation which meets my needs and looks most appealing. The most common way to do this is to make a reservation for a room on a holiday accomodation website. 

This project will showcase simplicity and ease to reserve a cabin, update a reservation, cancel a reservation, create a personal profile and update a profile.

## 1.1. Strategy

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user profile and create/update/delete a cabin booking in a simple and effective process.

### User Goals:
First Time Visitor Goals

- As a first-time visitor, I want to reserve a cabin at my chosen date and add notes to my reservation if needed.
- As a first-time visitor, I want to view the cabin types and understand what they have to offer so that I can decide if I would like to make a reservation or not.
- As a first-time visitor, I want to be able to contact the owner of the website with ease.

### Returning Visitor Goals

- As a returning visitor, I want to update my reservation details.
- As a returning visitor, I want to cancel a reservation I have already made.
- As a returning visitor, I want to edit my profile for any future reservation.

Frequent User Goals

- As a frequent user, I want to check to see if there are any new cabins to book or any further facilities added.

### User Expectations:
- The system should have a simple user interface, with the navigation to each section clear and concise.
- The accomodation offering is clear to understand.
- The user interface is easy to navigate.
- The website is responsive on all devices.
- To have the ability to contact the owner site for any enquiries.

### User Stories

Throughout the project I used the GitHub Kanban project board to log all user stories as my project management tool. This helped me to keep focus on the necesarry tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed.

![User Stories](assets/images-readme/)

# 6. Deployment

I used the terminal to deploy my project locally. To do this I had to:

- Create a repository on GitHub.
- Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
- Open the terminal within GitPod
- Enter "python3 manage.py runserver into the terminal.
- Go to local host address on my web browser.
- All locally saved changes will show up here.

For the final deployment to Heroku, I had to:

- Uncomment the PostgreSQL databse from my settings.py file.
- Set debug = False in my settings.py file.
- Commit and push all files to GitHub
- In Heroku, remove the DISABLE_COLLECTSTATIC config var.
- In the deploy tab, go to the manual deploy sections and click deploy branch.

# 7. End Product

# 8. Known Bugs

# 9. Credits