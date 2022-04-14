import requests  # IMport requests module

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # Store url of API in a variable
headers = {'Accept': 'application/vnd.github.v3+json'}  # Define the headers for the API call
# This explicitly asks to use this version of the API
r = requests.get(url, headers=headers)  # Use requests to make the call to the API
# Call get and pass it to URL and header we defined, and assign it to variable r
# The response object has attribute status_code which tells us if it is successful, (a code of 200 is successful)

print(f"Status code: {r.status_code}")  # Print the value of status_code to make sure the call went through successfully

# Store API response in a variable
response_dict = r.json()  # Returns info in a json format so we use json() to convert info into a python dictionary
                          # Store response dictionary in response_dict
print(f"Total respositories: {response_dict['total_count']}")  # Print the value associated with 'total_count'
                                                               # This is the number of python repositories on GitHub
# Explore info about repositories
repo_dicts = response_dict['items']  # Store list of dictionaries in repo_dicts and print the length of the list
# Value associated with 'items', a list containing number of dictionaries, each containing data about python repos
print(f"Repositories returned: {len(repo_dicts)}")  # Look at num repositories returned, see how many we have info for

# Examine the first repository
repo_dict = repo_dicts[0]  # Pull first item from repo_dicts and give it to repo_dict
print(f"\nKeys: {len(repo_dict)}")  # Print number of keys to see how much info we have
for key in sorted(repo_dict.keys()):  # Print all the dictionary's keys to see what kind of info is included
    print(key)

# Lets pull out the value for some of the keys in repo_dict

print("\n Selected informaiton about each repository: ")
for repo_dict in repo_dicts:
    print(F"\nName: {repo_dict['name']}") # Print the name of the project
    print(f"Owners: {repo_dict['owner']['login']}") # Use key owner to view the owner dictionary, and login to get the users login name
    print(f"Stars: {repo_dict['stargazers_count']}")    # print how many stars the project has earned
    print(f"Repository: {repo_dict['html_url']}")   # The URL for the projects repository
    print(f"Created: {repo_dict['created_at']}")    # Show when it was created
    print(f"Updated: {repo_dict['created_at']}")    # When it was last updated
    print(f"Description: {repo_dict['description']}")   # Print the repository's description


# Process results
print(response_dict.keys())  # Print the dictionary
# The small API call will usually return successful, but in bigger calls you will want to see the incomplete api calls

# The keys we receive give us some information on the types of data we can extract about a project
# The only true way to know what info is available is through treading the documentation of the API
