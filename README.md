# spotify-github-profile
Display the song you are listening to on your profile.

This is a Python script that updates your GitHub profile README file with the currently playing track on Spotify.

## Prerequisites

Before using this script, you need to have the following:

- A Spotify account with a valid Spotify access token.
- A GitHub account with a repository where you want to update your profile README file.
- A GitHub personal access token with the `repo` scope. You can create a personal access token in your GitHub account settings.

## Installation

1. Clone this repository using the following command:

```
git clone https://github.com/unofficialdxnny/spotify-github-profile
```

2. Install the required Python packages using pip:

```
pip install requests
```


## Usage

1. Open the `spotify_now_playing.py` file in a code editor.
2. Replace the following variables with your own values:

   - `SPOTIFY_ACCESS_TOKEN`: Your Spotify access token.
   - `GITHUB_ACCESS_TOKEN`: Your GitHub personal access token.
   - `GITHUB_USERNAME`: Your GitHub username.
   - `GITHUB_REPO`: The name of the repository where you want to update your profile README file.
   - `README_FILE_PATH`: The path to your profile README file, relative to the root of your repository.

3. Save the `spotify_now_playing.py` file.

```
python spotify_now_playing.py
```


If the script is successful, it will update your GitHub profile README file with the currently playing track on Spotify.

## Troubleshooting

If you encounter any issues while using this script, try the following:

- Make sure that your Spotify access token is valid and has the `user-read-playback-state` scope.
- Make sure that your GitHub personal access token has the `repo` scope.
- Check that the values of the `GITHUB_USERNAME`, `GITHUB_REPO`, and `README_FILE_PATH` variables in the script match the details of your GitHub repository and profile README file.
- Make sure that you have write access to your GitHub repository.
- Check that your internet connection is working properly.

## Credits

This script was inspired by Kittinan's [Spotify GitHub Profile](https://github.com/kittinan/spotify-github-profile) project.
