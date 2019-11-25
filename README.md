# Python csv url crawler

Simple Python script that sends requests to url's provided in csv file and exports them to another file file with server response codes.

## Getting Started

Just copy the script and run it on your machine.

### Prerequisites

You need Python 3.6 to run this script.
You need to put the input file in the same location with the script or provide script with full location of the input file.

### Crawling URLs

Running the script

```
python url_crawler.py
```

Providing the input file

```
>>> Input file name (including extension):
example.csv
```

Providing the output file name

```
>>> Output file name (including extension):
output_example.csv
```

Crawling url's from file and saving them to another file
```
>>> Crawling url:https://www.google.com/fake ...
>>> Crawling url:https://www.google.com/fake DONE. <Response [404]>
>>> Crawling url:https://www.google.com ...
>>> Crawling url:https://www.google.com DONE. <Response [200]>
```

Input file contents
```
https://www.google.com/fake
https://www.google.com
```

Output file contents
```
https://www.google.com/fake,<Response [404]>
https://www.google.com,<Response [200]>
```

## Built With

* [Requests](https://pypi.org/project/requests/) - HTTP library for Python


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
