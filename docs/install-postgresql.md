# Setup a local (development) Postgres database

#### Create the file repository configuration

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

#### Import the repository signing key

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

#### Update the package lists

```
sudo apt-get update;
```

# Install PostgresSQL

```
sudo apt-get -y install postgresql-14 postgresql-client-14;
```

##### Create .pgpass file for passwordless connection

```
echo "
#hostname:port:database:username:password
localhost:5432:blockchainsentry:bcs:bcs-2022.Y1bP1" | tee ~/.pgpass
```

#### Change .pgpass file permission

```
chmod 600 ~/.pgpass
```
