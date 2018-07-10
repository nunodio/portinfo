#!/usr/bin/env python3
import csv
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = DIR_PATH + "/" + "portinfo.csv"
BLOCK_SIZE = 8192


def print_row(row):
    print("{service} ({description}) :{port} {protocol}".format(
        service=row['Service Name'], port=row['Port Number'],
        protocol=row['Transport Protocol'], description=row['Description']))


def search_port(reader, search_value):
    for row in reader:
        if row['Port Number'] == search_value:
            print_row(row)


def search_service(reader, search_value):
    for row in reader:
        if search_value.lower() in row['Service Name'].lower():
            print_row(row)


def search(search_value):
    with open(FILENAME) as csvfile:
        reader = csv.DictReader(csvfile)
        if search_value.isdigit():
            search_port(reader, search_value)
        else:
            search_service(reader, search_value)
