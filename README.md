# MyScoop
Track your favorite ice cream using Scrapy and Django

## Description
This is a project I built as part of my software development capstone course at Minneapolis Technical and Community College. My goals for the project were to explore Scrapy, Django and Postgres.

## Application Features
 - Scrape the flavors of ice cream available at a local ice cream shop using Scrapy
 - Create a web app using Django that allows users to:
  - choose their favorite flavors
  - be notified by email when their favorites are available
  - see the last time a flavor was available
  - write reviews of flavors
  - get flavor recomendations

## Requirements
 - Python
 - Django
 - Scrapy
 - Postgres 

## Instructions
 - From the scoopscraper directory run `$ scrapy crawl izzy_spider` to populate the database
 - From the my_scoop directory run `$ python manage.py runserver`
 
