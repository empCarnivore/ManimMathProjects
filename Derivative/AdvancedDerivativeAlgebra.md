A more advance approach involves the taylor series.\
Instead of have only a linear form,\
the taylor series takes a more polynomial approach.\
This equation takes the change in domain of y to be equal to\
across each n summation of,\
the nth derivative of y of x over n factorial\
where n is a whole number\
This form is more accurate for larger changes than the simple linear form.\

For the product rule, this extends the previous mathematics well for higher derivatives.\
You just take the product of the two series and pull out the corresponding term for the higher order derivative.\
You don't even need to evaluate the whole thing if you're clever.\
For the third derivative the corresponding term is h^3/6.\
Once you have all the terms just divide by h^3/6, and you have the third derivative.

For the chain rule, it's significantly more complicated.\
Take f of g. You can create a taylor series for each. Where f uses the change in g for h. And g uses change in x for h.\
The hard part is that the change in g is actually the difference of the taylor series of g and g.\
So you have terms involving squares and cubes and more of an infinite series and none of it is fun to describe.\

For the third derivative. Take all the change in g terms cubed and less and iterate through each.\

For the linear change in g you'll need to pull the h cubed term.\

For the change in g term is squared, you'll need the h squared term and h linear term. \
The product being h cubed\
The two terms are counted twice like in the binomial theorem or the foil rule\
The final change in g term is cubed. So you just need one h linear term.\
Then just multiply by h^3/6.
