# Your Application Name: BoardGame Recommender

## Description
This application is designed to recommend board games based on user preferences. It takes in a range of desired player count, age, and playtime, then recommends the top 10 games fitting those criteria. It can also provide the top 30 games based on average rating, irrespective of the user's preferences.

The core logic of the recommendation is built on a `Data` class that handles data filtering and ranking. Additionally, a `Graph` class is used for data visualization.

### First page
![First page](C:\Users\Win10\Desktop\Recommender_board_game\begin_page.jpg)
### Second page
![Second_page](C:\Users\Win10\Desktop\Recommender_board_game\DisplayandInput_page.jpg)
### Graph page
![Graph page](C:\Users\Win10\Desktop\Recommender_board_game\graph_page.jpg)

[Link to Demonstration Video](https://your-video-link.com)

## Data Sources
The application uses a CSV file as its primary data source. This CSV file, `boardgames1.csv`, contains a comprehensive list of board games along with various attributes such as minimum players, maximum players, minimum age, minimum playtime, maximum playtime, and average rating.

## Running the Application
To run this application, you will need Python 3 and the following Python libraries:
- pandas
- matplotlib
- tkinter
- pillow
- seaborn

After installing the dependencies, you can run the application by executing the main Python script in your terminal.

```bash
python3 main.py
```

## Design
The application is designed with two main classes: `Data` and `Graph`.

- The `Data` class is responsible for reading the data from the CSV file, filtering the data based on user input, and providing recommendations.
- The `Graph` class is used for generating different types of plots for data visualization.

### UML Class Diagram
![UML diagram](C:\Users\Win10\Desktop\Recommender_board_game\boardgames_uml.jpg)

### Sequence Diagram
![UML diagram](C:\Users\Win10\Desktop\Recommender_board_game\boardgames_sequence_diagram.png)

## Design Patterns Used
The application doesn't explicitly use any specific design pattern, but it does follow good object-oriented programming practices by encapsulating data manipulation and visualization logic within separate classes.
I don't sure is it count as MVC pattern (Model–view–controller)

## Graph Algorithm Used
This application utilizes network graphs to establish connections between board game designers and game categories. Each node in the graph represents either a designer or a category, with an edge between a designer and a category indicating that the designer has created a game within that category.

The graph algorithm employed here is a ranking algorithm based on node degree. In the context of this application, the degree of a node corresponds to the number of connections (or edges) it has. The degree of a designer node signifies the number of categories in which the designer has created a game. The application uses this algorithm to identify the top 10 most connected designers, meaning the designers associated with the most categories. This algorithm, while being a form of graph algorithm, does not involve finding the shortest path between nodes.

## Other Information
This project was a great opportunity to learn and apply data manipulation and visualization techniques using pandas and matplotlib. It provides a practical application of data analysis in the context of game recommendations, which can be further expanded and refined to include more complex criteria and machine learning algorithms. Also tkinter is the basic GUI that really fun to design and it has many feature to play with.