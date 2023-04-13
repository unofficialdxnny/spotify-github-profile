import requests
import base64
import os

# Set up the Spotify API endpoint and access token
SPOTIFY_API_ENDPOINT = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'your-access-token-here'

# Set up the GitHub API endpoint and access token
GITHUB_API_ENDPOINT = 'https://api.github.com'
GITHUB_ACCESS_TOKEN = 'your-access-token-here'

# Set up the repository and file paths for your GitHub profile README file
GITHUB_USERNAME = 'your-github-username-here'
GITHUB_REPO = 'your-github-repo-name-here'
README_FILE_PATH = 'README.md'

# Make a GET request to the Spotify API endpoint to get the currently playing track
response = requests.get(
    SPOTIFY_API_ENDPOINT,
    headers={
        'Authorization': f'Bearer {SPOTIFY_ACCESS_TOKEN}'
    }
)

# Check if the response is valid and contains track data
if response.status_code == 200 and response.json().get('item') is not None:
    track = response.json().get('item')

    # Get the track name and artist name
    track_name = track.get('name')
    artist_name = track.get('artists')[0].get('name')

    # Create the Markdown text to update your GitHub profile README file
    markdown_text = f"🎧 Now playing: [{track_name} by {artist_name}]({track.get('external_urls').get('spotify')})"

    # Get the contents of your GitHub profile README file
    readme_url = f'{GITHUB_API_ENDPOINT}/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{README_FILE_PATH}'
    readme_response = requests.get(
        readme_url,
        headers={
            'Authorization': f'Token {GITHUB_ACCESS_TOKEN}'
        }
    )

    # Check if the response is valid and contains the README file data
    if readme_response.status_code == 200:
        readme_data = readme_response.json()
        readme_content = base64.b64decode(readme_data.get('content')).decode('utf-8')

        # Replace the now playing Markdown text in the README file
        new_readme_content = readme_content.replace(
            readme_content.splitlines()[0],
            markdown_text
        )

        # Update the contents of your GitHub profile README file
        update_url = f'{GITHUB_API_ENDPOINT}/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{README_FILE_PATH}'
        update_response = requests.put(
            update_url,
            headers={
                'Authorization': f'Token {GITHUB_ACCESS_TOKEN}'
            },
            json={
                'message': 'Update Now Playing on Spotify',
                'content': base64.b64encode(new_readme_content.encode('utf-8')).decode('utf-8'),
                'sha': readme_data.get('sha')
            }
        )

        # Check if the update was successful
        if update_response.status_code == 200:
            print('Success: Now Playing on Spotify updated on GitHub profile README file.')
        else:
            print('Error: Unable to update GitHub profile README file.')
    else:
        print('Error: Unable to get GitHub profile README file.')
else:
    print('Error: Unable to get currently playing track from Spotify API.')
