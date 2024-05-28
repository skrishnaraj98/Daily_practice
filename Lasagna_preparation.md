```python
%%writefile lasagna_prep.py

# This is a very basic python code to write a logic to understand how much time it takes 
# to make a lasagna dish within certain explicit conditions. 

EXPECTED_BAKE_TIME=60      #in minutes
EXPECTED_PREP_TIME=2       #in minutes for a single layer of lasagna

def bake_time(spent_time):
    """
    :param spent_time: int - baking time elapsed. 
    :return: int - total baking time elapsed. 
    
    This function takes in an int argument (in minutes) which represents the baking time elapsed. 
    And returns the baking time in minutes. 
    
    """
    return spent_time

def remaining_time(spent_time):
    """
    This function doesn't have any parameters and returns the remaining time from EXPECTED_BAKE_TIME.
    
    """
    return EXPECTED_BAKE_TIME - spent_time

def prepartion_time(layers): 
    """
    :param layers: int - represents the number of layer that we wish to add within the dish. 
    :return: int - represents the total time (in minutes) in preparing the layers of the dish. 
    
    This function takes in layers as the arguments representing the number of layers and then returns
    the time in minutes it takes to prepare all of the layers for the lasagna dish. 
    
    """
    return layers*EXPECTED_PREP_TIME

def total_time_elapsed(layers, spent_time):
    """
    This function doesn't take any arguments and returns the total time (prep+bake) elapsed in 
    cooking the lasagna dish. 
    
    """
    return (prepartion_time(layers) + bake_time(spent_time))
```

    Overwriting lasagna_prep.py
    


```python
import lasagna_prep

print("Baking time elapsed:",lasagna_prep.bake_time(20),"minutes")
print("Remaining time in Baking:",lasagna_prep.remaining_time(20),"minutes")
print("Lasagna layers prep time:",lasagna_prep.prepartion_time(8),"minutes")
print("Total time Layers prep + bake:",lasagna_prep.total_time_elapsed(8,20),"minutes")
```

    Baking time elapsed: 20 minutes
    Remaining time in Baking: 40 minutes
    Lasagna layers prep time: 16 minutes
    Total time Layers prep + bake: 36 minutes
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
