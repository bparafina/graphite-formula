# this example illustrates key you can overwrite in pillar (or grains)
# the values given here are the default ones already included

graphite:
  config:
    port: 2003
    pickle_port: 2004
    dbtype: sqlite3
    dbname: '/opt/graphite/storage/graphite.db'
    dbuser: ''
    dbpassword: ''
    dbhost: ''
    dbport: ''
    admin_user: 'admin'
    admin_password: 'pbkdf2_sha256$10000$wZuRMciV2VKr$OAtsP+BksbR2DPQUEsY728cbIJmuYf4uXg4tLLGsvi4='
    admin_email: 'admin@example.com'
    max_creates_per_minute: 50
    max_updates_per_second: 500

# a mysql example
    #dbtype: mysql
    #dbname: 'graphite'
    #dbuser: 'graphite'
    #dbpassword: 'graphite'
    #dbhost: 'localhost'
    #dbport: '3306'
    #admin_user: 'admin'
    #admin_password: 'pbkdf2_sha256$10000$wZuRMciV2VKr$OAtsP+BksbR2DPQUEsY728cbIJmuYf4uXg4tLLGsvi4='
    #admin_email: 'admin@example.com'

