# Facebook Marketplace Recommendation Ranking System (AiCore)

Project that I'm working on as a part of my 'Data and AI' training at [AiCore](https://www.theaicore.com/).

![A screenshot of the AiCore portal](images/portal.png)

In the Facebook Marketplace Search Ranking project, we are asked to develop and train a multimodal model that accepts images and text. The output of the model will generate embedding vectors that are helpful to make recommendations to buyers using their demographic information. 
Once the model is trained, we will have to deploy it by creating an API using FastAPI, containerising it using Docker, and uploading it to an EC2 instance. The API will contain all the models that we create and train, so any new request can be processed to make predictions on the cloud. To ensure that the model can be easily modified without building a new image again, the files corresponding to each model will be bound to the Docker image, so it allows us to update the models with retrained models even after deploying them.

## 👀 Project overview 👀

- process and clean text and image datasets;
- design and train a multimodal model that combines images and text to generate embedding vectors to create a search index using Pytorch;
- create a pipeline to systematically clean new data and upsert it into a database;
- develop an API that encapsulates the models using FastAPI;
- deploy a container with the API using docker compose.

## Technologies

## Milestones 1-2

![An image of the technology structure](images/technology.png)

The first and second milestones of the project consist in setting up GitHub, creating a repository for the project, an AWS account, and going over the technology that we are asked to reproduce.

A nice introductory video that I encourage everyone to watch is available on the [AiCore YouTube Channel](https://youtu.be/1Z5V2VrHTTA).

## Milestone 3

In milestone 3, we're required to clean both the tabular and the image datasets, which are made available to us as EC2 instances on AWS.

### Tabular data cleaning

The tabular dataset contains information about the listing, including its price, location, and description. We are required to create a file named `clean_tabular_data.py` within our repository, which has to be populated with code to clean the tabular dataset.

The dataset was in a EC2 instance on AWS, which is accessed by ssh from the local machine.

Basically, the only cleaning that was required in this task was to convert the prices into a numerical format. This was done by removing the pound sign (£) and, for some entries, the comma (,).

### Image data cleaning