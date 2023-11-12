# Make-kids-Great-Again
Junction 2023

![Screenshot_from_2023-11-12_09-20-10](https://github.com/Palpatox/Make-kids-Great-Again/assets/94328315/bb9c635f-1198-4122-98ab-cea3619bc324)

# Description
After the pandemic, the bonding of younger generation has suffered a lot, and they tend to have less physical activities  and social life than they used to. In fact if you look a little on google, you see that: "The SARS‐CoV‐2 COVID‐19 pandemic has disrupted the habits and social world of all individuals. Health measures and social restrictions taken to curb the spread of the virus directly affect the way in which individuals engage in social interactions, and how they develop and maintain social ties more generally."Now, many kids come to school, spend break times on social medias, maybe talk to some friends and then return home right after classes.

To break this momentum of antisocial behaviour and lack of activity, we thought about the ways we made contacts with our friends and spent some quality time together. We realized that the best contacts we had through the pandemic were party games. As we browsed through the play store, we realized that the party game catalogues are always entirely on the phone and don't require physical interactions, nor to be together in one place(ex: Uno, Monopoly, undercover,...).
To help the kids play together, have them meet physically, make stronger bonds or even an easy first contact in a group, we decided to build an app that provides multiple party games to challenge  anyone on small and fun games where they perform physical activities to some degree. 
To help the first contact with the app, we developped some games included originaly such as:

![Screenshot_from_2023-11-12_09-24-13](https://github.com/Palpatox/Make-kids-Great-Again/assets/94328315/ad238430-fab9-46f5-be4e-e19d3d74d75d)


## programed here
Game 1: rope jumping highest amount on one minute win

Game 2: Green light red light game


## future possibilities examples
Game 2: 360 picture of the environment then phone asks kids to get a picture of something within asap.

Game 4: Real life game with tasks and aliens

Game 5: Synch dance where you have to follow the moves of a player

Our purpose is to offer a sandbox app, where kids can express their creativity by making new game mods from a simple system and share them.  We offer a platform where it is easy to add a new games, and join groups that you meet in real life. Then, to ignite the competitiveness of the youth, we added a ranking system where the best players will be displayed in real time in the menu.

![Screenshot_from_2023-11-12_09-24-18](https://github.com/Palpatox/Make-kids-Great-Again/assets/94328315/1328af11-dad6-44d4-9fd4-bba0a0794238)

To improve the commitment of the kids, we added a monthly ranking to encourage the kids to play regularly, show off their skills and therefore enjoy some fun time with their friends an a little physical activities.

In the end, these contacts powered by the platform will help the kids to communicate more, provide discussion topics and build a dynamic in their life. We believe that increasing these contacts will improve the mental growth of the kids, but also their communication skills. We need to re ignite the youth dynamic ! 


# File Structure
The application is organized into several Python files and templates:

Main Flask Application File: This is the central file where the Flask application is defined and configured.
Game Modules: Separate Python files for each game (jump.py, redgreen.py) are included. These files contain the logic and routing for each game.
Template Folder: Contains HTML templates (mainpage.html, playpage.html, create_loby.html) used to render the frontend of the web application.

# Features
Flask Setup

Flask Application: An instance of the Flask application is created.

Blueprints: The application utilizes Flask Blueprints to organize and manage different sections of the site, each dedicated to a specific game (jump_blueprint, red_blueprint).

# Routing
Main Page (/mainpage): Renders the mainpage.html template.

Play Page (/playpage): Renders the playpage.html template.

Create Lobby (/createloby): Renders the create_loby.html template.

# Game Integration
Each game is integrated as a Blueprint, allowing for modular development and ease of navigation.
The games are accessible through distinct URLs (/jump for the Jump game and /redgreen for the Red-Green game).
Running the Application

The application is configured to run on 0.0.0.0 (making it accessible from other machines in the network) on port 5000.
Debug mode is enabled for development purposes, providing detailed error logs and live reloading of the application.

# Dependencies
Flask: The web framework used for building the application.

NumPy and SciPy: Used in the game logic for mathematical computations.

HTML/CSS: For structuring and styling the web pages.

# Usage
Starting the Application: Run the main Python file to start the Flask server.

Accessing the Games: Navigate to /jump or /redgreen in your web browser to play the games.

Navigating the Site: Use the provided routes to navigate between the main page, play page, and lobby creation page.

# Development Notes
Debug Mode: Remember to turn off debug mode in a production environment for security reasons.

Template Customization: The HTML templates can be customized to change the look and feel of the application.

# Conclusion
This Flask web application offers a simple yet effective platform for hosting browser-based games. Its modular structure and use of Flask Blueprints make it scalable and easy to maint
