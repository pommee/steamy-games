# steamy-games

_Scrape tweets and claim games automatically_

![preview](images/preview.gif)

## Prerequisites

Written and tested in python `3.12.2`.

The [.env](https://github.com/pommee/steamy-games/blob/main/.env) file contains user-data related to Twitter and Steam. This first needs to be filled in before running. Otherwise the application can't authenticate and pull tweets/games.

## Installation

First make sure that dependencies are available.

```bash
pipx install .
```

## Usage

Simply run

```bash
steamygames
```

This will...

- Log into Twitter and fetch tweets related to free steam games.
- Log into Steam and go to each respective game page.
- Add game to library
