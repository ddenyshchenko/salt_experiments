# How to test solution

## Step 1 - build docker images
```bash
docker-compose build
```

## Step 2 - run all containers
```bash
docker-compose up
```

## Step 3 - attach to salt master container
```bash
docker exec -it master bash
```

## Step 4 - check custom pillar
is located in /srv/salt/base/ext/pillar/rest_pillar.py

```bash
salt \* pillar.items
```

find rpms_list key with assigned packages

```
minion1:
    ----------
    default:
        default
...
   rpms_list:
        - bind-utils
        - bzip2
        - curl
        - git
        - jq
        - krb5-libs
        - krb5-workstation
        - lsof
        - mlocate
        - openldap-clients
        - openssh-clients
        - openssh-server
        - tar
        - telnet
        - unzip
        - wget

minion2:
    ----------
    default:
        default
...
    rpms_list:
        - telnet
        - lsof

```

## Step 5 - apply salt state
is located in /srv/salt/base/states/packages_set/init.sls

```bash
salt \* state.apply
```

go to the minions containers and shure that packages exist

## Step 6 - change packages for appropriate minion
* attach to web-rest container

```bash
docker exec -it web-rest bash
```

* go to the configs folder

```bash
cd /opt/web/configs
```

* name convention for packegs lists files:
```
<fqdn for minions>.rpms
```

* edit packages list, for example, add some package to minions2.rpms file


* check pillar rpms_list with

```bash
salt \* pillar.items
```

make shure that added packages exist in pillar

* apply new state


```bash
salt \* state.apply
```

# Files in repository by assignment points
## 1 - Flask web service
Location is ./web

To check separatedly:
```bash
cd ./web
# run REST service
./app.py

# open new terminal in the same ./web dir
# request packages for minion1
curl http://localhost:5000/api/v1/rpms?hostname=minion1
# request packages for minion2
curl http://localhost:5000/api/v1/rpms?hostname=minion2
# request packages by default
curl http://localhost:5000/api/v1/rpms
# Download json file for minion1
wget --content-disposition http://localhost:5000/api/v1/rpms?hostname=minion1
cat minion1.json
```

## 2 - Docker container that runs this as a service
./web/Dockerfile

## 3 - add the Docker container as part of the Docker Compose file

./docker-compose.yml

## 4 - custom External Pillar in SaltStack that does a HTTP request to your Flask service and fetches the JSON file and adds the list to the Pillars namespace
./salt/ext/pillar/rest_pillar.py

## 5 - Salt State that installs the RPM's list in the JSON file
./salt/states/packages_set/init.sls

## 6 - add a parameter to the REST service hostname and allow for overrides spec. for a host
For REST service realized in ./web/app.py with different lists files which name plus .rpms extension should be equal minion's FQDN.
For custom pillar realized in ./salt/ext/pillar/rest_pillar.py with assignment __grains__['fqdn'] value to hostname parameter.


