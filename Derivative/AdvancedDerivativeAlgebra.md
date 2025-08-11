A more advance approach involves the taylor series.\
Instead of have only the linear part concluded to takes a more polynomial approach.\
The taylor series takes the change in domain of y to equal a sum of (let me pace myself here) y(x), h y'(x), h^2/2 y''(x), h^3/6 y'''(x)...\
It is more accurate for a large change than the simple linear form.\

The second derivative is the derivative of the derivative.\
The third derivative is the derivative of the second derivative.\
This goes on infinitum.

Or you could also use the taylor series as a shortcut.\
For the product rule, this extends easily for higher derivatives.\
You just take the product of the two series and pull out the corresponding term for the higher order derivative.\
You don't even need to evaluate the whole thing if you're clever.\
For the third derivative the corresponding term is h^3/6.\
Once you have all the terms just divide by h^3/6, and you have the third derivative.

For the chain rule, it's significantly more complicated.\
Take f of g. You can create a taylor series for each. Where f uses change in g for h. And g uses change in x for h.\
The hard part is that the change in g is actually the taylor series of g minus g at the original point.\
So you have terms involving squares and cubes and more of an infinite series and none of it is fun to describe.\

For the third derivative. Take all the change in g terms cubed and less. \
These are the terms you pay attention to.\
Iterate through each. And pull out the h^3 terms.\
For the first change in g you'll need to pull the h^3 term.\
The resulting term of y is h^3 g'''(x)/6*f'(g(x))\
The next change in g term is squared so you'll need the h^2 and h term. The product being h^3\
The two terms are counted twice for the same reason the foil rule counts things twice in distributive rules of multiplication\
The resulting term of y is h^3 g'(x)g''(x)f''(g(x))/2\
The final change in g term is cubed. So you just need one h^1 term.\
The final term of y is h^3 g'(x)^3f'''(g(x))/6\
Then just multiply by h^3/6.
