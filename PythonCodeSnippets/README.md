## Python Code Snippets

1. Remove blank lines from a file:

```python
def remove_blank_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove blank lines
    lines = [line for line in lines if line.strip()]

    with open(output_file, 'w') as file:
        file.writelines(lines)

    print("Blank lines removed. Modified content saved to", output_file)


# Usage example
input_file = "input.txt"
output_file = "output.txt"

remove_blank_lines(input_file, output_file)
```

1. A nested for loop to iterate over a dictionary of dictionaries, 
printing a dictionary of dictionaries:  

```python
my_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25},
    'person3': {'name': 'Charlie', 'age': 35}
}

def print_dictofdicts():
	for key1, dict1 in my_dict.items():
		print("Key1:", key1)
		for key2, value in dict1.items():
			print("  Key2:", key2, "Value:", value)
            
print_dictofdicts()
```

2. Length of a list of lists given by a function like len() but returning a tuple: 

```python
def lenx2(listoflists):
    return (len(listoflists), len(listoflists[0])) 
```
