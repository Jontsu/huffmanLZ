This week I looked into modifying my solution into a binary implementation in order to compress actual files. This proved to be a lot more complicated than I thought with a lot of issues with the integrity and compression efficiency of the algorithms. The issues mainly revolved around my bits and bytes handling. 

After many failed attempts and without finding a similar reference solution to mine, I used chat.openai.com to help debug my solution. However, this was not succesful either. Ultimately I had to revert back completely and start over. 

After many interations, also using chat.openai.com to help debug the project, I finally have a seemingly working solution. However, I still get integrity issues, it seems to be related to how I handle my bit and byte conversions. Particularly it seems that I am lacking in how I handle the padding here.

Next week I will look into refactoring my code, presently it has some spaghetti elements due to the issues I have encountered and trials on fixing isses that arise on the go. Next week I will also write tests to ensure better test coverage (did not have time this week to do that). 

In retrospect, I think object oriented solution would have been a lot easier following yussiv example. However, I do not intend to change my solution completely and try and fix the issues. Once I have manage this, I will then refactor the code into a clean solution.

## Hours: 23