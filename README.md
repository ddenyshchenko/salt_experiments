Start by forking this repository.

# Getting started

[Official Salt tutorial](https://docs.saltstack.com/en/latest/topics/tutorials/states_pt1.html)

## Start containers

```bash
docker-compose build
docker-compose up
```

## Enter container

```bash
docker exec -it master bash
```

## Sync grains

Grains are scripts designed to gather informations about your minions (servers). These are not automatically synced on startup,
however if you run a highstate they will be synced.

```bash
salt \* saltutil.sync_all

minion1:
    ----------
    beacons:
    grains:
        - grains.cpuinfo
```

You'll see that it syncs a custom grain that gathers CPU info.

## Writing a state that maintains motd

First create the initial state file init.sls.

```bash
mkdir -p salt/states/motd/files
vi salt/states/motd/init.sls
```

```yaml
motd-packages:
  pkg.latest:
  - pkgs:
    - redhat-lsb

motd:
  file.managed:
  - name: /etc/motd
  - user: root
  - group: wheel
  - mode: 644
  - source: salt://motd/files/motd.jinja
  - template: jinja
```

```bash
vi salt/states/motd/files/motd.jinja
```

```
OS: {{ osfullname }}
OS Version: {{ osrelease }}

```

## Apply state

```bash
salt \* state.sls motd
```

## Stop and remove containers

Ctrl+C will stop docker-compose.

```bash
docker-compose rm -ya
```

## Run command on minions

```bash
salt \* cmd.run hostname
```

# Run command without entering the container

```bash
docker exec -it master salt \* cmd.run hostname
```

# List minions

```bash
salt-key
```

# List grains

```bash
salt \* grains.items
```

# List pillars

```bash
salt \* pillars.items
```

# Sync all

```bash
salt \* saltutil.sync_all
```
