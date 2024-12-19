import easygui as g
import requests
import time
import json
import os

# Function used to craft the appropriate recipepuppy URL to access the API
def captureAndFetch():
    ingredientList = g.enterbox(msg="What is your main ingredient: ")
    joinedIngredients = ingredientList.replace(' ', ',')
    apiUrl = "https://www.themealdb.com/api/json/v1/1/filter.php?i=" + joinedIngredients
    return apiUrl

# Function used to send a request using the crafted URL and getting a response result in JSON format
def requestAndStore(captureAndFetchPrint):
    r = requests.get(captureAndFetchPrint)
    rJson = r.json()
    results = rJson['meals']
    if results is None:
        return bool(False)
    else:
        return(results)
    # return r.json()

# Function used to save a human-friendly formatted list of the results
def saveResults(requestSaved):
    i = 1
    with open('recipeResults.txt', 'w') as fo:
        pass
    if (requestSaved != False):
        with open('recipeResults.txt', 'w') as fo:
            for key in requestSaved:
                iAsString = str(i)
                message = 'Recipe ' + iAsString
                title = 'Title: ' + key['strMeal']
                # ingredients = 'Ingredients: ' + key['ingredients']
                recipeUrl = 'https://www.themealdb.com/meal/' + key['idMeal']
                url = 'Webpage: ' + recipeUrl
                fo.write(message + os.linesep + title + os.linesep + url + os.linesep + os.linesep)
                i = i + 1
    else:
        g.msgbox(msg='No recipes found. Please try again.', title='PyPy is Hungry - Recipe Results', ok_button='Exit')
        exit()

# Function used to open the saved results and displaying them in a window via easygui
def displayResults():
    with open('recipeResults.txt', 'r') as f:
        readData = f.read()
        # g.textbox(msg='Recipe Results', title='PyPy is Hungry', text=readData)
        g.msgbox(msg=readData, title='PyPy is Hungry - Recipe Results', ok_button='Exit')


def run():
    captureAndFetchPrint = captureAndFetch()
    requestSaved = requestAndStore(captureAndFetchPrint)
    saveResults(requestSaved)
    displayResults()

run()


