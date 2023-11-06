import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException, status
from models import mydb
import pandas as pd

app = FastAPI()

# Register routes
# root routes
@app.route("/")
def index():
    return render_template(url="/")

# user sign-up and sign-in

@app.route("/signin")
def sign_in():
    cursor1=mydb.cursor()
    username=request.args.get("username")
    password=request.args.get("password")
    if username is None or password is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Details" 
        )
    script_get="SELECT * FROM users WHERE username =%s"
    cursor1.execute(script_get, (username,))
    user_row=cursor1.fetchone()
    if user_row is None:
        # no username = fail
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="username does not exist"
        )
    script_get2="SELECT password FROM user WHERE username =%s"
    cursor1.execute(script_get2)
    user_pass=cursor1.fetchone()
    if password == user_pass:
        return{
            "message":"user signed in succesfully"
        }

@app.route("/signup")
def sign_up():
    cursor2=mydb.cursor()
    username=request.args.get("username")
    password=request.args.get("password")
    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="please enter username and password"
        )
    cursor2.execute("SELECT username FROM users WHERE username=%s")
    old_user=cursor2.fetchone()
    if older_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username is already exist"
        )
    mydb.commit
    script_input1="INSERT INTO user(username, password) VALUES (%s, %s)"
    cursor2.execute(script_input1, (username, password))
    mydb.commit
    return {
        "message": "User created successfully"
    }

# core service
# game rank
@app.route("/get-rank")
def get_rank():
    cursor3=mydb.cursor()
    sql="SELECT name, rating FROM game ORDER BY rating"
    cursor3.execute(sql)
    data=cursor3.fetchall()
    df=pd.DataFrame(data, index=["rank 1", "rank 2", "rank 3", "rank 4", "rank 5", "rank 6", "rank 7", "rank 8", "rank 9", "rank 10"])

# game genre graph
@app.route("/get_genre")
def get_genre_graph();
    cursor4=mydb.cursor()
    sql2="SELECT name, genre, rating FROM game"
    cursor4.execute(sql2)
    data2=cursor4.fetchall()
    fig, axs=plt.subplots(figsize=(12,4))
    data2.groupby(data2["genre"])["value"].mean(),plot(kind="bar", rot=0, ax=axs)
    <axes:xlabel="genre">
    plt.xlabel("games genre");
    plt.ylabel("rating");

# Run
if __name__ == '__main__':
    uvicorn.run()