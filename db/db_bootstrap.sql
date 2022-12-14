CREATE DATABASE CHEF_IT_UP;
CREATE USER 'chef'@'%' IDENTIFIED BY 'chef123';
CREATE USER 'student'@'%' IDENTIFIED BY 'student123';
CREATE USER 'athlete'@'%' IDENTIFIED BY 'athlete123';
CREATE USER 'sudo_user'@'%' IDENTIFIED BY 'user123';
GRANT CREATE,ALTER,DROP,INSERT,UPDATE,DELETE ON CHEF_IT_UP.* TO 'chef'@'%';
GRANT SELECT ON CHEF_IT_UP.* TO 'student'@'%';
GRANT SELECT ON CHEF_IT_UP.* TO 'athlete'@'%';
GRANT ALL PRIVILEGES ON CHEF_IT_UP.* TO 'sudo_user'@'%';
FLUSH PRIVILEGES;

-- Move into the database we just created
USE CHEF_IT_UP;

-- Put your DDL
CREATE TABLE Athlete (
    BMI DECIMAL,
    Sport CHAR(30),
    MacroGoals TEXT,
    [Weight] INT,
    Height INT,
    BodyFat DECIMAL,
    PRIMARY KEY AthleteID INT
);

CREATE TABLE Macros (
    Calories INT,
    Carbs INT,
    Fat INT,
    Protein INT,
    RecipeName TEXT,
    AthleteGoals TEXT,
    RecipeNutrition TEXT,
    AthleteID INT,
    PRIMARY KEY (AthleteID< AthleteGoals),
    CONSTRAINT fk_1
        FOREIGN KEY (AthleteGoals) REFERENCES Athlete (MacroGoals),
    CONSTRAINT fk_9
        FOREIGN KEY (AthleteID) REFERENCES Athlete (AthleteID)
);

-- Put your DDL
CREATE TABLE Chef (
    Rating DECIMAL,
    TotalRecipes INT,
    Experience DECIMAL,
    PRIMARY KEY ChefID INT,
    SpecialityName VARCHAR(10)
);

-- Put your DDL
CREATE TABLE Specialty (
    SpecialityName VARCHAR(20),
    ChefID INT,
    Region VARCHAR(10),
    Nationality CHAR(30),
    PRIMARY KEY (ChefID, SpecialityName),
    CONSTRAINT fk_2
        FOREIGN KEY (ChefID) REFERENCES Chef (ChefID)
);

-- Put your DDL
CREATE TABLE Student (
    PRIMARY KEY StudentID INT,
    SchoolName TEXT,
    SchoolYear INT,
    Major CHAR(20),
    Minor CHAR(20),
    Budget DECIMAL
);

-- Put your DDL
CREATE TABLE Ingredient (
    PRIMARY KEY IngredientName CHAR(30),
    Price DECIMAL,
    Calories INT,
    Quantity DECIMAL,
    AgeOfIngredient DECIMAL,
    FoodType VARCHAR(30)
);

-- Put your DDL
CREATE TABLE FoodGroup (
    PRIMARY KEY FoodID INT,
    Fruit CHAR(30),
    Vegetables CHAR(30),
    Grains CHAR(30),
    Meats CHAR(30),
    Dairy CHAR(30),
    Other CHAR(30),
    CONSTRAINT fk_3
        FOREIGN KEY (FoodID) REFERENCES Ingredient (FoodType)
);

-- Put your DDL
CREATE TABLE Recipe (
    PRIMARY KEY RecipeID INT,
    RecipeName CHAR(30),
    DifficultyLevel DECIMAL,
    Price DECIMAL,
    TimeToCook INT,
    Rating DECIMAL,
    Servings DECIMAL,
    NutritionalValue CHAR(30),
    CONSTRAINT fk_4
        FOREIGN KEY (NutritionalValue) REFERENCES Macros (RecipeNutrition)
); 

-- Put your DDL
CREATE TABLE DietaryRestrictions (
    PRIMARY KEY RecipeID INT,
    RecipeName CHAR(30),
    LactoseIntolerant Boolean,
    Vegan Boolean,
    Kosher Boolean,
    Vegetarian Boolean,
    Halal Boolean,
    CONSTRAINT fk_5
        FOREIGN KEY (RecipeID) REFERENCES Recipe (RecipeID)
);

-- Put your DDL
CREATE TABLE Favorites (
    UserID INT,
    RecipeID INT,
    PRIMARY KEY(UserID, RecipeID),
    CONSTRAINT fk_6
        FOREIGN KEY (RecipeID) REFERENCES Recipe(RecipeID),
    CONSTRAINT fk_7
        FOREIGN KEY (UserID) REFERENCES User(UserID),
);

-- Put your DDL
CREATE TABLE User (
    FirstName CHAR(30),
    LastName CHAR(30),
    PRIMARY KEY UserID INT,
    Email CHAR(50),
    Age INT,
    City CHAR(300),
    [State] CHAR(30),
    Country CHAR(30),
    ReviewsLeft VARCHAR(1000),
    FavoriteRecipes VARCHAR(1000)
);

-- Put your DDL
CREATE TABLE Review (
    PRIMARY KEY RecipeID INT,
    RecipeName CHAR(30),
    Rating DECIMAL,
    Comments VARCHAR(2000),
    CONSTRAINT fk_8
        FOREIGN KEY (RecipeID) REFERENCES User(ReviewsLeft)
);

-- Add sample data
INSERT INTO Athlete
    (AthleteID,BMI,Sport,MacroGoals,[Weight],Height,BodyFat)
    VALUES
    (00000, 24, 'Track', '450 Calories 50g protein',  156, 75, 23.1);

-- Add sample data
INSERT INTO Macros
    (AthleteID, Calories,Carbs,Fat,Protein,RecipeName,AthleteGoals, RecipeNutrition)
    VALUES
    (00000, 2400, 54, 34,  156, "Salad", '3404 calories 19g carbs', 'Salad Recipe');

-- Add sample data
INSERT INTO Chef
    (Rating, TotalRecipes, Experience, ChefID, SpecialityName)
    VALUES
    (4.1, 43, 3.1, 23552, 'Italian');

-- Add sample data
INSERT INTO SpecialityName
    (SpecialityName, ChefID, Region, Nationality)
    VALUES
    ('Italian', 78365, 'Kanto', 'Japan');

-- Add sample data
INSERT INTO Student
    (StudentID, SchoolName, SchoolYear, Major, Minor, Budget)
    VALUES
    (12433, 'Northeastern', 3, 'Computer Science', 'Economics', 24.34);

-- Add sample data
INSERT INTO Ingredient
    (IngredientName, Price, Calories, Quantity, AgeOfIngredient, FoodType)
    VALUES
    ('Lettuce', 3.43, 6, 1.0, 1, 'Vegetable');

-- Add sample data
INSERT INTO FoodGroup
    (FoodID, Fruit, Vegetables, Grains, Meats, Dairy, Other)
    VALUES
    (1214, 'Apple', 'Lettuce', 'Bread', 'Goat', 'Milk', 'Insect');

-- Add sample data
INSERT INTO Recipe
    (RecipeID, RecipeName, DifficultyLevel, Price, TimeToCook, Rating, Servings, NutritionalValue)
    VALUES
    (1233, 'Pasta', 1, 45.22, 600, 5, 12, '45 calories 80g protein');

-- Add sample data
INSERT INTO DietaryRestrictions
    (RecipeID, RecipeName, LactoseIntolerant, Vegan, Kosher, Vegetarian, Halal)
    VALUES
    (12424, 'Pasta', True, True, True, True, True);

-- Add sample data
INSERT INTO Favorites
    (UserID, RecipeID)
    VALUES
    (1361, 434344);

-- Add sample data
INSERT INTO User
    (FirstName, LastName, UserID, Email, Age, City, [State], Country, ReviewsLeft, FavoriteRecipes)
    VALUES
    ('Chief', 'Keef', 1243, 'chiefkeef@keef.com', 23, 'Chicago', 'Illinois', 'USA', 'Pasta, Salad', 'Pasta, Salad');

-- Add sample data
INSERT INTO Review
    (RecipeID, RecipeName, Rating, Comments)
    VALUES
    (24313, 'Salad', 4.3, 'Gas');