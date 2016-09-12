{% for pkg in pillar['rpms_list'] %}
{{ pkg }}:
  pkg.installed
{% endfor %}