
## Python Inquirer 

The Python Inquirer package provides a nice CLI user interface: 

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  

```python
import random
import inquirer

def random_number_loop():
    while True:
        msg = ('\n' *12) + (' ' * 30) + str(random.randint(1, 100)) + "\n\n\n" + (' ' * 30) + "type anything to continue" +  "\n" + (' ' * 30) + "type 'x' to exit" + "\n"  
        questions = [
            inquirer.Text('input', message=msg) 
        ]
        answer = inquirer.prompt(questions)['input']
        if answer == 'x': 
            break            
if __name__ == '__main__':
    random_number_loop()
```

- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  

```python
import inquirer

# print message to the console
print("Welcome to the program!")

# define the question
questions = [
    inquirer.Text("name", message="What is your name?")
]

# prompt the user for input
answers = inquirer.prompt(questions)

# print the user's name
print("Hello,", answers["name"])
```

- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

```python
import inquirer

# ask if user is ready
ready = inquirer.prompt([inquirer.Confirm('ready', message="Are you ready?")])

if ready['ready']:
    # prompt the user for their name
    questions = [
        inquirer.Text("name", message="What is your name?")
    ]
    answers = inquirer.prompt(questions)

    # greet the user
    print("Hello,", answers["name"])
else:
    # say goodbye
    print("Ok, then try again later. Goodbye.")
```


