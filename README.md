# obsidian-publish-downloader

A simple Python script to download an entire [Obsidian Publish](https://obsidian.md/publish) site

## Requirements

- [tqdm](https://pypi.org/project/tqdm/)
- [requests](https://pypi.org/project/requests/)

## Example

```
python download.py https://help.obsidian.md/ vault
```

To download the Obsidian Help site to a folder called "vault".

## To-do

- [ ] Parallel downloads
- Implement input validation for URL and folder path.
    - currently providing some inputs can lead to unpredictable behavior
- Use a safer method to parse JSON data, avoiding implicit `eval()` through `json.loads()` on data extracted from the webpage
- Sanitize filenames before writing to disk.
- Improve error handling and logging
- Handle common user mistakes, e.g.:
    - not enough disk space
    - meaningful 4xx and 5xx http responses


## Licensing

This software is licensed under the MIT License. See `LICENSE`.
