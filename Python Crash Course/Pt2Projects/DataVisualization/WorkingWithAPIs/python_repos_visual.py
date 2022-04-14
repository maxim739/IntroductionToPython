import requests  # IMport requests module

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # Continue to print the status to know if there is a problem

# Store API response in a variable
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []  # Create two empty lists to store the data we'll include in the initial chart
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']    # Pull url for the project from repo_dict and assign it to repo_url
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # Generate a link for the URl with HTML anchor tag
                                                        # Anchor tag for links is <a href='URL'>link text</a>
    repo_links.append(repo_link)    # Append link to repo_link

    stars.append(repo_dict['stargazers_count']) # Append the number of stars to the stars list

    # Add for tooltips on chart
    owner = repo_dict['owner']['login'] # Pull owner of project
    description = repo_dict['description']  # Pull description for each project
    label = f"{owner}<br />{description}"   # <br /> creates line break between project owner's username and description
                                            # Plotly allows use of html code withing text elements
    labels.append(label)

# Make a visualization
data = [{   # Define the data list, which contains a dictionary
    'type': 'bar',  # define the type of plot
    'x': repo_links,    # provides data for x values, which are names with links to their pages
    'y': stars,         # provides data for y axis, which is the number of stars
    'hovertext': labels,    # Assign label to key hovertext to create a hovertext when cursor is over a bar
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {   # Define the layout of the chart with a dictionary approach, instead of using the Layout class
    'title': 'Most-Starred Python Projects on GitHub',  # Set a title for the overall chart
    'titlefont': {'size': 28},
    'xaxis': {  # Set a title for the x axis
        'title': 'Repository',
        'titlefont': {'size': 24},  # Control font size of the x axis title
        'tickfont': {'size': 14},   # Control the size of the tick labels
    },
    'yaxis': {   # Set a title for the y axis
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')