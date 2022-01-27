#!/usr/bin/env python
# coding: utf-8

# # Table Functions
# 

# In[1]:


import numpy as np
from datascience import *


# In[2]:


population_amounts = Table.read_table("world_population.csv").column("Population")
years = np.arange(1950, 2015+1)
print("Population column:", population_amounts)
print("Years column:", years)


# In[3]:


population = Table().with_columns(
    "Population", population_amounts,
    "Year", years
)
population


# ## 1. Creating Tables

# In[4]:


top_10_movie_ratings = make_array(9.2, 9.2, 9., 8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.8)
top_10_movie_names = make_array(
        'The Shawshank Redemption (1994)',
        'The Godfather (1972)',
        'The Godfather: Part II (1974)',
        'Pulp Fiction (1994)',
        "Schindler's List (1993)",
        'The Lord of the Rings: The Return of the King (2003)',
        '12 Angry Men (1957)',
        'The Dark Knight (2008)',
        'Il buono, il brutto, il cattivo (1966)',
        'The Lord of the Rings: The Fellowship of the Ring (2001)')

top_10_movies = Table().with_columns("Name",top_10_movie_names,
                                    "Rating",top_10_movie_ratings)
top_10_movies


# In[6]:


imdb = Table.read_table("imdb.csv")
imdb


# ## 2. Using lists

# In[8]:


# Run this cell to recreate the table
flowers = Table().with_columns(
    'Number of petals', make_array(8, 34, 5),
    'Name', make_array('lotus', 'sunflower', 'rose')
)
flowers


# In[9]:


my_flower = [42,'Jason F']
my_flower


# In[11]:


# Use the method .with_row(...) to create a new table that includes my_flower 

four_flowers = flowers.with_row(my_flower)

# Use the method .with_rows(...) to create a table that 
# includes four_flowers followed by other_flowers

other_flowers = [[10, 'lavender'], [3, 'birds of paradise'], [6, 'tulip']]

seven_flowers = four_flowers.with_rows(other_flowers)
seven_flowers


# ## 3. Analyzing datasets

# In[13]:


Rating_Num=imdb.column("Rating")
Rating_Num


# In[14]:


highest_rating = max(Rating_Num)
highest_rating


# In[16]:


imdb.sort("Rating")


# In[17]:


imdb.sort("Rating", descending=True)


# In[18]:


imdb_by_year = imdb.sort('Year')
imdb_by_year


# In[20]:


sort_name=imdb_by_year.column('Title')
earliest_movie_title = sort_name.item(0)
earliest_movie_title


# ## 4. Finding pieces of a dataset

# In[22]:


forties = imdb.where('Decade', are.equal_to(1940))
forties


# In[23]:


Rating_Column=forties.column('Rating')
average_rating_in_forties = np.average(Rating_Column)
average_rating_in_forties


# In[25]:


ninety_nine = imdb.where('Year',are.equal_to(1999))
ninety_nine


# 
# |Predicate|Example|Result|
# |-|-|-|
# |`are.equal_to`|`are.equal_to(50)`|Find rows with values equal to 50|
# |`are.not_equal_to`|`are.not_equal_to(50)`|Find rows with values not equal to 50|
# |`are.above`|`are.above(50)`|Find rows with values above (and not equal to) 50|
# |`are.above_or_equal_to`|`are.above_or_equal_to(50)`|Find rows with values above 50 or equal to 50|
# |`are.below`|`are.below(50)`|Find rows with values below 50|
# |`are.between`|`are.between(2, 10)`|Find rows with values above or equal to 2 and below 10|
# 
# 

# In[27]:


really_highly_rated = imdb.where('Rating',are.above(8.5))
really_highly_rated


# In[29]:


century_20th = imdb.where('Year',are.between(1899,2000))
rating_20th = century_20th.column ('Rating')                    
average_20th_century_rating = np.average(rating_20th)
                          
century_21th = imdb.where('Year',are.above(1999))  
rating_21th = century_21th.column ('Rating')  
average_21st_century_rating = np.average(rating_21th)
print("Average 20th century rating:", average_20th_century_rating)
print("Average 21st century rating:", average_21st_century_rating)


# In[31]:


num_movies_in_dataset = imdb.num_rows
num_movies_in_dataset


# In[32]:


num_20 = imdb.where('Year', are.between(1899,2000))
proportion_in_20th_century = num_20.num_rows / 250
num_21 = imdb.where('Year', are.above(1999))
proportion_in_21st_century = num_21.num_rows / 250
print("Proportion in 20th century:", proportion_in_20th_century)
print("Proportion in 21st century:", proportion_in_21st_century)


# In[34]:


even_number = imdb.column('Year') % 2
even_year_table = imdb.with_columns(
    'Division', even_number)
num_even_year = even_year_table.where ('Division', are.equal_to(0))
num_even_year_movies = len(num_even_year.column('Division'))
num_even_year_movies


# In[36]:


Where_6M = population.where('Population', are.above(6000000000))
year_6M = Where_6M.column('Year')
year_population_crossed_6_billion = year_6M.item(0)
year_population_crossed_6_billion


# ## 5. Miscellanea

# In[38]:


farmers_markets = Table.read_table("farmers_markets.csv")
farmers_markets


# In[40]:


num_farmers_markets_columns = farmers_markets.num_columns
print("The table has", num_farmers_markets_columns, "columns in it!")


# In[42]:


farmers_markets_locations = farmers_markets.select("MarketName", "city", "State", "y", "x")
farmers_markets_locations


# In[44]:


average_latitude = np.average(farmers_markets.column('y'))
average_longitude = np.average(farmers_markets.column('x'))
print("The average of US farmers' markets' coordinates is located at (", average_latitude, ",", average_longitude, ")")


# In[46]:


farmers_markets_without_fmid = farmers_markets.drop("FMID","updateTime")
farmers_markets_without_fmid


# In[48]:


import numpy as np
northern_markets_sketch = farmers_markets_locations.sort('y',descending = True)
northern_markets = northern_markets_sketch.take(np.arange(0,5))
northern_markets


# In[50]:


berkeley_markets = farmers_markets_locations.where('city',are.equal_to('Berkeley'))
berkeley_markets


# ## 6. Summary
# 
# For your reference, here's a table of all the functions and methods we saw in this lab.
# 
# |Name|Example|Purpose|
# |-|-|-|
# |`Table`|`Table()`|Create an empty table, usually to extend with data|
# |`Table.read_table`|`Table.read_table("my_data.csv")`|Create a table from a data file|
# |`with_columns`|`tbl = Table().with_columns("N", np.arange(5), "2*N", np.arange(0, 10, 2))`|Create a copy of a table with more columns|
# |`column`|`tbl.column("N")`|Create an array containing the elements of a column|
# |`sort`|`tbl.sort("N")`|Create a copy of a table sorted by the values in a column|
# |`where`|`tbl.where("N", are.above(2))`|Create a copy of a table with only the rows that match some *predicate*|
# |`num_rows`|`tbl.num_rows`|Compute the number of rows in a table|
# |`num_columns`|`tbl.num_columns`|Compute the number of columns in a table|
# |`select`|`tbl.select("N")`|Create a copy of a table with only some of the columns|
# |`drop`|`tbl.drop("2*N")`|Create a copy of a table without some of the columns|
# |`take`|`tbl.take(np.arange(0, 6, 2))`|Create a copy of the table with only the rows whose indices are in the given array|
# 
# <br/>
# 

# In[ ]:




