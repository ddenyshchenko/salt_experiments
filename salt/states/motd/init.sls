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
