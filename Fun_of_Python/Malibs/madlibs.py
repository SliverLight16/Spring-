# string concetentions (how to putt strings together)
# suppose we watn to create a string that says "subscribe to ____"
#youtuber = "Mr. Pang"

# a few ways to do so 
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input ("Another one: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)