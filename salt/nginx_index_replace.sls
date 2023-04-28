{% set page_filename = 'nginx_index.html' %}
replace_index: 
  file.managed:
    - name: /usr/local/nginx/html/index.html  
    - source: salt://res/{{ page_filename }}
    - makedirs: False
    - replace: True
