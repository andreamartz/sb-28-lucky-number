### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
A: REST provides a standard protocol for how we set up and name our JSON API routes and how we choose the HTTP verbs to use.

- What is a resource?
A: The resource is what comes after the base url in the path to a RESTful route. It is often something we're representing with a class model in our database, such as users, comments, tags, etc.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
A: JSON APIs are used primarily by developers; there is no need for a user-friendly front end. A new user is created through code.

- What does idempotent mean? Which HTTP verbs are idempotent?
A: A function is idempotent if it gives the same result (for the same input) no matter how many times it is called.

- What is the difference between PUT and PATCH?
A: PUT is used to update all the data on an entire resource; PATCH is used to update just part of the resource.

- What is one way encryption?
A: One-way encryption is not a reversible process; it virtually ensures that the hashed value cannot be decoded.

- What is the purpose of a `salt` when hashing a password?
A: Without salting, a bad actor who knows the deterministic encryption algorithm being used, could create a dictionary of passwords and hashes that could be used to decode hashed passwords. To make this decoding virtually impossible, a randomly generated `salt` is added to each password prior to encryption to make the hashed password much more secure.
Another benefit of using salts is that when many people have chosen the same popular password, the resulting hashed passwords will most likely all be different.

- What is the purpose of the Bcrypt module?
A: Bcrypt is a popular one-way encryption algorithm for password hashing that uses salting.

- What is the difference between authorization and authentication?
A: Authentication is the validation of a user's identity through login credentials. Authorization happens after authentication; it's the process of determining what the authenticated user has permission to do.
