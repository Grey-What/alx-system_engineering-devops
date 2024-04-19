# Executing a command
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/user/bin']
}
