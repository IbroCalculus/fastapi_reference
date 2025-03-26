from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


# Define the background task function
def background_task(name: str):
    time.sleep(5)  # Simulate a time-consuming task
    print(f"Hello {name}, your background task is complete!")


# Define the endpoint that triggers the background task
@app.post("/send-email/")
async def send_email(email: str, background_tasks: BackgroundTasks):
    # Add the background task
    background_tasks.add_task(background_task, email)
    return {"message": "Email will be sent in the background"}


# =================================================================


def write_log(message: str):
    time.sleep(10)
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")
    print("Done writing to log")


def perform_other_action():
    print("Performing other action while background task is running...")
    # Simulate doing something else
    time.sleep(5)
    print("Other action completed")


@app.post("/start-tasks/")
async def start_tasks(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)

    # Perform another action immediately, while the background task is running
    perform_other_action()

    return {"message": "Background task started, and other action is performed"}


#   ========================   OUTPUT:  ========================

# Performing other action while background task is running...
# Other action completed
# Done writing to log

