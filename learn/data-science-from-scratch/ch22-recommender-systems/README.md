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
