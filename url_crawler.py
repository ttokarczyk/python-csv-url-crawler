import requests
import csv

inputfile = input("Input file name (including extension): ")
outputfile = input("Output file name (including extension): ")

crawl_end = open(outputfile, mode="w")

writer = csv.writer(crawl_end, delimiter=',', lineterminator='\n')

with open(inputfile, newline='') as crawl_list:
    crawl_reader = csv.reader(crawl_list, delimiter=',')

    for row in crawl_reader:
        print(f"Crawling url:{row[0]} ...")
        req = requests.get(row[0])
        ans = [row[0], req]
        writer.writerow(ans)
        print(f"Crawling url:{row[0]} DONE. {req}")

crawl_end.close()
