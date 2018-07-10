# Portinfo Package

This is very simple package that fetches service name by its port and vice versa.

Service/Port data from [IANA](https://iana.org).


## Install:

### PIP:
pip install portinfo

## Usage:
```
$ portinfo [Service Port | Service Name]
```

### Get service name by port
```
$ portinfo 5432
```

Output:
```
postgresql (PostgreSQL Database) :5432 tcp
postgresql (PostgreSQL Database) :5432 udp
```

### Get port by service name
```
$ portinfo redis
```

output:
```
redis (An advanced key-value cache and store) :6379 tcp
```
