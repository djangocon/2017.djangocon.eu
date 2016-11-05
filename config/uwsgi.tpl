[uwsgi]
home = %(venv_path)s
chdir = %(www_path)s/%(config_name)s
logto = %(www_path)s/log/uwsgi.log
pythonpath = %(www_path)s
wsgi-file = %(wsgi_file)s
max-requests = 5000
chmod-socket = 666
master = True
vacuum = True
uid = %(www_user)s
gid = %(www_group)s
socket = %(uwsgi_run)s/%(config_name)s%(site_prefix)s.sock
auto-procname = true
procname-prefix = %(config_name)s%(site_prefix)s_
enable-threads = true
env=DJANGO_SETTINGS_MODULE=%(settings_module)s
%(uwsgi_custom_settings)s
