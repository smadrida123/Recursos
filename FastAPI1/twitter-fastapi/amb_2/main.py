#Python
from typing import List
import json

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body
from fastapi import Form
from fastapi import HTTPException

#Modelos
from models import UserBase, UserLogin, User, Tweet, UserRegister, serialize
#Pydantic
from pydantic import EmailStr
from pydantic import Field
from pydantic import BaseModel

app = FastAPI()

#Path Operations


## Users

###Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
    )
def signup(user:UserRegister=Body(...)):
    """
    SIGNUP
   
    Path operation that registers path operation in function
    
    Parameters: 
      -Request body parameter
        -user: UserRegister

    Returns a json with basic user information
     -user_id:UUID
     -email: Emailstr
     -first_name: str
     -last_name:str
     -birth_date:datetime
    """
    with open("users.json","r+",encoding="utf-8") as f:
        results=json.load(f)
        user_dict=user.dict()
        serialize(user_dict)
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


###Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
    )
def Login(user_email: EmailStr=Form(...), password: str = Form(...)):
    """
    Login

    This path operation login a Person in the app

    Parameters:
    - Request body parameters:
        - email: EmailStr
        - password: str

    Returns User information that logged in
    """
    with open("users.json", "r", encoding="utf-8") as f:
        all_users: list = json.loads(f.read())
        user_found: dict = None
        for user in all_users:
            if user["email"] == user_email and user["password"] == password:
                user_found = user
                return User(
                    user_id=user["user_id"],
                    email = user["email"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                )
                
        return user_found
        


###Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
    )
def show_all_users():
    """
    SHOW ALL USERS
    
    This path operations shows all users in app
    
    Parameters: -

    Returns a list with all users information in app
     -user_id:UUID
     -email: Emailstr
     -first_name: str
     -last_name:str
     -birth_date:datetime
    """
    with open("users.json","r+",encoding="utf-8") as f:
        results=json.load(f)

        return results

###Show a user
@app.post(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Show a User",
    tags=["Users"]
    )

def show_a_user(user_email: EmailStr=Form(...)):
    """
    Check if users exists by asking for email
    """   
    with open("users.json", "r", encoding="utf-8") as f:
        all_users: list = json.loads(f.read())
        user_found: dict = None
        for user in all_users:
            if user["email"] == user_email:
                user_found = user
                return User(
                    user_id=user["user_id"],
                    email = user["email"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                )                       
        return user_found
            
###Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user(user_email: EmailStr=Form(...)):
   """
    DELETE A USER
    
    This path operations deletes a user in the app
    
    Parameters: user_email

    Returns a message of succesful operation and deletes user in database.json
    """
   with open("users.json") as f:
    all_users: list = json.loads(f.read())
    # Find the index of the user with the matching ID
    user_index = next((i for i, u in enumerate(all_users) if u["email"] == user_email), None)
    if user_index is None:
        # Raise an HTTPException with a 404 status code if the user doesn't exist
        raise HTTPException(status_code=404, detail="User not found")
    # Remove the user from the list of users
    deleted_user = all_users.pop(user_index)
    # Save the updated list of users to the external JSON file
    with open("users.json", "w") as f:
        json.dump(all_users, f)
    # Return a response indicating that the deletion was successful
    return {"detail": f"User '{deleted_user['first_name']}' deleted successfully"}

        

###Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
    )
def update_a_user():
    pass


##Tweets

###Show all tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    """
    SHOW ALL TWEETS IN HOME
    
    This path operations shows all tweets in home
    
    Parameters: -

    Returns a json with all tweets in app with the following information:
     -tweet_id:UUID
     -content:str
     -created at:Datetime
     -Updated at:Optional[Datetime]
     -by: User
    """
    with open("tweets.json","r+",encoding="utf-8") as f:
        results=json.load(f)

    return results

###Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Create a tweet",
    tags=["Tweets"]
)
def create_tweet(tweet:Tweet=Body(...)):
    """
    POST A TWEET
   
    Path operation post a tweet in the app
    
    Parameters: 
      -Request body parameter
        -tweet: Tweet

    Returns a json with basic tweet information
     -tweet_id:UUID
     -content:str
     -created at:Datetime
     -Updated at:Optional[Datetime]
     -by: User
    """
    with open("tweets.json","r+",encoding="utf-8") as f:
        results=json.load(f)
        tweet_dict=tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"]=str(tweet_dict["created_at"])
        tweet_dict["updated_at"]=str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"]=str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"]=str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

###Show a tweet
@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_tweet():
    pass

###Delete a tweet
@app.delete(
    path="/tweet/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_tweet(tweet_content: str=Form(...)):
    """
    DELETE A TWEET
    
    This path operations deletes a tweet in the app
    
    Parameters: ucontent of tweet that is going to be deleted

    Returns a message of succesful operation and deletes tweet in database.json
    """
    with open("tweets.json") as f:
     all_tweets: list = json.loads(f.read())
    # Find the index of the user with the matching ID
     tweet_index = next((i for i, u in enumerate(all_tweets) if u["content"] == tweet_content), None)
     if tweet_index is None:
        # Raise an HTTPException with a 404 status code if the user doesn't exist
        raise HTTPException(status_code=404, detail="Tweet not found")
    # Remove the user from the list of users
     deleted_tweet = all_tweets.pop(tweet_index)
    # Save the updated list of users to the external JSON file
    with open("tweets.json", "w") as f:
        json.dump(all_tweets, f)
    # Return a response indicating that the deletion was successful
    return {"detail": f"User '{deleted_tweet['content']}' deleted successfully"}

###Update a tweet
@app.put(
    path="/tweet/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_tweet():
    pass


###crear funcion open para solo ingresar parametros