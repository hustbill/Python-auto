## Ch22  Recommender Systems


### 1. Recommending What's Popular
One easy approach is to simply recommend what's popular to customers.  


### 2. User-Based Collaborative Filtering
One way of taking a user's interests into account is to look for users who are somehow
similar to him, and then suggest the things that those users are interested in.  

In order to do that, we'll need a way to measure how similar two users are.  Here we'll  
use a metric called cosine similarity.   

GIven two vectors, v and w, it's defined as :  

```python
def  cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

```

### 3. Item-Based Collaborative Filtering
An alternative approach is to compute similarities between interests directly. We can   
then generate suggestions for each user by aggregating interests that are similar to her   
current interests.  


### For Further Exploration
* [Crab] (http://muricoca.github.io/crab)  is a framework for building recommender Systems in python  
* Graphlab also has a recommender toolkit (http://bit.ly/1MF9Tsy).
* [The Netflix Prize](http://www.Netflixprize.com) was a somewhat famous competition to build a better system to recommend movies to Netflix users.  
