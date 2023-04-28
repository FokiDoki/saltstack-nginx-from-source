{% set nginx_filename = 'nginx-1.24.0.tar.gz' %}
{% set pcre_filename = 'pcre2-10.40.tar.gz' %}
{% set zlib_filename = 'zlib-1.2.13.tar.gz' %}
{% set openssl_filename = 'openssl-1.1.1p.tar.gz' %}



#--------
# Passing Nginx
#--------
copy_nginx:
  file.managed:
    - name: /tmp/nginx.tar.gz
    - source: salt://res/{{ nginx_filename }}
    - makedirs: False

#---------
# Passing dependencies
#---------
copy_dependency_pcre: 
  file.managed: 
    - name: /tmp/pcre.tar.gz
    - source: salt://res/{{ pcre_filename }}
copy_dependency_zlib:
  file.managed:
    - name: /tmp/zlib.tar.gz
    - source: salt://res/{{ zlib_filename }}
copy_dependency_openssl:
  file.managed:
    - name: /tmp/openssl.tar.gz
    - source: salt://res/{{ openssl_filename }}
