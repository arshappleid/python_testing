# How the tests were created.
Initially since we were allowed to choose any language , or any framework to create the gists. I decided to do some reasearch online for simple easy libraries or framework. Whilst also going through the github documentation. After reading through the github documentation , i realized making up bashscripts would be the simplest and easiest way. Here onwards i started testing the api requests using postman , and was successfull , in making api calls.

Although previous method would have limited the reusability of the code. Thus after doing more research i found the *gistyc* library , and read through a [tutorial](https://towardsdatascience.com/gistyc-a-python-based-github-gist-management-toolkit-ee507d5a0e7b) . This framework allowed me to easily make github api requests , with minimal code . Later I wrote functions to create / update / delete gists, using [documentation](https://pypi.org/project/gistyc/) from the python library. 

 

# Writing out tests for my functions:

To test out my functions, i simply used the pytest library . Then used the response data , to see if it matched with the initial parameters provided to write the tests . I choose this method as i knew it would allow me to easily carry out my tests on a dockerized containor , using github workflows. Therefore after writing out my functions, and my tests , i set up my dockerized containor on github. The benefit of using github workflows for this task , allowed me to carryout my tests automatically everytime i pushed my work to the [repo](https://github.com/arshappleid/python_testing).



## Challenges I faced.

Initially the most toughest part of the assignment was to choose which language or framework to use. As there were many possible ways in my opinion to do this. Although i belive having chosen python for this task , and the framework gistyc was a great decision. This gave me enough time to learn how the api works, and easily write tests for my functions.



## How to run the code.

1. Make sure you have python 3.5 > installed on your machine.
2. Navigate into the project directory (python_testing).

#### Creating a new Gist.

1. Open ```main.py``` then enter the dynamic name of the file, that you want to add to your gist.
2. Run the script from terminal using ```python3  "main.py" ```.

### Other Function

1. update_gist(filePath, gistId) - Updates the gist with the new file, whose filePath has been given. Also requires the gistId , for the gist that is being updated.
2. delete_gist(filePath)



## How to run tests

1. Run the command in terminal : ```python3 "test_github_functions.py" ```. Whilst being in the main directory.

## Extra Notes :

Since i did not make use of the traditional https , way of creating gists in API. The idea of requiring "User agent" parameter is kind of obsolete or non-relevant for my code.

