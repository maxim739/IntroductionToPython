from operator import itemgetter

import requests

# Make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")  # Make an API call and print the status of the response

# Process information about each submission
submission_ids = r.json()   # Conveert 500 most popular articles to a python list, store in submission_ids
# We'll use these ids to build a set of dictionaries that store information about one of the current submissions
submission_dicts = []   # Create an empty list to tore these dictionaries
for submission_id in submission_ids:   # Only go through the top 30
    # Make a seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}19155826.json"
            # New API call for each submission by generating a new URl which includes thecurrent value of submission_id
    r = requests.get(url)
    print(f"ID: {submission_id}\tStatus: {r.status_code}")  # Print status to see if we were successful
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {     # Create a dict for the submission currently being processed
        'title': response_dict['title'], # Store title of submission
        'hn_link': f"http://news.ycombinator.cpm/item?id={submission_id}",  # Store link to the discussion
        'comments': response_dict['descendants'],   # And the number of comments the submission has received so far
    }
    submission_dicts.append(submission_dict)    # Append each submission _dict to the list submission_dicts

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True) # Use function itemgetter to pull number of comments
                                        # Sorted uses received number of comments to put most commented first

for submission_dict in submission_dicts:    # Loop through list  and print out pieces of information
    print(f"\nTitle: {submission_dict['title']}")   # Print The stitle of the submission
    print(f"Discussion link: {submission_dict['hn_link']}") # Print lin to discussion page
    print(f"Comments: {submission_dict['comments']}")   # Print number of comments the submission has



