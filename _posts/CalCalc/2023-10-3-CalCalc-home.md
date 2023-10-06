---
comments: true
layout: post
title: Calorie Calculator
type: hacks
courses: { compsci: {week: 7} }
permalink: /CalCalc/home
---

{% include nav_CalCalc.html %}

## Welcome to our Daily Calorie Maintenance Calculator

For our passion project we decided to create a program that calculates the number of calories you need to consume each day in order to maintain your weight. Thi prpgram can help you on your journey to gain or lose weight and obtain your dream physique, promoting a healthier lifestyle. 

<p>Try our program by clicking the "Calculate" Button below:</p>
<button><a href="https://www.google.com/search?sca_esv=569384727&q=smurf+cat+meme&tbm=vid&source=lnms&sa=X&ved=2ahUKEwidooPHqM-BAxXKMUQIHRsGCGEQ0pQJegQICRAB&biw=1440&bih=702&dpr=2&safe=active&ssui=on#fpstate=ive&vld=cid:b4627ef3,vid:Gmc00FKuH70,st:0">Click to see Smurf Cat Before you use the Calculator</a></button>

# Calorie Calculator

Fill out the form below to calculate your daily calorie requirement.

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calorie Calculator</title>
</head>
<body>
    <h1>Calorie Calculator</h1>
    <form id="calorieForm">
        <label for="age">Age:</label>
        <input type="number" id="age" required><br><br>
        
        <label for="gender">Gender:</label>
        <select id="gender" required>
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select><br><br>
        
        <label for="weight">Weight (kg):</label>
        <input type="number" id="weight" required><br><br>
        
        <label for="height">Height (cm):</label>
        <input type="number" id="height" required><br><br>
        
        <label for="activity">Activity Level:</label>
        <select id="activity" required>
            <option value="sedentary">Sedentary</option>
            <option value="lightly active">Lightly Active</option>
            <option value="moderately active">Moderately Active</option>
            <option value="very active">Very Active</option>
            <option value="extra active">Extra Active</option>
        </select><br><br>
        
        <input type="submit" value="Calculate">
    </form>

    <div id="result"></div>

    <script>
        document.getElementById("calorieForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const age = parseFloat(document.getElementById("age").value);
            const gender = document.getElementById("gender").value;
            const weight = parseFloat(document.getElementById("weight").value);
            const height = parseFloat(document.getElementById("height").value);
            const activity = document.getElementById("activity").value;

            // Send a POST request to the Python backend using relative path
            fetch("/_posts/CalCalc/2023-10-3-CalCalc-backend.py", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ age, gender, weight, height, activity }),
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").innerHTML = `Your daily calorie requirement is approximately ${data.calories.toFixed(2)} calories.`;
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    </script>
</body>
</html>



## Thank You for using Our Program!!
