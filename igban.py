import requests

def login(username, password):
    # Same as before...

def report_user(session, user_id):
    # Same as before...

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual Instagram credentials
    your_username = 'Ibsjdhuwfhkg'
    your_password = 'meekmalachi123'
    
    user_id_to_report = '63576865514'  # Replace '123456789' with the user ID of the profile you want to report
    num_reports = 1000

    session = login(your_username, your_password)

    for i in range(num_reports):
        report_user(session, user_id_to_report)
        print(f"Report {i + 1} completed.")

    print("All reports completed.")
