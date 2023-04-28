#--------
# Extracting files
#--------
extract_nginx:
  archive.extracted:
    - source: file:///tmp/nginx.tar.gz
    - name: /tmp/nginx
    
extract_pcre:
  archive.extracted:
    - source: file:///tmp/pcre.tar.gz
    - name: /tmp/pcre
    
extract_zlib:
  archive.extracted:
    - source: file:///tmp/zlib.tar.gz
    - name: /tmp/zlib
    
extract_openssl:
  archive.extracted:
    - source: file:///tmp/openssl.tar.gz
    - name: /tmp/openssl

install_build:
    cmd.run:
      - name: apt-get install build-essential -y

install_zlib:
  cmd.run:
    - name: |
        mv */* .
       # ./configure
       # make
       # make install 
    - cwd: /tmp/zlib

install_pcre:
  cmd.run:
    - name: |
        mv */* .
        #./configure
        #make
        #make install 
    - cwd: /tmp/pcre
    
install_openssl:
  cmd.run:
    - name: |
        mv */* .
        #./Configure darwin64-x86_64-cc --prefix=/usr
        #make
        #make install 
    - cwd: /tmp/openssl
    
        
install_nginx:
  cmd.run:
    - name: |
        cd nginx*
        ./configure \
        --with-pcre=/tmp/pcre \
        --with-zlib=/tmp/zlib \
        --with-openssl=/tmp/openssl \
        --with-http_ssl_module 
        make
        make install 
    - cwd: /tmp/nginx

    
run_nginx:
  cmd.run:
    - name: /usr/local/nginx/sbin/nginx
