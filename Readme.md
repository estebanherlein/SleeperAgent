# Sleeper Agent

## Command and Control via social network persona

Proof of Concept on the idea that sleeper bots can be remotely controlled using hashtags on instagram posts.

Similar to what happens in old fashioned spy networks, in the event that a system administrator discovers the communication of sleeping agents through the nexus with their command and control center, he will not be able to identify the real origin of the Orders neither stop the one giving them.

This kind of structure is a lot more resilient to dismantlement by law enforcement forces.


# How does it work ?

First let's meet the requirements 

`pip install bs4 requests objectpath`


There are two classes InstagramScraper and SleeperAgent.

##### InstagramScraper

This class fetches instagram feeds through a headless browser, traffic will be similar to that generated by a conventional user stalking an instagram profile

##### Sleeper Agent

in this class resides the protocol that the remote bot will follow when identifying a hashtag associated with an order or task.

Currently it features a sleeping stage and 3 placeholders methods 
- **alpha** -  placeholder
- **beta** - placeholder
- **gamma** - placeholder
- **sleep** - Sleep for 24 hours before checking for new orders

##### Main loop

1 - fetches instagram feed that serves as CnC

2 - scrapes post texts

3 - fish the list of post texts for hashtags

4 - identify the last hashtag as the current order, if it's #alpha, #beta or #gamma it will change to each one of those stages. If the last hashtag is none of those it will transition to a sleeping stage 


## TO DO
[ ]code alpha as an information gathering stage

[ ]code beta as a Denial of Service stage

[ ]code gamma as a spreading stage

[ ]add method that changes the contact with CnC

**I am not responsible for what you will do with this**

