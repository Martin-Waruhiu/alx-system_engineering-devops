# puppet code to kill a process in shell

exec { 'pkill -f killmenow':
  path  => 'usr/bin/:/usr/local/bin/:/bin/'
}
